import os
from app.sql_utils import import_sql_query
from app.page_4.plots import bar_graph
import streamlit as st
import pandas as pd

ROOT_DIR = "c:/Users/ashle/Documents/GitHub/DF_capstone"
QUERY_PATH = os.path.join(ROOT_DIR, 'streamlit', 'app', 'sql')


def genres_by_year(conn):
    sql = import_sql_query(os.path.join(QUERY_PATH, "genres_by_year.sql"))

    # Execute the query using SQLAlchemy
    result = conn.query(sql)

    # Convert the result to a Pandas DataFrame
    df = pd.DataFrame(result)

    dynamic_filters = st.multiselect('Select Genres',
                                     options=[
                                         'Pop', 'Rock', 'Hip-Hop',
                                         'Electronic', 'R&B/soul',
                                         'Folk', 'Country', 'Ska',
                                         'Disco/Dance', 'Indie/Alternative',
                                         'Retro/Vintage', 'Novelty',
                                         'Easy Listening'
                                         ],
                                     default=[
                                         'Pop', 'Rock', 'Hip-Hop',
                                         'Electronic', 'R&B/soul',
                                         'Folk', 'Country', 'Ska',
                                         'Disco/Dance', 'Indie/Alternative',
                                         'Retro/Vintage', 'Novelty',
                                         'Easy Listening'
                                         ]
                                     )

    bar_graph(df, dynamic_filters)
