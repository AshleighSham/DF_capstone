from app.page_6.plots import heat_map
import streamlit as st
import pandas as pd
from app.sql.popularity_by_year import popularity_by_year_query


def popularity_by_year(conn):
    schema = st.secrets.sql_schema.schema

    with st.sidebar:
        group_size = st.number_input(':green[Select Year Group Size:]',
                                     min_value=1,
                                     max_value=15,
                                     value=5)

    # Execute the query using SQLAlchemy
    result = conn.query(popularity_by_year_query(schema, group_size))

    # Convert the result to a Pandas DataFrame
    df = pd.DataFrame(result)

    space1, col1, spac2 = st.columns([1, 10, 1])
    with col1:
        heat_map(df)
