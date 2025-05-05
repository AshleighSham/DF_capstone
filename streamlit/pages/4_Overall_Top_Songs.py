import streamlit as st
from app.page_4_output import display_output

st.set_page_config(page_title="Top Songs from 1950 - 2024", page_icon="🎵", layout="wide")
st.sidebar.title(":green[Top Songs from 1950 - 2024]")
with st.sidebar:
    st.write("The tracks properties are defined by spotify as follows:")
    st.write("**:green[Danceability]:** Combines elements suhc as tempo, rhythm and overall regularity. Wiht 0 being least danceable and 1 being the most.")
    st.write("**:green[Energy]:** Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity.")
    st.write("**:green[Loudness]:** The overall loudness of a track in decibels (dB) with values typically range between -60 and 0 db.")
    st.write("**:green[Speechiness]:** Speechiness detects the presence of spoken words in a track. With 1 for peotry and values below 0.33 likely have little to no speech.")
    st.write("**:green[Acousticness]:** A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.")
    st.write("**:green[Instrumentalness]:** Predicts whether a track contains no vocals. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.")
    st.write("**:green[Liveness]:** Detects the presence of an audience in the recording. A value above 0.8 provides strong likelihood that the track is live.")
    st.write("**:green[Valence]:** A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track.")
    st.write("**:green[Tempo]:** The overall estimated tempo of a track in beats per minute (BPM).")
    
st.header(":green[Spotify Data Explorer]")
st.write("---")

st.session_state.artist_name = st.session_state.artist_name
st.session_state.artist_id = st.session_state.artist_id
st.session_state.token = st.session_state.token

display_output(st.session_state.artist_id)
