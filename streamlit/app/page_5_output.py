from app.page_5.properties_by_year import properties_by_year
import streamlit as st


def display_output(artist_id):
    conn = st.connection("sql")

    properties_by_year(conn)
