from app.page_3.artist_songs_dataframe import artist_songs_dataframe
import streamlit as st


def display_output(artist_name, artist_id):
    conn = st.connection("sql")

    artist_songs_dataframe(conn, artist_id, artist_name)
