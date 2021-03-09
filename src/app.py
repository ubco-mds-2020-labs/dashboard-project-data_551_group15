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

        ], width={"offset": 1, "width": 5}),

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
        ], width={"offset": 1, "width": 5})
    ]),
    dbc.Row([
        dbc.Col([
            html.Iframe(
                id="plot",
                style={'border-width': '0', 'width': '1000px', 'height': '500px'}
            )
        ], width={"offset": 1, "width": 10})
    ])



])


@app.callback(
    Output("plot", "srcDoc"),
    Input("year", "value"),
    Input("province", "value")
)
def plt_total_gdp(year, province):
    return Vis.plt_total_gdp(year, province)
# def update_output(input_value):
#     return str(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
