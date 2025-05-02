import pandas as pd


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

