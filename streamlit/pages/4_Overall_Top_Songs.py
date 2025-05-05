import streamlit as st
from app.page_4_output import display_output

st.set_page_config(page_title="Top Songs from 1950 - 2024", page_icon="🎵", layout="wide")
st.sidebar.title(":green[Top Songs from 1950 - 2024]")

st.header(":green[Spotify Data Explorer]")
st.write("---")
# Check if session_state contains the required attributes
if 'artist_id' not in st.session_state or 'token' not in st.session_state:
    st.error("Please enter an artist on the homepage.")
    st.stop()  # Stop further execution

st.session_state.artist_name = st.session_state.artist_name
st.session_state.artist_id = st.session_state.artist_id
st.session_state.token = st.session_state.token

display_output(st.session_state.artist_id)
