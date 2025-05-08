import streamlit as st
from app.page_1.artist_top_tracks import get_artists_top_tracks
from app.page_1.artist_data import get_artists_data
from app.page_1.plots import scatter_plot


def display_output(artist_id, token):

    results = get_artists_top_tracks(token, artist_id)
    artist_data = get_artists_data(token, artist_id)
    st.title(f":green[{artist_data[0]}'s Top Tracks]")

    space1, col1, space2, col2 = st.columns([1, 2, 1, 4],
                                            vertical_alignment='center')

    with col1:
        st.image(artist_data[2], width=400)
        col3, col4 = st.columns([2, 3])
        with col3:
            st.subheader(f"{artist_data[1]}")
            st.text('Popularity')
        with col4:
            st.subheader(f"{artist_data[3]}")
            st.text('Followers')

    with col2:
        for track in range(len(results)):
            st.write(
                f":green[**{track + 1}.**] {results.loc[track, 'name']} - "
                f"*:gray[{results.loc[track, 'album']}]*"
            )

    st.write("---")
    scatter_plot(results)
