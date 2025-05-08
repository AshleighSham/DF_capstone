import pandas as pd
from utils.transform_utils import (
    get_track_data,
    get_tracks_data,
    check_in_list,
    genre_dict
)
from utils.api_utils import AuthenticateSpotify
from etl.extract.extract import extract_data


def transform_data(tracks: pd.DataFrame, state: str) -> pd.DataFrame:
    """
    Transforms the input DataFrame of tracks by performing a series of
    cleaning, formatting, and enrichment operations
    """
    # format dataframe column names
    tracks = format_column_names(tracks)

    # Remove user API data
    tracks = drop_columns(tracks)

    # Clean dataframe
    tracks = clean_tracks(tracks)

    # removie missing values
    tracks = remove_missing_values(tracks)

    if state == 'new':
        # update the popularities from API
        tracks.reset_index(drop=True, inplace=True)
        tracks = update_API_data(tracks, AuthenticateSpotify())

    elif state == 'old':
        # update the popularities from past csv
        filepath = "../../data/clean/transformed_data.csv"
        tracks = update_data(tracks, filepath)

    tracks = tracks.dropna(subset=['popularity'])

    # add columns for cleaner genre for the lols
    tracks = simplify_and_expand_artist_genres(tracks)

    return tracks


def format_column_names(tracks: pd.DataFrame) -> pd.DataFrame:
    """
    Format the columns names to consistent standards
    """

    # remove spaces and change to lower case
    tracks.columns = tracks.columns.str.lower().str.replace(' ', '_')

    # remove special characters
    tracks.columns = tracks.columns.str.replace('(', '').str.replace(')', '')

    # rename columns
    tracks = tracks.rename(columns={'track_uri': 'track_id',
                                    'artist_uris': 'artist_id',
                                    'album_uri': 'album_id',
                                    'album_artist_uris': 'album_artist_id',
                                    'album_release_date': 'album_year'})

    return tracks


def update_API_data(dataframe: pd.DataFrame, token) -> pd.DataFrame:
    raise "Oopsie"
    """
    Updates the 'popularity' column in the given DataFrame by fetching data
    from an external API using track IDs and ISRC codes.
    """

    updated_df = dataframe.copy()

    # process the DataFrame in batches to optimise API calls
    batch_size = 50

    for i in range(0, len(dataframe), batch_size):

        # select batch of track_id
        end_index = min(i + batch_size, len(dataframe))
        tracks_ids = dataframe[i:end_index]['track_id'].tolist()

        try:
            response = get_tracks_data(token, tracks_ids)

            # select popularity and a second id for comformation
            temp_isrc = [item.get('external_ids')['isrc'] for
                         item in response['tracks']]
            temp_pop = [item['popularity'] for item in response['tracks']]

            # Create a mapping of ISRC to popularity
            isrc_pop_map = dict(zip(temp_isrc, temp_pop))

            # Update the popularity column in df2 only if ISRC matches
            for idx in dataframe[i:end_index].index:
                try:
                    isrc_value = dataframe.loc[idx, 'isrc']
                    if isrc_value in isrc_pop_map:
                        updated_df.loc[idx, 'popularity'] = isrc_pop_map[
                                isrc_value
                            ]
                    else:
                        # Set as null if ISRC doesn't match
                        updated_df.loc[idx, 'popularity'] = pd.NA
                except Exception as row_error:

                    print(f"Error processing row {idx}: {row_error}")
                    # Set as null for problematic rows
                    updated_df.loc[idx, 'popularity'] = pd.NA
        except Exception as batch_error:
            # if a batch fails, move to row by row updation for that batch

            for j in range(i, end_index):
                try:
                    # Attempt to process each track IDs individually
                    track_id = dataframe.loc[j, 'track_id']
                    a = get_track_data(token, track_id)

                    if 'isrc' in a.get('external_ids'):
                        isrc_value = a.get('external_ids')['isrc']

                        if isrc_value == updated_df.loc[j, 'isrc']:
                            updated_df.loc[j, 'popularity'] = a['popularity']
                    else:
                        updated_df.loc[j, 'popularity'] = None
                        print(
                              "ISRC not found for track ID {j}".format(
                                j=j
                              )
                          )
                        print(
                              "IRSC: {irsc}".format(
                                  irsc=updated_df.loc[j, 'isrc']
                                  )
                              )
                except Exception as e:
                    # if the row updation fail print error and continue
                    print(
                          "Error processing track ID {j}, irsc {irsc}".format(
                            j=j, irsc=updated_df.loc[j, 'isrc']
                            )
                        )
                    print(
                        "Error: {e}".format(e=e)
                    )
                    continue

            # prin tth ebatch that failed and the IRSC ids in it
            print(f"Error processing batch {i}-{end_index}: {batch_error}")
            print(f"Track IDs in batch: {tracks_ids}")
            continue

    return updated_df


