import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots


def line_plot(results):

    fig = px.line(results, x=results['album_year'], y=results.columns[1:-1])
    fig.update_traces(marker=dict(size=10))
    st.plotly_chart(fig)


def line_plots(results):
    st.title(":green[Top Songs Trends Through The Years]")
    cols = results.columns
    fig = make_subplots(rows=4, cols=2, subplot_titles=cols[1:])

    col = 1
    for i in range(1, 5):
        for j in range(1, 3):
            fig.add_trace(go.Scatter(x=results['album_year'], y=results[cols[col]], name=f"{cols[col]}"),
                          row=i, col=j)
            col += 1

    fig.update_layout(showlegend=False, height=1500, width=100)
    st.plotly_chart(fig)


def bar_graph(results):
    st.title(":green[Genre Trends Through The Years]")
    labels = {'album_year': 'Album Year'}
    fig = px.bar(results, x="album_year", y=results.columns[1:-1], labels=labels)
    fig.update_layout(showlegend=True, height=1000)
    st.plotly_chart(fig)
