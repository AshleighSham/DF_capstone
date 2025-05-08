import streamlit as st
from app.page_1_output import display_output


bl1 = (
    "https://developer.spotify.com/documentation/"
    "web-api/reference/get-an-artist"
)

bl2 = (
    "https://developer.spotify.com/documentation/web-api/"
    "reference/get-an-artists-top-tracks"
)
st.set_page_config(page_title="Artist Top Tracks",
                   page_icon="🎵",
                   layout="wide")

st.sidebar.title(":green[Artist Top Tracks]")
with st.sidebar:
    st.link_button(":green[Go to Spotify's Get Artist API]",
                   bl1)
    st.link_button(":green[Go to Spotify's Get Artist's Top Tracks API]",
                   bl2)
st.header(":green[Spotify Data Explorer]")
st.write("---")
# Check if session_state contains the required attributes
if 'artist_id' not in st.session_state or 'token' not in st.session_state:
    st.error("Please enter an artist on the homepage.")
    st.stop()  # Stop further execution

st.session_state.artist_name = st.session_state.artist_name
st.session_state.artist_id = st.session_state.artist_id
st.session_state.token = st.session_state.token

display_output(st.session_state.artist_id, st.session_state.token)