def convert_uris_to_ids(tracks: pd.DataFrame) -> pd.DataFrame:
    """

    Args:

    Returns:

    """
    # Convert Spotify URIs to IDs
    tracks['track_id'] = tracks['track_id'].str.replace('spotify:track:',
                                                        '', regex=False)

    tracks['album_id'] = tracks['album_id'].str.replace('spotify:album:', '',
                                                        regex=False)
    tracks['album_artist_id'] = tracks['album_artist_id'].str.replace(
                                        'spotify:artist:', '', regex=False
                                                                        )
    # format artist_id
    tracks['artist_id'] = tracks['artist_id'].str.replace('spotify:artist:',
                                                          '', regex=False)
    return tracks


def clean_tracks(tracks: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and transforms a DataFrame containing track information
    """

    # remove duplicates
    tracks = tracks.drop_duplicates()

    # standardise date format
    tracks['album_year'] = pd.to_datetime(tracks['album_year'],
                                          errors='coerce').dt.year

    # drop rows with invalid dates
    tracks = tracks.dropna(subset=['album_year'])

    # Convert the year to an integer
    tracks['album_year'] = tracks['album_year'].astype(int)

    tracks = convert_uris_to_ids(tracks)

    return tracks


def remove_missing_values(tracks: pd.DataFrame) -> pd.DataFrame:
    """
    Drop rows where specific columns have missing data
    """

    # Remove rows with missing values
    tracks = tracks.dropna(subset=['track_id', 'track_name',
                                   'artist_id', 'artist_names',
                                   'album_year', 'album_id',
                                   'album_name', 'album_artist_id',
                                   'album_artist_names', 'album_image_url'])

    return tracks


def drop_columns(tracks: pd.DataFrame) -> pd.DataFrame:
    """
    Remove columns
    """

    # Remove user API data
    tracks = tracks.drop(columns=['added_at', 'added_by'])

    # Remove unnecessary columns
    tracks = tracks.drop(columns=['track_preview_url', 'album_genres',
                                  'copyrights', 'label'])
    return tracks


def simplify_and_expand_artist_genres(tracks):
    """
    Map the artist_genres columns out into less and more broad genres,
    mapping made with the help of CoPilot
    """

    # import genres dictionary
    genres = genre_dict()

    # add genre count column for missing value count
    for key, value in genres.items():
        tracks[key] = tracks.apply(lambda x: check_in_list(x['artist_genres'],
                                                           value), axis=1)

    tracks['genre_count'] = tracks[genres.keys()].sum(axis=1)
    tracks = tracks.drop(columns=['artist_genres'])

    return tracks


def update_data(tracks, filepath):

    new_pop_data = extract_data(file=filepath)

    # Create a mapping of ISRC to popularity
    new_pop_data_map = dict(zip(new_pop_data['track_id'],
                                new_pop_data['popularity']))

    tracks.set_index('track_id')
    for idx in tracks:
        if idx in new_pop_data_map:
            tracks.loc[idx, 'popularity'] = new_pop_data_map[
                        idx
                    ]
        else:
            tracks.loc[idx, 'popularity'] = pd.NA

    return tracks
