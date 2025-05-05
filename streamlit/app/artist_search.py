import streamlit as st
from app.spotify_auth import AuthenticateSpotify
from app.utilis import verify_request
import requests


@st.cache_data
def get_artist_id(artist_name):
    token = AuthenticateSpotify()

    headers = {
        "Authorization": f"Bearer {token}",
    }
    params = {
        "market": "ES",
    }
    url = f"https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=1"

    try:
        response_main = requests.get(url, headers=headers, params=params)
        verify_request(response_main)
        if response_main.status_code == 200:
            artist_id = response_main.json().get('artists').get('items')[0].get('id')

    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")

    return token, artist_id
