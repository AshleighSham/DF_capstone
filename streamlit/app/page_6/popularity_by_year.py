from app.page_6.plots import heat_map
import streamlit as st
import pandas as pd
from app.sql.popularity_by_year import popularity_by_year_query


def popularity_by_year(conn):
    schema = st.secrets.sql_schema.schema

    # Execute the query using SQLAlchemy
    result = conn.query(popularity_by_year_query(schema))

    # Convert the result to a Pandas DataFrame
    df = pd.DataFrame(result)

    space1, col1, spac2 = st.columns([1, 3, 1])
    with col1:
        heat_map(df)
