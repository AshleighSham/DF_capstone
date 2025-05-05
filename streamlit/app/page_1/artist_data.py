import requests
import streamlit as st


@st.cache_data
def get_artists_data(token, artist_id):

    url = f'https://api.spotify.com/v1/artists/{artist_id}'

    headers = {
        "Authorization": f"Bearer {token}",
    }
    params = {
        "market": "ES",
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return [response.json().get('name'),
                response.json().get('popularity'),
                response.json().get('images')[0].get('url'),
                response.json().get('followers').get('total')]
    else:
        raise f'Error:, {response.status_code, response.json()}'
