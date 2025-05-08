import pandas as pd
from app.page_2.get_track_popularity import get_track_popularity


def top_album_dataframe(response, token):
    df = pd.DataFrame(response.get('albums', []))
    df.drop(columns=['is_playable', 'external_urls', 'external_ids',
                     'copyrights', 'album_type', 'images', 'genres',
                     'href', 'release_date_precision', 'uri',
                     'artists', 'type'], inplace=True, errors='ignore')

    individal_albums = {}
    for id, i in zip(df['id'], range(len(df))):
        album_id = df['id'][i]
        id = pd.DataFrame(response.get('albums', [])[i]['tracks']['items'])
        id.drop(columns=['is_playable', 'external_urls', 'external_ids',
                         'uri', 'href', 'artists', 'preview_url', 'track',
                         'is_local', 'type'], inplace=True, errors='ignore')
        track_ids = id['id'].tolist()
        id['popularity'] = get_track_popularity(token, track_ids)
        individal_albums[album_id] = id

    df.drop(columns=['tracks'], inplace=True, errors='ignore')
    df.rename(columns={'id': 'album_id', 'name': 'album'}, inplace=True)
    return df, individal_albums
