import pandas as pd
import requests
import base64
import re


def AuthenticateSpotify():
    """Authenticate with Spotify API and get an access token."""

    # Spotify client credentials
    client_id = "47f30520c4e8485b925d9910d6d68d62"
    client_secret = "aa86334039704df3aec915153c9dd8c4"

    # Encode client_id and client_secret in Base64
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

    # Define the request headers and data
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "client_credentials",
    }

    try:
        # Make the POST request to get the access token
        response = requests.post("https://accounts.spotify.com/api/token",
                                 headers=headers, data=data)
    except requests.exceptions.RequestException as e:
        raise f"Error: {e}"

    access_token = response.json().get("access_token")
    return access_token


def convert_uris_to_ids(tracks: pd.DataFrame) -> pd.DataFrame:
    """

    Args:

    Returns:

    """
    # rename columns
    tracks = tracks.rename(columns={'track_uri': 'track_id',
                                    'artist_uris': 'artist_id',
                                    'album_uri' : 'album_id',
                                    'album_artist_uris' : 'album_artist_id'})
    # Convert Spotify URIs to IDs
    tracks['track_id'] = tracks['track_id'].str.replace('spotify:track:', '', regex=False)
    #tracks['artist_id'] = tracks['artist_id'].str.replace('spotify:artist:', '', regex=False)
    tracks['album_id'] = tracks['album_id'].str.replace('spotify:album:', '', regex=False)
    tracks['album_artist_id'] = tracks['album_artist_id'].str.replace('spotify:artist:', '', regex=False)
    return tracks


def set_index(tracks: pd.DataFrame) -> pd.DataFrame:
    """

    Args:

    Returns:

    """
    # Set the index to the track ID
    tracks = tracks.set_index('track_id')
    return tracks


def get_track_data(token, track_id):

    url = f'https://api.spotify.com/v1/tracks/{track_id}'

    headers = {
        "Authorization": f"Bearer {token}",
    }
    params = {
        "market": "ES",
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise f'Error:, {response.status_code, response.json()}'


def get_tracks_data(token, track_ids):
    ids = ','.join(track_ids)

    url = f'https://api.spotify.com/v1/tracks?ids={ids}'

    headers = {
        "Authorization": f"Bearer {token}",
    }
    params = {
        "market": "ES",
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise f'Error:, {response.status_code, response.json()}'