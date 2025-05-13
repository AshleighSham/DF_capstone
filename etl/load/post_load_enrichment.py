import os
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from config.db_config import load_db_config
from utils.db_utils import create_db_engine
from utils.sql_utils import import_sql_query


ROOT_DIR = "c:/Users/ashle/Documents/GitHub/DF_capstone"
QUERY_PATH = os.path.join(ROOT_DIR, 'etl', 'sql')

QUERY_FILE_NAMES = {
    "gby": "genres_by_year.sql",
    "pby": "properties_by_year.sql",
    "at": "artists_track_table.sql",
    "poby": "popularity_by_year.sql"
}


def enrich_database_data():

    create_views()


def create_views():
    # import the SQL query from the file
    # create view in database
    try:
        for query_file in QUERY_FILE_NAMES.values():

            sql = import_sql_query(os.path.join(QUERY_PATH, query_file))
            executable_sql = text(sql)
            connection_details = load_db_config()["target_database"]
            schema = connection_details.get("dbschema", "public")

            engine = create_db_engine(connection_details)
            Session = sessionmaker(bind=engine)
            session = Session()

            # Set the schema for the session
            session.execute(text(f"SET search_path TO {schema}"))

            session.execute(
                executable_sql
            )
            print(f"{query_file} view created")
            session.commit()

    except Exception as e:
        print(f"Error creating view: {e}")
        raise

    finally:
        session.close()
