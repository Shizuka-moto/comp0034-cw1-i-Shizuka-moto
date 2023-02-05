import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html, Input, Output

dash.register_page(__name__, path='/')

ex = pd.read_excel(r"after prepare.xlsx",sheet_name = "expenditure")
ex = ex[['Years','Constant 1990  prices','Education Price Index']]

layout = html.Div(
    [
        dcc.Graph(id='line-fig',
                  figure=px.line(ex, x='Years', y='Constant 1990  prices',
                                 title="Public expenditure on education in the UK from 1833 to 2019 (constant price of 2019)" )),
        dcc.Graph(id='line-fig2',
                  figure=px.line(ex, x='Years', y='Education Price Index',
                                 title="Education Price Index in the UK from 1833 to 2019")),
    ]
)