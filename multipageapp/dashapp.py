import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[
                    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
                    ],
                use_pages=True)



app.layout = html.Div(
    [
        html.Div("Data visualization about education in the UK 1833-2019.", style={'fontSize':50, 'textAlign':'center'}),
        html.Div([
            dcc.Link(page['name']+"  |  ", href=page['path'])
            for page in dash.page_registry.values()
        ]),
        html.Hr(),
        dash.page_container
    ]
)


if __name__ == "__main__":
    app.run(debug=True)