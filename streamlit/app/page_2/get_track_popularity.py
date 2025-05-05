import requests


def get_track_popularity(token, track_ids):
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
        return [response.json().get('tracks', [])[i]['popularity'] for i in
                range(len(response.json().get('tracks', [])))]
    else:
        raise f'Error:, {response.status_code, response.json()}'
