import streamlit as st
from app.page_4_output import display_output

st.set_page_config(page_title="Genre Popularity from 1950 - 2024",
                   page_icon="🎵",
                   layout="wide")

bl1 = (
    "https://www.kaggle.com/datasets/joebeachcapital/"
    "top-10000-spotify-songs-1960-now"
    )

st.sidebar.title(":green[Genre Popularity from 1950 - 2024]")

with st.sidebar:
    st.write(("As we all know Spotify has taken Genre "
              "categories way too far, for reference "
              "the dataset CSV has over 800 unqiue "
              "genres. Overkill imo. For the purpose of "
              "this visualtion the Genres where mapped "
              "back to their purest form with the "
              " MUCH appreciated help of Github Copolit."))
    st.write(("The dataset provided the relevent genres of the "
              "of the artist who released each track. Even "
              "though this is not a completely accurate "
              "representation of the tracks genre, it "
              "is suitable enough for the purpose of "
              "this project."))
    st.link_button(":green[Go to Kaggle Dataset]", bl1)

st.header(":green[Spotify Data Explorer]")
st.write("---")

st.session_state.artist_name = st.session_state.artist_name
st.session_state.artist_id = st.session_state.artist_id
st.session_state.token = st.session_state.token

display_output(st.session_state.artist_id)
