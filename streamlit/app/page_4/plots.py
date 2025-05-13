import streamlit as st
import plotly.graph_objects as go


def bar_graph(results):
    # full_results = results.copy()
    st.title(":green[Genre Trends Through The Years]")

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

    selected_genres = st.pills(':green[Select Genres]',
                               selection_mode="multi",
                               options=[
                                    'Pop', 'Rock', 'Hip-Hop',
                                    'Electronic', 'R&B/soul',
                                    'Folk', 'Country', 'Ska',
                                    'Disco/Dance', 'Indie/Alternative',
                                    'Retro/Vintage', 'Novelty',
                                    'Easy Listening'
                                    ]
                               )

    filter = [item for item in color_discrete_map.keys()
              if item not in selected_genres]
    filter.sort()

    plot_spot = st.empty()

    selected_years = st.slider(
        ":green[Select a Range of Years]", 1950, 2024,
        value=[1950, 2024]
    )

    results.set_index("album_year", inplace=True)

    temp_results = results.loc[selected_years[0]:selected_years[1]]

    fig = go.Figure()
    for genre in filter:
        fig.add_trace(go.Bar(
            x=temp_results.index,
            y=temp_results[genre],
            name=genre,
            marker_color=color_discrete_map[genre]
            )
        )

    fig.update_layout(barmode='stack', showlegend=True, height=600,
                      yaxis={'title': "Number of Tracks"},
                      xaxis={'title': "Album Release Year",
                             'categoryorder': 'category ascending'})

    with plot_spot.container():
        st.plotly_chart(fig)
