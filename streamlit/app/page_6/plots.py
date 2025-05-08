import plotly.express as px
import streamlit as st


def heat_map(data):
    data.set_index(['year_group'], inplace=True)

    fig = px.imshow(data, x=data.columns, y=data.index,
                    color_continuous_scale='aggrnyl')
    fig.update_xaxes(title_text="Popularity")
    fig.update_yaxes(title_text="Release Year")
    fig.update_layout(width=500, height=1000)

    st.plotly_chart(fig)


# ['aggrnyl', 'agsunset', 'algae', 'amp',
#  'armyrose', 'balance', 'blackbody', 'bluered',
#  'blues', 'blugrn', 'bluyl', 'brbg', 'brwnyl',
#  'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'curl',
#  'darkmint', 'deep', 'delta', 'dense', 'earth', 'edge',
#  'electric', 'emrld', 'fall', 'geyser', 'gnbu', 'gray',
#  'greens', 'greys', 'haline', 'hot', 'hsv', 'ice',
#  'icefire', 'inferno', 'jet', 'magenta', 'magma',
#  'matter', 'mint', 'mrybm', 'mygbm', 'oranges',
#  'orrd', 'oryel', 'oxy', 'peach', 'phase', 'picnic',
#  'pinkyl', 'piyg', 'plasma', 'plotly3', 'portland',
#  'prgn', 'pubu', 'pubugn', 'puor', 'purd', 'purp',
#  'purples', 'purpor', 'rainbow', 'rdbu', 'rdgy',
#  'rdpu', 'rdylbu', 'rdylgn', 'redor', 'reds',
#  'solar', 'spectral', 'speed', 'sunset', 'sunsetdark',
#  'teal', 'tealgrn', 'tealrose', 'tempo', 'temps', 'thermal',
#  'tropic', 'turbid', 'turbo', 'twilight', 'viridis', 'ylgn',
#  'ylgnbu', 'ylorbr', 'ylorrd']