import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)



app = Dash(__name__)

# -- Import and clean data (importing csv into pandas)
# df = pd.read_csv("intro_bees.csv")
ex = pd.read_excel(r"after prepare.xlsx",sheet_name = "expenditure")
ex = ex[['Years','Constant 1990  prices']]
en = pd.read_excel(r"after prepare.xlsx",sheet_name = "enrolment")
ins = pd.read_excel(r"after prepare.xlsx",sheet_name = "institutional_distribution")

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),

    dcc.Dropdown(id="select_dataset",
                 options=[
                     {"label": "Public expenditure on education in the UK (1833-2019)", "value": 1},
                     {"label": "2016", "value": 2},
                     {"label": "2017", "value": 3},
                         ],
                 multi=False,
                 value=1,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={})

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='select_dataset', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The dataset chosen by user was: {}".format(option_slctd)

    exx = ex.copy()
    enn = en.copy()
    inss = ins.copy()
    dff = dff[dff["Year"] == option_slctd]
    dff = dff[dff["Affected by"] == "Varroa_mites"]

    # Plotly Express
    fig = px.line(
        exx,
        x='year',
        y='price of education(1990 price constant)'
        color_continuous_scale=px.colors.sequential.YlOrRd,
        template='plotly_dark'
    )


    return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)