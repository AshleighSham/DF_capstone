import os
from app.sql_utils import import_sql_query
from app.page_4.line_plot import line_plots
import pandas as pd

ROOT_DIR = "c:/Users/ashle/Documents/GitHub/DF_capstone"
QUERY_PATH = os.path.join(ROOT_DIR, 'streamlit', 'app', 'sql')


def properties_by_year(conn):
    sql = import_sql_query(os.path.join(QUERY_PATH, "properties_by_year.sql"))

    # Execute the query using SQLAlchemy
    result = conn.query(sql)

    # Convert the result to a Pandas DataFrame
    df = pd.DataFrame(result)

    line_plots(df)
