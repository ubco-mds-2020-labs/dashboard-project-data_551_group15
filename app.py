import altair as alt
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=['dbc.themes.BOOTSTRAP'])
server = app.server

app.layout = html.Div([
    html.H1("DATA551 Project APP")
])

# @app.callback(
#     Output(),
#     Input()
# )
# def update_output(input_value):
#     return input_value

if __name__ == '__main__':
    app.run_server(debug=True)