import pandas as pd
import re
import requests
from utils.api_utils import verify_request


def get_track_data(token, track_id):
    """

    Args:

    Returns:

    """
    url = f'https://api.spotify.com/v1/tracks/{track_id}'

    headers = {
        "Authorization": f"Bearer {token}",
    }
    params = {
        "market": "ES",
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        verify_request(response)
        return response.json()
    except Exception as e:
        raise RuntimeError(f"Error during Spotify authentication: {e}")


def get_tracks_data(token, track_ids):
    """

    Args:

    Returns:

    """
    ids = ','.join(track_ids)

    url = f'https://api.spotify.com/v1/tracks?ids={ids}'

    headers = {
        "Authorization": f"Bearer {token}",
    }
    params = {
        "market": "ES",
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        verify_request(response)
        return response.json()
    except Exception as e:
        raise RuntimeError(f"Error during Spotify authentication: {e}")


def set_index(tracks: pd.DataFrame) -> pd.DataFrame:
    """

    Args:

    Returns:

    """
    # Set the index to the track ID
    tracks = tracks.set_index('track_id')
    return tracks


def check_in_list(list, value):
    """

    Args:

    Returns:

    """
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
    """

    Args:

    Returns:

    """
    genres = {'pop': ['pop', 'boy band', 'viral trap', 'deep talent show',
                      'dansktop', 'girl group', 'chanson', 'talent show'],
              'rock': ['rock', 'post-grunge', 'beatlesque', 'british invasion',
                       'punk', 'new wave', 'british blues', 'funk metal',
                       'permanent wave', 'neo mellow', 'stomp and holler',
                       'metal', 'surf music', 'cosmic american'],
              'hip_hop': ['hip hop', 'rap', 'viral trap', 'bass', 'grime',
                          'britcore'],
              'electronic': ['edm', 'complextro', 'german techno',
                             'acid house', 'house', 'vapor soul',
                             'viral trap', 'bounce', 'remix product',
                             'tronica', 'trip hop', 'uk garage',
                             'ruta destroy', 'rave', 'trance', 'grime',
                             'techno', 'gabber', 'freestyle', 'electro',
                             'dnb', 'drum', 'beat'],
              'rnb_soul': ['r&b', 'soul', 'urban contemporary',
                           'rhythm and blues', 'doo-wop', 'motown'],
              'folk': ['folk', 'singer-songwriter', 'stomp and holler',
                       'calypso', 'soca', 'ukulele', 'cosmic american',
                       'banjo', 'acoustic'],
              'country': ['country', 'nashville', 'western'],
              'ska': ['ska', 'reggae'],
              'dance_disco': ['disco', 'hi-nrg', 'dance', 'funana', 'groove',
                              'funk'],
              'indie_alt': ['indie', 'new romantic', 'art rock',
                            'alternative', 'chamber psych', 'anti-folk',
                            'neo mellow', 'permanent wave', 'lilith', 'alt'],
              'retro_vintage': ['brill building pop', 'british invasion',
                                'merseybeat', 'beatlesque', 'freakbeat',
                                'rock-and-roll'],
              'novelty': ['a cappella', 'glee club', 'show tunes', 'novelty',
                          'pixie', 'comic', 'zolo', 'parody', 'kindermusik',
                          'karaoke', 'hollywood', 'cartoon', 'broadway',
                          'theme', 'wrestling'],
              'easy_listening': ['mellow gold', 'lounge', 'soft rock',
                                 'yacht rock', 'adult standards', 'solo wave',
                                 'easy listening', 'downtempo', 'poetry',
                                 'light music', 'library music'],
              'cultural': ['australian', 'british', 'queens', 'tropical',
                           'schlager', 'oktoberfest', 'musical advocacy',
                           'didgeridoo', 'yodeling', 'opm', 'native american',
                           'idol', 'hawaiian', 'enka', 'polka'],
              'jazz': ['jazz', 'swing', 'blues', 'instrumental worship',
                       'hammond organ', 'drum']}
    return genres
