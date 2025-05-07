import streamlit as st
from app.sql.artist_songs_in_top_songs import find_artist_songs


def artist_songs_dataframe(conn, artist_id, artist_name):

    df = conn.query(
        "SELECT * FROM c12de.as_artists_track WHERE artist_id = :artist_id",
        params={"artist_id": artist_id}
    )

    if df.empty:
        st.error(
            "No tracks found in the top songs (1950-2024) :( Try again!"
        )
    else:
        st.title(
                f":green[{artist_name} has songs in the Top Songs (1950-2024)]"
            )
        df2 = conn.query(find_artist_songs(artist_id))
        st.dataframe(df2,
                     hide_index=True,
                     height=35*len(df2)+38,
                     column_config={
                         'album_image_url': None,
                         'album_name': 'Album Name',
                         'disc_number': 'Disc Number',
                         'track_number': 'Track Number',
                         'album_release_date': 'Release Date',
                         'track_name': 'Track Name',
                         'artist_names': 'Artist Names',
                         'track_duration_ms': st.column_config.TimeColumn(
                             'Duration (min)', format="mm:ss"
                         ),
                         'explicit': 'Explicit',
                         'popularity': 'Popularity (0-100)'
                         },
                     )
