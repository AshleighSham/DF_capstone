import streamlit as st
import plotly.express as px


def scatter_plot(results):
    axis = st.multiselect("Select two track properties to inspect",
                          ["Popularity (0-100)",
                           "Duration (min)",
                           "Release Date"],
                          default=["Release Date", "Popularity (0-100)"])

    if len(axis) < 2:
        st.warning("Please select two properties to inspect.")
        return
    elif len(axis) > 2:
        st.warning("Please select at most two properties to inspect.")
        return
    else:
        labels1 = {"Release Date": "release_date",
                   "Popularity (0-100)": "popularity",
                   "Duration (min)": "duration_ms"}
        lables2 = {"release_date": "Release Date",
                   "popularity": "Popularity (0-100)",
                   "duration_ms": "Duration (min)",
                   "album": "Album"}

        st.subheader(f":green[Top Tracks {axis[0]} vs {axis[1]}]")

        fig = px.scatter(results, x=labels1[axis[0]], y=labels1[axis[1]],
                         color="album", hover_name="name",
                         labels=lables2)
        fig.update_traces(marker=dict(size=10))
        st.plotly_chart(fig)
