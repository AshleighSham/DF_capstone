from app.page_6.popularity_by_year import popularity_by_year
import streamlit as st


def display_output(artist_id):
    conn = st.connection("sql")

    popularity_by_year(conn)
