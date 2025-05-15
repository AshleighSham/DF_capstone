import pandas as pd
import os
from sqlalchemy import text, Table, MetaData, types
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import sessionmaker
from config.db_config import load_db_config, DatabaseConfigError
from utils.db_utils import (
    get_db_connection,
    DatabaseConnectionError,
    QueryExecutionError,
)
from etl.load.post_load_enrichment import enrich_database_data
import numpy as np


ROOT_DIR = "c:/Users/ashle/Documents/GitHub/DF_capstone"
INDEXES_PATH = os.path.join(ROOT_DIR, 'etl', 'sql', 'indexes')
QUERY_PATH = os.path.join(ROOT_DIR, 'etl', 'sql')

TARGET_TABLE_NAME = "as_capstone"

LOAD_QUERY_FILES = {
    "set_primary_key": os.path.join(
        os.path.dirname(QUERY_PATH), "sql/set_primary_key.sql"
    ),
}


DATA_TYPES = {'track_id': types.String,
              'track_name': types.String,
              'artist_id': types.String,
              'artist_names': types.String,
              'album_id': types.String,
              'album_name': types.String,
              'album_artist_id': types.String,
              'album_artist_names': types.String,
              'album_image_url': types.String,
              'isrc': types.String,
              'album_year': types.INTEGER,
              'disc_number': types.INTEGER,
              'track_number': types.INTEGER,
              'explicit': types.BOOLEAN,
              'popularity': types.INTEGER,
              'pop': types.BOOLEAN,
              'rock': types.BOOLEAN,
              'hip_hop': types.BOOLEAN,
              'electronic': types.BOOLEAN,
              'rnb_soul': types.BOOLEAN,
              'folk': types.BOOLEAN,
              'country': types.BOOLEAN,
              'ska': types.BOOLEAN,
              'dance_disco': types.BOOLEAN,
              'indie_alt': types.BOOLEAN,
              'retro_vintage': types.BOOLEAN,
              'novelty': types.BOOLEAN,
              'easy_listening': types.BOOLEAN,
              'cultural': types.BOOLEAN,
              'jazz': types.BOOLEAN,
              'genre_count': types.INTEGER
              }

# Mapping SQLAlchemy types to Pandas types
SQLALCHEMY_TO_PANDAS_TYPES = {
    types.INTEGER: "int64",
    types.BOOLEAN: "bool",
    types.String: "str",
    types.Float: "float64"
}


def enforce_data_types(data: pd.DataFrame, data_types: dict) -> pd.DataFrame:

    for column, sql_type in data_types.items():
        # map SQLAlchemy type to Pandas type
        pandas_type = SQLALCHEMY_TO_PANDAS_TYPES.get(type(sql_type))
        if pandas_type:
            try:
                data[column] = data[column].astype(pandas_type)

            except KeyError:
                print(f"Column {column} not found in DataFrame.")

            except Exception as e:
                print(f"Error converting {column} to {pandas_type}: {e}")

    return data


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

    # save data data to an SQL table in target database
    load_table(data)

    # create views
    enrich_database_data()

    return None


def load_table(data):
    try:
        connection_details = load_db_config()["target_database"]
        connection = get_db_connection(connection_details)

        schema = connection_details.get("dbschema", "public")

        with connection.begin():
            # set the schema for the session
            connection.execute(text(f"SET search_path TO {schema}"))

            # load data into the table
            data.to_sql(
                TARGET_TABLE_NAME, connection, if_exists="fail", index=False,
                dtype=DATA_TYPES
            )

            # set the primary key
            set_primary_key(connection)

    except ValueError:
        print("Target table exists")
        print("Upserting data into existing table instead")
        upsert_on_existing_table(data, connection)

    except DatabaseConfigError as e:
        print(f"Target database not configured correctly: {e}")
        raise

    except DatabaseConnectionError as e:
        print(
            f"Failed to connect to the database: {e}"
        )
        raise

    except pd.errors.DatabaseError as e:
        print(f"Failed to create data table: {e}")
        raise QueryExecutionError(f"Failed to execute query: {e}")

    finally:
        connection.close()
        print("Successfully closed database connection.")


def upsert_on_existing_table(data: pd.DataFrame, connection):
    """
    Upsert data into an existing table
    """
    try:
        if "index" in data.columns:
            data = data.drop(columns=["index"])

        # Eenforce data types
        data = enforce_data_types(data, DATA_TYPES)
        data['popularity'] = data['popularity'].astype(np.int32)
        data['album_year'] = data['album_year'].astype(np.int32)
        data['disc_number'] = data['disc_number'].astype(np.int32)
        data['track_number'] = data['track_number'].astype(np.int32)
        data['genre_count'] = data['genre_count'].astype(np.int32)

        data_dict = data.to_dict(orient="records")

        # reflect the table from the database
        metadata = MetaData()
        table = Table(TARGET_TABLE_NAME, metadata, autoload_with=connection)

        # create an insert statement with an upsert (ON CONFLICT) clause
        insert_stmt = insert(table).values(data_dict)
        upsert_stmt = insert_stmt.on_conflict_do_update(
            constraint='pk_track_id',
            set_={
                'popularity': insert_stmt.excluded.popularity
            },
        )

        # create a session
        Session = sessionmaker(bind=connection)
        session = Session()

        # Execute the upsert statement within a transaction
        print("Executing upsert statement...")
        session.execute(upsert_stmt)
        session.flush()
        print("Committing transaction...")
        session.commit()
        print("Transaction committed successfully.")

    except SQLAlchemyError as e:
        if "session" in locals():
            session.rollback()
        print(f"SQLAlchemyError occurred: {e}")
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
        connection.execute(executable_sql)
        print("Primary key set on target table")

    except Exception as e:
        print(f"Error setting primary key on target table: {e}")
        raise
