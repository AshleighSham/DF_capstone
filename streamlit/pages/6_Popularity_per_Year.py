import streamlit as st
from app.page_6_output import display_output

st.set_page_config(page_title="Popularity from 1950 - 2024",
                   page_icon="🎵",
                   layout="wide")

bl1 = (
    "https://www.kaggle.com/datasets/joebeachcapital/"
    "top-10000-spotify-songs-1960-now"
    )

st.sidebar.title(":green[Popularity from 1950 - 2024]")

with st.sidebar:
    st.write(("Spotify's API quanitfies the popularity of a song"
              " on a scale of 0-100, calculated by an algorithm that"
              " is based mostly on the total numbe rof plays and"
              " how recent those plays are. I.E. songs that are played"
              " alot recently have a higher popularity than those"
              " that were played more in the past."))
    st.write(("Duplicate tracks, i.e. the same track on different"
              " albums are treated seperately, and an artists"
              " overall popularity is based on their track popularities"))
    st.link_button(":green[Go to Kaggle Dataset]", bl1)

st.header(":green[Spotify Data Explorer]")
st.write("---")

st.session_state.artist_name = st.session_state.artist_name
st.session_state.artist_id = st.session_state.artist_id
st.session_state.token = st.session_state.token

display_output(st.session_state.artist_id)
