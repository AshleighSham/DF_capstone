import plotly.express as px
import streamlit as st


def heat_map(data):
    opt = ['0', '1-10', '11-20', '21-30',
           '31-40', '41-50', '51-60',
           '61-70', '71-80', '81-90', '91-100']

    plot_spot = st.empty()

    selected_bins = st.pills(':green[Select Bins]',
                             selection_mode="multi",
                             options=[
                                '0', '1-10', '11-20', '21-30',
                                '31-40', '41-50', '51-60',
                                '61-70', '71-80', '81-90', '91-100'
                                ]
                             )

    filter = [item for item in opt
              if item not in selected_bins]
    filter.sort()
    data.set_index(['year_group'], inplace=True)
    data = data.reindex(columns=filter)
    fig = px.imshow(data, x=data.columns, y=data.index,
                    color_continuous_scale='aggrnyl')
    fig.update_xaxes(title_text="Popularity")
    fig.update_yaxes(title_text="Release Year")
    fig.update_layout(width=500, height=800)

    with plot_spot.container():
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
