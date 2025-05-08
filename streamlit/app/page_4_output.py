from app.page_4.plots import bar_graph
import streamlit as st
from app.sql.genres_by_year import genres_by_year_query
import pandas as pd


@st.cache_data
def make_query(_conn):
    schema = st.secrets.sql_schema.schema

    # Execute the query using SQLAlchemy
    result = _conn.query(genres_by_year_query(schema))

    # Convert the result to a Pandas DataFrame
    df = pd.DataFrame(result)
    return df


def display_output(artist_id):
    conn = st.connection("sql")

    df = make_query(conn)

    bar_graph(df)
