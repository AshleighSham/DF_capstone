import pandas as pd
from utils.transform_utils import convert_uris_to_ids, AuthenticateSpotify, get_track_data, get_tracks_data


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

    # update the popularities
    tracks.reset_index(drop=True, inplace=True)
    tracks = update_data(tracks, AuthenticateSpotify())
    tracks = tracks.dropna(subset=['popularity'])
    # Set the index to the track ID
    # tracks = tracks.set_index('track_id')

    return tracks


def update_data(dataframe: pd.DataFrame, token) -> pd.DataFrame:
    
    updated_df = dataframe.copy()
    batch_size = 50  # Adjust batch size if needed

    for i in range(0, len(dataframe), batch_size):
        end_index = min(i + batch_size, len(dataframe))
        tracks_ids = dataframe[i:end_index]['track_id'].tolist()

        try:
            response = get_tracks_data(token, tracks_ids)
            temp_isrc = [item.get('external_ids')['isrc'] for item in response['tracks']]
            temp_pop = [item['popularity'] for item in response['tracks']]
            # Create a mapping of ISRC to popularity
            isrc_popularity_map = dict(zip(temp_isrc, temp_pop))

            # Update the popularity column in df2 only if ISRC matches
            for idx in dataframe[i:end_index].index:
                try:
                    isrc_value = dataframe.loc[idx, 'isrc']
                    if isrc_value in isrc_popularity_map:
                        updated_df.loc[idx, 'popularity'] = isrc_popularity_map[isrc_value]
                    else:
                        updated_df.loc[idx, 'popularity'] = pd.NA  # Set as null if ISRC doesn't match
                except Exception as row_error:
                    print(f"Error processing row {idx}: {row_error}")
                    updated_df.loc[idx, 'popularity'] = pd.NA  # Set as null for problematic rows
        except Exception as batch_error:
            for j in range(i, end_index):
                try:
                    # Attempt to process each track ID individually
                    track_id = dataframe.loc[j, 'track_id']
                    a = get_track_data(token, track_id)
                    if 'isrc' in a.get('external_ids'):
                        isrc_value = a.get('external_ids')['isrc']
                        if isrc_value == updated_df.loc[j, 'isrc']:
                            updated_df.loc[j, 'popularity'] = a['popularity']
                    else:
                        updated_df.loc[j, 'popularity'] = None
                        print(f"ISRC not found for track ID {j}, irsc {updated_df.loc[j, 'isrc']}")
                except Exception as e:
                    print(f"Error processing track ID {j}, irsc {updated_df.loc[j, 'isrc']}: {e}")
                    continue
                    # Optionally, handle the error or log it
            print(f"Error processing batch {i}-{end_index}: {batch_error}")
            print(f"Track IDs in batch: {tracks_ids}")
            # Optionally, continue to the next batch or break
            continue
    return updated_df


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
                                   'album_artist_names', 'album_image_url'])
    return tracks


def drop_columns(tracks: pd.DataFrame) -> pd.DataFrame:
    """

    Args:

    Returns:

    """
    # Remove user API data
    tracks = tracks.drop(columns=['added_at', 'added_by'])
    # Remove unnecessary columns
    tracks = tracks.drop(columns=['track_preview_url', 'album_genres', 'copyrights', 'label'])
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
