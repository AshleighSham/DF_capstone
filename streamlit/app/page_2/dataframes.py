import streamlit as st
import pandas as pd


def get_full_album_dataframe(albums_df, overall):
    albums_df = albums_df.merge(overall,
                                on=['album_id',
                                    'release_date',
                                    'album'],
                                how='left')

    albums_df.set_index('album_id', inplace=True)
    return albums_df


def display_albums_dataframe(albums_df):
    data = albums_df[['album',
                      'total_tracks',
                      'release_date',
                      'label',
                      'popularity']]

    # standardise date format
    data['release_date'] = pd.to_datetime(data['release_date'],
                                          errors='coerce').dt.year

    # Convert the year to an integer
    data['release_date'] = data['release_date'].astype(int)
    st.dataframe(
        data,
        hide_index=True,
        height=35*len(data)+38,
        column_config={
            'album': 'Album Name',
            'total_tracks': 'Total Tracks',
            'release_date': 'Release Year',
            'popularity': 'Popularity (0-100)',
            'label': 'Label'
            }
        )


def display_individual_album_dataframe(individual_albums, album_id):
    data = individual_albums[album_id][['disc_number',
                                        'track_number',
                                        'name',
                                        'duration_ms',
                                        'explicit',
                                        'popularity']]

    st.dataframe(
        data,
        hide_index=True,
        height=35*len(data)+38,
        column_config={
            'disc_number': 'Disc Number',
            'track_number': 'Track Number',
            'name': 'Track Name',
            'duration_ms': st.column_config.TimeColumn('Duration (min)',
                                                       format="mm:ss"),
            'explicit': 'Explicit',
            'popularity': 'Popularity (0- 100)'
            }
        )
