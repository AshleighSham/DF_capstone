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
    # standardise date format
    albums_df['release_date'] = pd.to_datetime(albums_df['release_date'],
                                               errors='coerce').dt.year
    albums_df['release_date'] = albums_df['release_date'].astype(int)
    data = albums_df[['album',
                      'total_tracks',
                      'release_date',
                      'label',
                      'popularity']]

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
