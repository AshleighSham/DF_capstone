import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots


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
