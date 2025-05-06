from app.page_2_output import display_output
import streamlit as st

st.set_page_config(page_title="Artist Top Albums", page_icon="🎵", layout="wide")
st.sidebar.title(":green[Artist Top Albums]")
with st.sidebar:
    st.link_button(":green[Go to Spotify's Get Several Ablums API]", "https://developer.spotify.com/documentation/web-api/reference/get-multiple-albums")
    st.link_button(":green[Go to Spotify's Get Several Tracks API]", "https://developer.spotify.com/documentation/web-api/reference/get-several-tracks")
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
