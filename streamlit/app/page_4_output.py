from app.page_4.genres_by_year import genres_by_year
from app.page_4.properties_by_year import properties_by_year
import streamlit as st


def display_output(artist_id):
    conn = st.connection("sql")

    genres_by_year(conn)

    properties_by_year(conn)
