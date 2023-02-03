import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc



app = Dash(__name__, 
external_stylesheets=[dbc.themes.BOOTSTRAP],
meta_tags=[
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
)



ex = pd.read_excel(r"after prepare.xlsx",sheet_name = "expenditure")
ex = ex[['Years','Constant 1990  prices','Education Price Index']]
en = pd.read_excel(r"after prepare.xlsx",sheet_name = "enrolment")
ins = pd.read_excel(r"after prepare.xlsx",sheet_name = "institutional_distribution")



app.layout = html.Div([
    html.H1("Data visualization about education in the UK 1833-2019.", style={'text-align': 'center'}),
    dcc.Dropdown(id="select_dataset",
                 options=[
                     {"label": "Public expenditure on education in the UK from 1833 to 2019 (constant price of 2019).", "value": 1},
                     {"label": "Trend of enrolment distributed by level in UK public education from 1854 to 2019.", "value": 2},
                     {"label": "Distribution of public expenditure on education in the UK by spenders from 1880 to 2019.", "value": 3},
                         ],
                 multi=False,
                 value=2,
                 style={'width': "80%"}
                 ),

    html.Div(id='container', children=[]),
    html.Br(),
    dcc.Graph(id='graph', figure={}),
    dcc.Graph(id='graph2', figure={}),
])



@app.callback(
    [Output(component_id='container', component_property='children'),
     Output(component_id='graph', component_property='figure'),
     Output(component_id='graph2', component_property='figure')],
    [Input(component_id='select_dataset', component_property='value'),]
)



def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The dataset chosen by user was: {}".format(option_slctd)
    exx = ex.copy()
    enn = en.copy()
    inss = ins.copy()

    if option_slctd == 1:
        fig = px.line(
            exx,
            x = "Years",
            y = "Constant 1990  prices",
            title="Public expenditure on education in the UK from 1833 to 2019 (constant price of 2019)")
        fig2 = px.line(
            exx,
            x = "Years",
            y = "Education Price Index",
            title="Education Price Index in the UK from 1833 to 2019")

    if option_slctd == 2:
        ennn = enn.copy()
        #data normalization
        for column in ennn.columns:
            ennn[column] = ennn[column]  / ennn[column].abs().max()
        ennn['Years'] = enn['Years']
        fig = px.line(
            ennn,
            x="Years",
            y=['TOTAL','Primaire','Secondaire','Higher education ','Special','Further Education'],
            title="Plot of trend of enrolment distributed by level in UK public education from 1854 to 2019 (after normalized)",
            )
        fig2 = px.bar(
            enn,
            x = "Years",
            y = ['Primaire','Secondaire','Higher education ','Special','Further Education'],
            title="Amount of enrolment distributed by level in UK public education from 1854 to 2019",
        ).update_layout(xaxis_title="Years", yaxis_title="amount of people by different level of enrolment from 1854 to 2019")
        
    if option_slctd == 3:
        insss = inss.copy()
        #data normalization
        for column in insss.columns:
            insss[column] = insss[column]  / insss[column].abs().max()
        insss['Years'] = inss['Years']
        fig = px.line(
            insss,
            x="Years",
            y=['Total','Central Government','LEA','UGC'],
            title="Plot of trend of Distribution of public expenditure on education in the UK by spenders from 1880 to 2019 (after normalized)",
            )
        fig2 = px.bar(
            inss,
            x = "Years",
            y = ['Central Government','LEA','UGC'],
            title="Amount of public expenditure on education in the UK by spenders from 1880 to 2019",
        ).update_layout(xaxis_title="Years", yaxis_title="amount of public expenditure on education in the UK by spenders")
    return container, fig, fig2



if __name__ == '__main__':
    app.run_server(debug=True)