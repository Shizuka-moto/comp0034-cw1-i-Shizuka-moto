import dash
from dash import html
import dash_bootstrap_components as dbc
"""
Program name: dashapp.py
Student number: 20054718

Integrate all the page together and set how navigare bar looks like and include.
All the page files are in folder named "page"
"""
app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[
                    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
                    ],
                use_pages=True)

app.layout = html.Div(
    [   
        dbc.Nav(
            [
                dbc.NavLink("Public expenditure on education in the UK (1833-2019)", href="/", active="exact"),
                dbc.NavLink("Enrolment distributed by level in UK public education (1854-2019)", href="/page2", active="exact"),
                dbc.NavLink("Distribution of public expenditure on education in the UK by spenders (1880-2019)	", href="/page3", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
        html.Hr(),
        dash.page_container
    ]
)

if __name__ == "__main__":
    app.run(debug=True)