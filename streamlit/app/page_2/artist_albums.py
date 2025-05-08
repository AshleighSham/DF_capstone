import requests
from app.page_2.clean_top_album_data import top_album_dataframe
import streamlit as st


@st.cache_data
def get_artist_albums(token, album_ids):
    ids = ','.join(album_ids)

    url = f'https://api.spotify.com/v1/albums?ids={ids}'

    headers = {
        "Authorization": f"Bearer {token}",
    }
    params = {
        "market": "ES",
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return top_album_dataframe(response.json(), token)
    else:
        raise f'Error:, {response.status_code, response.json()}'
