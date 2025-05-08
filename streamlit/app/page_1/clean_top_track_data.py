import pandas as pd


def top_track_dataframe(response):
    df = pd.DataFrame(response.json().get('tracks', []))
    df.drop(columns=['uri', 'preview_url', 'external_urls', 'is_local',
                     'external_ids', 'album', 'artists', 'href',
                     'is_playable', 'type'], inplace=True, errors='ignore')

    df['album'] = [
        response.json().get('tracks', [])[i]['album']['name']
        for i in range(len(df))
    ]

    df['release_date'] = [
        response.json().get('tracks', [])[i]['album']['release_date']
        for i in range(len(df))
    ]

    df['album_id'] = [
        response.json().get('tracks', [])[i]['album']['id']
        for i in range(len(df))
    ]

    df['album_image'] = [
        response.json().get('tracks', [])[i]['album']['images'][0]['url']
        for i in range(len(df))
    ]

    return df
