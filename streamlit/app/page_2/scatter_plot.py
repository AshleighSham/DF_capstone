import pandas as pd
import plotly.express as px
import streamlit as st


def individual_album_scatter(individual_albums, album_name):
    data = individual_albums[['name',
                              'duration_ms',
                              'explicit',
                              'popularity']].copy()
    data['album'] = album_name
    data['duration_ms'] = pd.to_timedelta(data['duration_ms'], unit='ms')

    kinda_simple_scatter_plot(data)


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


def kinda_simple_scatter_plot(results):
    axis = st.multiselect("Select two track properties to inspect",
                          ["Popularity (0-100)",
                           "Duration (min)",
                           "Explicit"],
                          default=["Duration (min)", "Popularity (0-100)"])

    if len(axis) < 2:
        st.warning("Please select two properties to inspect.")
        return
    elif len(axis) > 2:
        st.warning("Please select at most two properties to inspect.")
        return
    else:
        labels1 = {"Explicit": "explicit",
                   "Popularity (0-100)": "popularity",
                   "Duration (min)": "duration_ms"}
        lables2 = {"explicit": "Explicit",
                   "popularity": "Popularity (0-100)",
                   "duration_ms": "Duration (min)"}

        st.subheader(f":green[Top Tracks {axis[0]} vs {axis[1]}]")

        fig = px.scatter(results, x=labels1[axis[0]], y=labels1[axis[1]],
                         color="album", hover_name="name",
                         labels=lables2)
        fig.update_traces(marker=dict(size=10))
        st.plotly_chart(fig)


def not_so_simple_scatter_plot(results):
    axis = st.multiselect("Select two track properties to inspect",
                          ["Popularity (0-100)",
                           "Duration (min)",
                           "Release Date",
                           "Explicit"],
                          default=["Duration (min)", "Popularity (0-100)"])

    if len(axis) < 2:
        st.warning("Please select two properties to inspect.")
        return
    elif len(axis) > 2:
        st.warning("Please select at most two properties to inspect.")
        return
    else:
        labels1 = {"Release Date": "release_date",
                   "Popularity (0-100)": "popularity",
                   "Duration (min)": "duration_ms",
                   "Explicit": "explicit"}
        lables2 = {"release_date": "Release Date",
                   "popularity": "Popularity (0-100)",
                   "duration_ms": "Duration (min)",
                   "explicit": "Explicit"}

        st.subheader(f":green[Top Tracks Across Albums {axis[0]} vs {axis[1]}]")

        fig = px.scatter(results, x=labels1[axis[0]], y=labels1[axis[1]],
                         color="album", hover_name="name",
                         labels=lables2)
        fig.update_traces(marker=dict(size=10))
        st.plotly_chart(fig)
