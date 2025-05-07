import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots


def line_plot(results):

    fig = px.line(results,
                  x=results['album_year'],
                  y=results.columns[1:-1])
    fig.update_traces(marker=dict(size=10))
    st.plotly_chart(fig)


def line_plots(results):
    st.title(":green[Top Songs Trends Through The Years]")
    cols = results.columns
    fig = make_subplots(rows=4,
                        cols=2,
                        subplot_titles=cols[1:])

    col = 1
    for i in range(1, 5):
        for j in range(1, 3):
            fig.add_trace(go.Scatter(x=results['album_year'],
                                     y=results[cols[col]],
                                     name=f"{cols[col]}"),
                          row=i, col=j)
            fig.update_xaxes(title_text="Album Release Year", row=i, col=j)
            col += 1

    fig.update_layout(showlegend=False, height=1500, width=100)
    st.plotly_chart(fig)


def bar_graph(results, filter):
    st.title(":green[Genre Trends Through The Years]")

    filter.sort()
    color_discrete_map = {
            'Pop': 'green',
            'Rock': 'blue',
            'Hip-Hop': 'red',
            'Electronic': 'pink',
            'R&B/soul': 'purple',
            'Folk': 'black',
            'Country': 'aliceblue',
            'Ska': 'coral',
            'Disco/Dance': 'darkred',
            'Indie/Alternative': 'lime',
            'Retro/Vintage': 'maroon',
            'Novelty': 'mistyrose',
            'Easy Listening': 'orange'
            }

    fig = go.Figure()
    for genre in filter:
        fig.add_trace(go.Bar(
            x=results["album_year"],
            y=results[genre],
            name=genre
            )
        )

    fig.update_layout(barmode='stack', showlegend=True, height=1000,
                      yaxis={'title': "Number of Tracks"},
                      xaxis={'title': "Album Release Year",
                             'categoryorder': 'category ascending'})
    st.plotly_chart(fig)
