import altair as alt
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from src import Visualizations as Vis
from src import wrangling as wr

# Prepare the inputs:
minyear = int(min(wr.years))
maxyear = int(max(wr.years))

drop_options = []
for i in wr.provinces:
    temp = {"label": i, "value": i}
    drop_options.append(temp)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div([
    dbc.Row(
        dbc.Col(
            html.H1("DATA551 Project APP"),
            width={"offset": 1}
        )
    ),
    dbc.Row([
        dbc.Col([
            html.Label([
                html.H5('Select Province:'),
                dcc.Dropdown(
                    id="province",
                    options=drop_options,
                    value="British Columbia",
                    style={"width": "300px"}
                )
            ])

        ], width={"offset": 2, "width": 5}),

        dbc.Col([
            html.Label([
                html.H5('Select Year:'),
                dcc.Slider(
                    id="year",
                    min=minyear,
                    max=maxyear,
                    value=minyear,
                    marks={minyear: str(minyear), maxyear: str(maxyear)},
                    tooltip={"placement": "bottomLeft"}
                )
            ], style={"width": "300px"})
        ], width={"offset": 2, "width": 5})
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.Iframe(
                        id="total",
                        style={'border-width': '0', 'width': '400px', 'height': '250px'}
                    ),
                ], width=6),
                dbc.Col([
                    html.Iframe(
                        id="hist",
                        style={'border-width': '0', 'width': '400px', 'height': '250px'}
                    ),
                ], width=6)
            ]),
            dbc.Row([
                dbc.Col([
                    html.Iframe(
                        id="prov",
                        style={'border-width': '0', 'width': '800px', 'height': '500px'}
                    )
                ])
            ]),
        ], width={"offset": 1, "width": 5}),
        dbc.Col([
            html.Iframe(
                id="indus",
                style={'border-width': '0', 'width': '800px', 'height': '800px'}
            )
        ], width={"width": 6})
    ])
])


@app.callback(
    Output("total", "srcDoc"),
    Input("year", "value"),
    Input("province", "value")
)
def plt_total_gdp(year, province):
    return Vis.plt_total_gdp(year, province)


@app.callback(
    Output("hist", "srcDoc"),
    Input("year", "value"),
    Input("province", "value")
)
def plt_historical_gdp(year, province):
    return Vis.plt_historical_gdp(year, province)


@app.callback(
    Output("prov", "srcDoc"),
    Input("year", "value"),
)
def plt_province_gdp(year):
    return Vis.plt_province_gdp(year)


@app.callback(
    Output("indus", "srcDoc"),
    Input("year", "value"),
    Input("province", "value")
)
def plt(year, province):
    return Vis.plt_indus_contri(year, province)


if __name__ == '__main__':
    app.run_server(debug=True)
