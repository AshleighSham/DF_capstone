from app.page_4.plots import bar_graph
from app.sql.genres_by_year import genres_by_year_query
import streamlit as st
import pandas as pd


def genres_by_year(conn):
    schema = st.secrets.sql_schema.schema

    # Execute the query using SQLAlchemy
    result = conn.query(genres_by_year_query(schema))

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
