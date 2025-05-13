from app.page_2_output import display_output
import streamlit as st

st.set_page_config(page_title="Artist Top Albums",
                   page_icon="🎵",
                   layout="wide")

bl1 = (
    "https://developer.spotify.com/documentation/web-api/"
    "reference/get-multiple-albums"
)

bl2 = (
    "https://developer.spotify.com/documentation/web-api/"
    "reference/get-several-tracks"
)

st.sidebar.title(":green[Artist Top Albums]")
with st.sidebar:
    st.write(("The albums listed in the Artist Top Albums section are"
              " those that feature tracks appearing in the Artist Top"
              " Tracks. General information about these albums is"
              " provided at the top of the page. For more detailed"
              " data on a specific album, please select it from the"
              " Album Data section below."))
    st.link_button(":green[Go to Spotify's Get Several Ablums API]", bl1)
    st.link_button(":green[Go to Spotify's Get Several Tracks API]", bl2)
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
