import pandas as pd
from utils import convert_uris_to_ids


def format_column_names(tracks: pd.DataFrame) -> pd.DataFrame:
    """

    Args:

    Returns:

    """
    # remove spaces and change to lower case
    tracks.columns = tracks.columns.str.lower().str.replace(' ', '_')
    # remove special characters
    tracks.columns = tracks.columns.str.replace('(', '').str.replace(')', '')
    return tracks


def transform_data(tracks: pd.DataFrame) -> pd.DataFrame:
    """

    Args:

    Returns:

    """
    # Clean the tracks DataFrame

    # format dataframe column names
    tracks = format_column_names(tracks)

    # replaces URIs to IDs
    tracks = convert_uris_to_ids(tracks)

    # Remove user API data
    tracks = drop_columns(tracks)

    # Clean dataframe
    tracks = clean_tracks(tracks)

    # removie missing values
    tracks = remove_missing_values(tracks)

    # Set the index to the track ID
    tracks = tracks.set_index('track_id')

    return tracks


def clean_tracks(tracks: pd.DataFrame) -> pd.DataFrame:
    """

    Args:

    Returns:

    """
    # Remove duplicates
    tracks = tracks.drop_duplicates()

    # Standardise date format
    tracks['album_release_date'] = pd.to_datetime(tracks['album_release_date'], errors='coerce')
    tracks['album_release_date'] = tracks['album_release_date'].dt.strftime('%d/%m/%Y')

    # Drop rows with invalid dates
    tracks = tracks.dropna(subset=['album_release_date'])

    return tracks


def remove_missing_values(tracks: pd.DataFrame) -> pd.DataFrame:
    """

    Args:

    Returns:

    """
    # Remove rows with missing values
    tracks = tracks.dropna(subset=['track_id', 'track_name',
                                   'artist_id', 'artist_names',
                                   'album_release_date', 'album_id',
                                   'album_name', 'album_artist_id',
                                   'album_artist_names', 'album_image_url'
                                   'label'])
    return tracks


def drop_columns(tracks: pd.DataFrame) -> pd.DataFrame:
    """

    Args:

    Returns:

    """
    # Remove user API data
    tracks = tracks.drop(columns=['added_at', 'added_by'])
    # Remove unnecessary columns
    tracks = tracks.drop(columns=['track_preview_url', 'album_genres', 'copyrights'])
    return tracks


def format_artist_id(tracks: pd.DataFrame) -> pd.DataFrame:
    """

    Args:

    Returns:

    """
    # Convert artist_id to a list of strings fro API data calls
    tracks['artist_id'] = tracks['artist_id'].str.replace('spotify:artist:', '', regex=False)
    tracks['artist_id'] = tracks['artist_id'].str.replace(' ', '', regex=False)
    return tracks
