import pandas as pd
import os
from sqlalchemy import text, Table, MetaData
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import sessionmaker
from config.db_config import load_db_config, DatabaseConfigError
from utils.db_utils import (
    get_db_connection,
    DatabaseConnectionError,
    QueryExecutionError,
)


ROOT_DIR = "c:/Users/ashle/Documents/GitHub/DF_capstone"
INDEXES_PATH = os.path.join(ROOT_DIR, 'etl', 'sql', 'indexes')
QUERY_PATH = os.path.join(ROOT_DIR, 'etl', 'sql')

TARGET_TABLE_NAME = "as_capstone"

LOAD_QUERY_FILES = {
    "load_merged_data": os.path.join(
        os.path.dirname(__file__), "load_merged_data.sql"
    ),
    "load_high_value_customers": os.path.join(
        os.path.dirname(__file__), "load_high_value_customers.sql"
    ),
    "load_cleaned_high_value_customers": os.path.join(
        os.path.dirname(__file__), "load_cleaned_high_value_customers.sql"
    ),
    "set_primary_key": os.path.join(
        os.path.dirname(QUERY_PATH), "sql/set_primary_key.sql"
    ),
}


def import_sql_query(filename):
    try:
        with open(filename, 'r') as file:
            imported_query = file.read().replace('\n', ' ').strip()
            print(f"Successfully imported query from {filename}")
            return imported_query
    except FileNotFoundError as e:
        print(f"Failed to import query: {filename} not found")
        raise QueryExecutionError(f"Failed to import query: {e}")


def load_data(data):
    try:
        connection_details = load_db_config()["target_database"]
        connection = get_db_connection(connection_details)
        data.to_sql(
            TARGET_TABLE_NAME, connection, if_exists="fail", index=False
        )
        set_primary_key(connection)
    except ValueError:
        print("Target table exists")
        print("Upserting data into existing table instead")
        set_primary_key(connection)
        upsert_on_existing_table(data, connection)
    except DatabaseConfigError as e:
        print(f"Target database not configured correctly: {e}")
        raise
    except DatabaseConnectionError as e:
        print(
            f"Failed to connect to the database when creating data table:"
            f" {e}"
        )
        raise
    except pd.errors.DatabaseError as e:
        print(f"Failed to create data table: {e}")
        raise QueryExecutionError(f"Failed to execute query: {e}")
    finally:
        connection.close()
        print("Successfully closed database connection.")


def upsert_on_existing_table(data: pd.DataFrame, connection):
    try:
        data_dict = data.to_dict(orient="records")

        # Reflect the table from the database
        metadata = MetaData()
        table = Table(TARGET_TABLE_NAME, metadata, autoload_with=connection)

        # Create an insert statement with an upsert (ON CONFLICT) clause
        insert_stmt = insert(table).values(data_dict)
        upsert_stmt = insert_stmt.on_conflict_do_update(
            index_elements=["track_id"],
            set_={
                col.name: insert_stmt.excluded[col.name]
                for col in table.columns
                if col.name != "track_id"
            },
        )

        # Create a session
        Session = sessionmaker(bind=connection)
        session = Session()

        # # Execute the upsert statement within a transaction
        session.execute(upsert_stmt)
        # session.commit()
    except SQLAlchemyError as e:
        if "session" in locals():
            session.rollback()
        raise QueryExecutionError(f"Failed to execute upsert query: {e}")
    except Exception as e:
        if "session" in locals():
            session.rollback()
        print(f"An error occurred when upserting data: {e}")
        raise
    finally:
        if "session" in locals():
            session.close()
        print("Successfully closed database session.")


def set_primary_key(connection):
    create_primary_key_query = import_sql_query(
        LOAD_QUERY_FILES["set_primary_key"]
    )
    executable_sql = text(create_primary_key_query)
    try:
        with connection.begin():
            connection.execute(executable_sql)
            print("Primary key set on target table")
            connection.commit()
    except Exception as e:
        print(f"Error setting primary key on target table: {e}")
        raise