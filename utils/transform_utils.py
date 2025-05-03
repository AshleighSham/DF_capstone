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


def check_in_list(list, value):
    try:
        if isinstance(list, str):
            list = list.split(',')
            for j in list:
                for i in value:
                    if re.search(i, j):
                        return True
            return False
        else:
            return False
    except Exception as e:
        print(list, f'{e}')


def genre_dict():
    genres = {'pop': ['pop', 'boy band', 'viral trap', 'deep talent show', 'dansktop', 'girl group', 'chanson', 'talent show'],
          'rock': ['rock', 'post-grunge', 'beatlesque', 'british invasion', 'punk',
                   'new wave', 'british blues', 'funk metal', 'permanent wave', 'neo mellow',
                   'stomp and holler', 'metal', 'surf music', 'cosmic american'],
          'hip_hop': ['hip hop', 'rap', 'viral trap', 'bass', 'grime', 'britcore'],
          'electronic': ['edm', 'complextro', 'german techno', 'acid house', 'house',
                         'vapor soul', 'viral trap', 'bounce', 'remix product', 'tronica', 'trip hop',
                         'uk garage', 'ruta destroy', 'rave', 'trance',
                         'grime', 'techno', 'gabber', 'freestyle', 'electro', 'dnb', 'drum', 'beat'],
          'rnb_soul': ['r&b', 'soul', 'urban contemporary', 'rhythm and blues', 'doo-wop', 'motown'],
          'folk': ['folk', 'singer-songwriter', 'stomp and holler', 'calypso', 'soca', 'ukulele',
                   'cosmic american', 'banjo', 'acoustic'],
          'country': ['country', 'nashville', 'western'],
          'ska': ['ska', 'reggae'],
          'dance_disco': ['disco', 'hi-nrg', 'dance', 'funana', 'groove', 'funk'],
          'indie_alt': ['indie', 'new romantic', 'art rock', 'alternative', 'chamber psych',
                        'anti-folk', 'neo mellow', 'permanent wave', 'lilith', 'alt'],
          'retro_vintage': ['brill building pop', 'british invasion', 'merseybeat',
                            'beatlesque', 'freakbeat', 'rock-and-roll'],
          'novelty': ['a cappella', 'glee club', 'show tunes', 'novelty', 'pixie', 'comic', 'zolo',
                      'parody', 'kindermusik', 'karaoke', 'hollywood', 'cartoon', 'broadway', 'theme', 'wrestling'],
          'easy_listening': ['mellow gold', 'lounge', 'soft rock', 'yacht rock',
                             'adult standards', 'solo wave', 'easy listening', 'downtempo', 'poetry',
                             'light music', 'library music'],
          'cultural': ['australian', 'british', 'queens', 'tropical', 'schlager', 'oktoberfest',
                       'musical advocacy', 'didgeridoo', 'yodeling', 'opm', 'native american', 'idol',
                       'hawaiian', 'enka', 'polka'],
          'jazz': ['jazz', 'swing', 'blues', 'instrumental worship', 'hammond organ', 'drum']}
    return genres