import streamlit as st
import plotly.express as px
from app.simple_scatter_plot import not_so_simple_scatter_plot, kinda_simple_scatter_plot
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

    st.dataframe(data, hide_index=True, height=35*len(data)+38,
                 column_config={'album': 'Album Name',
                                'total_tracks': 'Total Tracks',
                                'release_date': st.column_config.DateColumn('Release Date'),
                                'popularity': 'Popularity (0-100)',
                                'label': 'Label'})


def display_individual_album_dataframe(individual_albums, album_id):
    data = individual_albums[album_id][['disc_number',
                                        'track_number',
                                        'name',
                                        'duration_ms',
                                        'explicit',
                                        'popularity']]

    st.dataframe(data, hide_index=True, height=35*len(data)+38,
                 column_config={'disc_number': 'Disc Number',
                                'track_number': 'Track Number',
                                'name': 'Track Name',
                                'duration_ms': st.column_config.TimeColumn('Duration (min)', format="mm:ss"),
                                'explicit': st.column_config.TextColumn('Explicit'),
                                'popularity': 'Popularity (0- 100)'})


def all_album_scatter(individual_albums, album_name, albums_df):
    results = {'album_id': [], 'album': [], 'name': [],
               'duration_ms': [], 'explicit': [], 'popularity': [], 'release_date': []}
    results = pd.DataFrame(results)
    for album_id in individual_albums:
        data = individual_albums[album_id][['name',
                                            'duration_ms',
                                            'explicit',
                                            'popularity']].copy()
        data['album'] = album_name[album_id]
        data['duration_ms'] = pd.to_timedelta(data['duration_ms'], unit='ms')
        data['release_date'] = albums_df.loc[album_id, 'release_date']
        results = pd.concat([results, data])

    not_so_simple_scatter_plot(results)


def individual_album_scatter(individual_albums, album_name):
    data = individual_albums[['name',
                              'duration_ms',
                              'explicit',
                              'popularity']].copy()
    data['album'] = album_name
    data['duration_ms'] = pd.to_timedelta(data['duration_ms'], unit='ms')

    kinda_simple_scatter_plot(data)
