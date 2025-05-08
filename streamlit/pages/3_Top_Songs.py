import streamlit as st
from app.page_3_output import display_output

st.set_page_config(page_title="Artist Tracks in Top Songs from 1950 - 2024",
                   page_icon="🎵",
                   layout="wide")
st.sidebar.title(":green[Artist Tracks in Top Songs from 1950 - 2024]")

bl1 = (
    "https://www.kaggle.com/datasets/joebeachcapital/"
    "top-10000-spotify-songs-1960-now"
    )

with st.sidebar:
    st.write(
        "The 'Top 10000 Spotify Songs - ARIA and Billboard Charts' is a "
        "comprehensive collection of 10,000 of the most popular songs that "
        "have dominated the music scene from 1950 to the present day. This "
        "dataset was curated based on rankings from both the ARIA "
        "(Australian Recording Industry Association) and Billboard charts, "
        "ensuring a diverse representation of songs that have achieved "
        "immense commercial success and cultural significance."
    )
    st.link_button(":green[Go to Kaggle Dataset]", bl1)

st.header(":green[Spotify Data Explorer]")
st.write("---")
# Check if session_state contains the required attributes
if 'artist_id' not in st.session_state or 'token' not in st.session_state:
    st.error("Please enter an artist on the homepage.")
    st.stop()  # Stop further execution

st.session_state.artist_name = st.session_state.artist_name
st.session_state.artist_id = st.session_state.artist_id
st.session_state.token = st.session_state.token

display_output(st.session_state.artist_name, st.session_state.artist_id)
