import pandas as pd
import plotly.express as px
import streamlit as st


def format_sec(x):
    if isinstance(x, pd.Timedelta):
        total_seconds = int(x.total_seconds())
    else:
        total_seconds = int(x / 1000)
    return total_seconds


def format_min_sec(x):
    total_seconds = format_sec(x)

    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes}:{seconds:02}"


def individual_album_scatter(individual_albums, album_name):
    data = individual_albums[['name',
                              'duration_ms',
                              'explicit',
                              'popularity']].copy()
    data['album'] = album_name

    # Add float duration in minutes for hover, and timedelta for plotting
    data['duration_min'] = data['duration_ms'].apply(
        lambda x: format_min_sec(x))
    data['duration_sec'] = data['duration_ms'].apply(
        lambda x: format_sec(x))

    individual_scatter_plot(data)


def all_album_scatter(individual_albums, album_name, albums_df):
    results = {'album_id': [],
               'album': [],
               'name': [],
               'duration_ms': [],
               'duration_min': [],
               'explicit': [],
               'popularity': [],
               'release_date': []}

    results = pd.DataFrame(results)
    for album_id in individual_albums:
        data = individual_albums[album_id][['name',
                                            'duration_ms',
                                            'explicit',
                                            'popularity']].copy()
        data['album'] = album_name[album_id]
        data['duration_sec'] = data['duration_ms'].apply(
            lambda x: format_sec(x))
        data['duration_min'] = data['duration_ms'].apply(
            lambda x: format_min_sec(x))

        data['release_date'] = albums_df.loc[album_id, 'release_date']
        results = pd.concat([results, data])

    all_scatter_plot(results)


def individual_scatter_plot(results):
    axis = st.multiselect("Select two track properties to inspect",
                          ["Popularity (0-100)",
                           "Duration (sec)"],
                          default=["Duration (sec)", "Popularity (0-100)"])

    if len(axis) < 2:
        st.warning("Please select two properties to inspect.")
        return
    elif len(axis) > 2:
        st.warning("Please select at most two properties to inspect.")
        return
    else:
        labels1 = {"Album": "album",
                   "Explicit": "explicit",
                   "Popularity (0-100)": "popularity",
                   "Duration (sec)": "duration_sec",
                   "Duration (min)": "duration_min"}
        lables2 = {"album": "Album",
                   "explicit": "Explicit",
                   "popularity": "Popularity (0-100)",
                   "duration_sec": "Duration (sec)",
                   "duration_min": "Duration (min)"}

        st.subheader(f":green[Top Tracks {axis[0]} vs {axis[1]}]")

        fig = px.scatter(results, x=labels1[axis[0]], y=labels1[axis[1]],
                         color="album", hover_name="name",
                         hover_data=["duration_min", "popularity"],
                         labels=lables2)

        fig.update_traces(marker=dict(size=10))
        st.plotly_chart(fig)


def all_scatter_plot(results):
    axis = st.multiselect("Select two track properties to inspect",
                          ["Popularity (0-100)",
                           "Duration (sec)",
                           "Release Date"],
                          default=["Duration (sec)", "Popularity (0-100)"])

    if len(axis) < 2:
        st.warning("Please select two properties to inspect.")
        return
    elif len(axis) > 2:
        st.warning("Please select at most two properties to inspect.")
        return
    else:
        labels1 = {"Album": "album",
                   "Release Date": "release_date",
                   "Popularity (0-100)": "popularity",
                   "Duration (sec)": "duration_sec",
                   "Explicit": "explicit",
                   "Duration (min)": "duration_min"}
        lables2 = {"album": "Album",
                   "release_date": "Release Date",
                   "popularity": "Popularity (0-100)",
                   "duration_sec": "Duration (sec)",
                   "explicit": "Explicit",
                   "duration_min": "Duration (min)"}

        st.subheader(
            f":green[Top Tracks Across Albums {axis[0]} vs {axis[1]}]"
        )

        fig = px.scatter(results, x=labels1[axis[0]], y=labels1[axis[1]],
                         color="album", hover_name="name",
                         hover_data=["duration_min", "popularity"],
                         labels=lables2)

        fig.update_traces(marker=dict(size=10))
        st.plotly_chart(fig)
