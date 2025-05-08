import streamlit as st
from app.page_1.artist_top_tracks import get_artists_top_tracks
from app.page_1.artist_data import get_artists_data
from app.page_2.artist_albums import get_artist_albums
from app.page_2.dataframes import (
    get_full_album_dataframe,
    display_albums_dataframe,
    display_individual_album_dataframe
)
from app.page_2.plots import individual_album_scatter, all_album_scatter


def display_output(artist_id, token):
    results = get_artists_top_tracks(token, artist_id)
    artist_data = get_artists_data(token, artist_id)
    st.session_state.artist_name = artist_data[0]
    st.title(f":green[{artist_data[0]}'s Top Albums]")

    albums_df = results[['album',
                         'release_date',
                         'album_id',
                         'album_image']].copy()

    albums_df.drop_duplicates(subset=['album'], inplace=True)

    overall, individual_albums = get_artist_albums(
        token,
        albums_df['album_id'].tolist()
    )

    albums_df = get_full_album_dataframe(albums_df, overall)

    album_names = {}
    for key in individual_albums:
        album_names[key] = albums_df[albums_df.index == key]['album'].values[0]

    display_albums_dataframe(albums_df)

    all_album_scatter(individual_albums, album_names, albums_df)

    st.write("---")
    st.title(":green[Album Data]")
    option = st.selectbox("Select an album",
                          options=list(album_names.values()),
                          key="album_select")

    album_id = [
        key for key, value in album_names.items() if value == option
    ][0]

    space1, col1, space2, col2 = st.columns([1, 4, 1, 8],
                                            vertical_alignment="center")
    with col1:
        if len(individual_albums[album_id]) < 10:
            width = 35 * 10 + 38
        else:
            width = 35 * len(individual_albums[album_id]) + 38
        st.image(albums_df.loc[album_id, 'album_image'], width=width)
    with col2:
        display_individual_album_dataframe(individual_albums, album_id)

    individual_album_scatter(individual_albums[album_id],
                             album_names[album_id])
