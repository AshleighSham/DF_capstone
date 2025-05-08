import streamlit as st
import plotly.express as px
import pandas as pd


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


def scatter_plot(results):
    axis = st.multiselect("Select two track properties to inspect",
                          ["Popularity (0-100)",
                           "Duration (sec)",
                           "Release Date"],
                          default=["Release Date", "Popularity (0-100)"])

    if len(axis) < 2:
        st.warning("Please select two properties to inspect.")
        return
    elif len(axis) > 2:
        st.warning("Please select at most two properties to inspect.")
        return
    else:
        # Add float duration in minutes for hover, and timedelta for plotting
        results['duration_min'] = results['duration_ms'].apply(
            lambda x: format_min_sec(x))
        results['duration_sec'] = results['duration_ms'].apply(
            lambda x: format_sec(x))

        labels1 = {"Release Date": "release_date",
                   "Popularity (0-100)": "popularity",
                   "Duration (sec)": "duration_sec",
                   "Duration (min)": "duration_min"}
        lables2 = {"release_date": "Release Date",
                   "popularity": "Popularity (0-100)",
                   "duration_sec": "Duration (sec)",
                   "duration_min": "Duration (min)",
                   "album": "Album"}

        st.subheader(f":green[Top Tracks {axis[0]} vs {axis[1]}]")

        fig = px.scatter(results, x=labels1[axis[0]], y=labels1[axis[1]],
                         color="album", hover_name="name",
                         hover_data=["duration_min"],
                         labels=lables2)
        fig.update_traces(marker=dict(size=10))
        st.plotly_chart(fig)
