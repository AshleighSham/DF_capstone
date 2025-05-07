import streamlit as st
import plotly.graph_objects as go


def bar_graph(results, filter):
    st.title(":green[Genre Trends Through The Years]")

    filter.sort()
    color_discrete_map = {
            'Pop': '#ea5545',
            'Rock': '#f46a9b',
            'Hip-Hop': '#ef9b20',
            'Electronic': '#87bc45',
            'R&B/soul': '#ede15b',
            'Folk': '#b3d4ff',
            'Country': '#edbf33',
            'Ska': '#50e991',
            'Disco/Dance': '#27aeef',
            'Indie/Alternative': '#b33dc6',
            'Retro/Vintage': "#4421af",
            'Novelty': '#bdcf32',
            'Easy Listening': '#9b19f5'
            }

    fig = go.Figure()
    for genre in filter:
        fig.add_trace(go.Bar(
            x=results["album_year"],
            y=results[genre],
            name=genre,
            marker_color=color_discrete_map[genre]
            )
        )

    fig.update_layout(barmode='stack', showlegend=True, height=1000,
                      yaxis={'title': "Number of Tracks"},
                      xaxis={'title': "Album Release Year",
                             'categoryorder': 'category ascending'})
    st.plotly_chart(fig)
