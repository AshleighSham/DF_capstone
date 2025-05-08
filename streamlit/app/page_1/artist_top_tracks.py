import requests
from app.page_1.clean_top_track_data import top_track_dataframe
import streamlit as st


@st.cache_data
def get_artists_top_tracks(token, artist_id):

    url = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks'

    headers = {
        "Authorization": f"Bearer {token}",
    }
    params = {
        "market": "ES",
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return top_track_dataframe(response)
    else:
        raise f'Error:, {response.status_code, response.json()}'
