import streamlit as st
from app.artist_search import get_artist_id


title_alignment = """
<style>
#the-title {
  text-align: center;
  font-size: 100px
}
</style>
"""


def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(
        page_title="Spotify App",
        page_icon="🎵",
        layout="wide",
        initial_sidebar_state="auto"
    )
    st.markdown(title_alignment, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        st.sidebar.title(":green[Spotify Data Explorer]")

        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Spotify_icon.svg/512px-Spotify_icon.svg.png?20220821125323')
    st.title(":green[Spotify Data Explorer]")
    st.subheader(":green[by Ashleigh Shambrook]")

    with st.form(key="artist_form"):
        st.write("Choose your fighter!")
        artist_name = st.text_input("Type an artist",
                                    'Mitski',
                                    key="artist_name")
        st.form_submit_button("Submit")

    token, artist_id = get_artist_id(artist_name)

    st.session_state.artist_id = artist_id
    st.session_state.token = token


if __name__ == "__main__":
    main()
