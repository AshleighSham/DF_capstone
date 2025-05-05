import streamlit as st

st.set_page_config(page_title="Global Top Songs", page_icon="🎵", layout="wide")
st.sidebar.title(":green[Global Top Songs]")

st.header(":green[Spotify Data Explorer]")
st.write("---")
# Check if session_state contains the required attributes
if 'artist_id' not in st.session_state or 'token' not in st.session_state:
    st.error("Please enter an artist on the homepage.")
    st.stop()  # Stop further execution

st.session_state.artist_name = st.session_state.artist_name
st.session_state.artist_id = st.session_state.artist_id
st.session_state.token = st.session_state.token
