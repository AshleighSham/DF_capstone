import streamlit as st
from app.page_5_output import display_output

st.set_page_config(page_title="Track Feature Trends from 1950 - 2024",
                   page_icon="🎵",
                   layout="wide")

bl1 = (
    "https://developer.spotify.com/documentation/web-api/"
    "reference/get-audio-features"
)

bl2 = (
    "https://www.kaggle.com/datasets/joebeachcapital/"
    "top-10000-spotify-songs-1960-now"
    )

st.sidebar.title(":green[Track Feature Trends from 1950 - 2024]")
with st.sidebar:
    features = {
        "Danceability": (
            "Combines elements such as tempo, rhythm, and overall regularity. "
            "With 0 being least danceable and 1 being the most."
        ),
        "Energy": (
            "A measure from 0.0 to 1.0 representing intensity and activity."
        ),
        "Loudness": (
            "The overall loudness of a track in decibels (dB), typically "
            "ranging between -60 and 0 dB."
        ),
        "Speechiness": (
            "Detects the presence of spoken words in a track. Values below"
            " 0.33 likely have little to no speech."
        ),
        "Acousticness": (
            "A confidence measure from 0.0 to 1.0 of whether the track is"
            " acoustic. 1.0 represents high confidence."
        ),
        "Instrumentalness": (
            "Predicts whether a track contains no vocals. Values above 0.5"
            " represent instrumental tracks."
        ),
        "Liveness": (
            "Detects the presence of an audience in the recording. A value"
            " above 0.8 indicates a live track."
        ),
        "Valence": (
            "A measure from 0.0 to 1.0 describing the musical positiveness"
            " conveyed by a track."
        ),
        "Tempo": (
            "The overall estimated tempo of a track in beats per minute (BPM)."
        ),
    }

    for feature, description in features.items():
        st.write(f"**:green[{feature}]:** {description}")

    st.link_button(":green[Got to Spotify Audio Features API]", bl1)
    st.link_button(":green[Go to Kaggle Dataset]", bl2)

st.header(":green[Spotify Data Explorer]")
st.write("---")

st.session_state.artist_name = st.session_state.artist_name
st.session_state.artist_id = st.session_state.artist_id
st.session_state.token = st.session_state.token

display_output(st.session_state.artist_id)
