from app.page_5.plots import line_plots
import streamlit as st
import pandas as pd
from app.sql.features_by_year import features_by_year_query


def properties_by_year(conn):
    schema = st.secrets.sql_schema.schema

    # Execute the query using SQLAlchemy
    result = conn.query(features_by_year_query(schema))

    # Convert the result to a Pandas DataFrame
    df = pd.DataFrame(result)

    line_plots(df)
