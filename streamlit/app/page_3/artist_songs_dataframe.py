import streamlit as st
from app.sql.artist_songs_in_top_songs import find_artist_songs


def artist_songs_dataframe(conn, artist_id, artist_name):

    schema = st.secrets.sql_schema.schema

    df = conn.query(
        f"SELECT * FROM {schema}.as_artists_track WHERE"
        f" artist_id = '{artist_id}'"
    )

    if df.empty:
        st.error(
            ("No tracks found in the top songs (1950-2024) by "
             "this artist :( Try again!")
        )
    else:
        st.title(
                ":green[{a} has {b} songs in the Top Songs (1950-2024)]".format(
                    a=artist_name,
                    b=len(df)
                )
            )
        df2 = conn.query(find_artist_songs(artist_id, schema))
        st.dataframe(df2,
                     hide_index=True,
                     height=35*len(df2)+38,
                     column_config={
                         'album_image_url': None,
                         'album_name': 'Album Name',
                         'disc_number': 'Disc Number',
                         'track_number': 'Track Number',
                         'album_year': 'Release Year',
                         'track_name': 'Track Name',
                         'artist_names': 'Artist Names',
                         'track_duration_ms': st.column_config.TimeColumn(
                             'Duration (min)', format="mm:ss"),
                         'explicit': 'Explicit',
                         'popularity': 'Popularity (0-100)'
                         },
                     )
