from app.page_3.artist_songs_dataframe import artist_songs_dataframe
import streamlit as st


def display_output(artist_name, artist_id):
    conn = st.connection("sql")
    st.title(
        f":green[{artist_name} has songs in the Top Songs (1950-2024)]"
    )

    artist_songs_dataframe(conn, artist_id)
