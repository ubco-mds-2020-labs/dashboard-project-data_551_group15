import altair as alt
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=['dbc.themes.BOOTSTRAP'])
server = app.server

app.layout = dbc.Container([
    html.H1("DATA551 Project APP"),
    dbc.Row([
        dbc.Col([
            html.Label([
                'Select Province',
                dcc.Dropdown(
                    id="province",
                    options=[{"label": "temp", "value": "temp"}],
                    value="temp"
                )
            ]),
            html.Label([
                "Select Year",
                dcc.Slider(id="year", min=1990, max=2010, value=1990, marks={1990: '1990', 2010: '2010'})
            ])
        ]),
        dbc.Col([
            dcc.Textarea(id="output")
        ])
    ])
])


@app.callback(
    Output("output", "value"),
    Input("year", "value")
)
def update_output(input_value):
    return str(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
