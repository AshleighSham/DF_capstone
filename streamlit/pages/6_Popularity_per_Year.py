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
    st.link_button(":green[Go to Kaggle Dataset]", bl1)

st.header(":green[Spotify Data Explorer]")
st.write("---")

st.session_state.artist_name = st.session_state.artist_name
st.session_state.artist_id = st.session_state.artist_id
st.session_state.token = st.session_state.token

display_output(st.session_state.artist_id)
