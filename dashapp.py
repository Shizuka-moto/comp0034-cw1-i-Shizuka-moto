import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import dash

app = Dash(__name__, 
external_stylesheets=[dbc.themes.BOOTSTRAP],
meta_tags=[
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
)

ex = pd.read_excel(r"after prepare.xlsx",sheet_name = "expenditure")
ex = ex[['Years','Constant 1990  prices']]
en = pd.read_excel(r"after prepare.xlsx",sheet_name = "enrolment")
ins = pd.read_excel(r"after prepare.xlsx",sheet_name = "institutional_distribution")



app.layout = html.Div([

    html.H1("Data visualization on public education in the UK 1833-2019.", style={'text-align': 'center'}),
    dcc.Dropdown(id="select_dataset",
                 options=[
                     {"label": "Public expenditure on education in the UK from 1833 to 2019 (constant price of 2019).", "value": 1},
                     {"label": "Trend of enrolment distributed by level in UK public education from 1854 to 2019.", "value": 2},
                     {"label": "Distribution of public expenditure on education in the UK by spenders from 1880 to 2019.", "value": 3},
                         ],
                 multi=False,
                 value=1,
                 style={'width': "60%"}
                 ),

    html.Div(id='container', children=[]),
    html.Br(),
    dcc.Graph(id='graph', figure={}),
])



@app.callback(
    [Output(component_id='container', component_property='children'),
     Output(component_id='graph', component_property='figure')],
    [Input(component_id='select_dataset', component_property='value')]
)



def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The dataset chosen by user was: {}".format(option_slctd)

    exx = ex.copy()
    enn = en.copy()
    inss = ins.copy()

    # Plotly Express
    if option_slctd == 1:
        fig = px.line(
            exx,
            x="Years",
            y="Constant 1990  prices",
            template='simple_white',)
        
    if option_slctd == 2:
        #data normalization
        for column in enn.columns:
            enn[column] = enn[column]  / enn[column].abs().max()
        enn['Years'] = en['Years']
        fig = px.line(
            enn,
            x="Years",
            y=['TOTAL','Primaire','Secondaire','Higher education ','Special','Further Education'],
            template='simple_white',)
        
    if option_slctd == 3:
        fig = px.line(
            inss,
            x="Years",
            y=['Total','Central Government','LEA','UGC'],
            template='simple_white',)
    return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)