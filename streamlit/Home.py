import streamlit as st
from app.home_page.artist_search import get_artist_id
from app.page_1.artist_data import get_artists_data
import time


def stream_data(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.05)


title_alignment = """
<style>
#the-title {
  text-align: center;
  font-size: 100px
}
</style>
"""

imag = (
    "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/"
    "Spotify_icon.svg/512px-Spotify_icon.svg.png?20220821125323"
)
b_link = "https://developer.spotify.com/documentation/web-api/reference/search"


def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(
        page_title="Spotify App",
        page_icon="🎵",
        layout="wide",
        initial_sidebar_state="auto"
    )
    st.markdown(title_alignment, unsafe_allow_html=True)

    st.sidebar.title(":green[Spotify Data Explorer]")
    with st.sidebar:
        st.link_button(":green[Go to Spotify's Search API]",
                       b_link)

    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        st.image(imag)
    st.title(":green[Spotify Data Explorer]")
    st.subheader(":green[by Ashleigh Shambrook]")

    with st.form(key="artist_form"):
        st.write("Choose your fighter! :muscle:")
        artist_name = st.text_input("Type an artist",
                                    'Mitski',
                                    key="artist_name")
        if st.form_submit_button("Submit"):
            token, artist_id = get_artist_id(artist_name)

            artist_name = get_artists_data(token, artist_id)[0]
            st.session_state.artist_id = artist_id
            st.session_state.token = token

            st.write(stream_data(("...collecting data for suggested artist "
                                  f"**:green[{artist_name}]**, if this is not "
                                  "the Artist you were looking for please "
                                  "double check your spelling...")))


if __name__ == "__main__":
    main()
