import pandas as pd


def clean_tracks(tracks: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the top 10000 tracks DataFrame by removing duplicates 
    and standardising the format of the release date column.

    Args:
        tracks (pd.DataFrame): DataFrame containing top 10000 tracks data.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    # Remove duplicates
    tracks = tracks.drop_duplicates()

    # Standardise date format
    tracks['release_date'] = pd.to_datetime(tracks['release_date'], errors='coerce')
    tracks['release_date'] = tracks['release_date'].dt.strftime('%d/%m/%Y')

    # Drop rows with invalid dates
    tracks = tracks.dropna(subset=['release_date'])

    return tracks