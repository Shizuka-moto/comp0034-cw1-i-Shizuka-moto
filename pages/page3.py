import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback

dash.register_page(__name__)

ins = pd.read_excel(r"after prepare.xlsx",sheet_name = "institutional_distribution")
inss = ins.copy()
insss = ins.copy()
inssss = ins.copy()
for column in insss.columns:
    insss[column] = insss[column]  / insss[column].abs().max()
insss['Years'] = inss['Years']
inssss_t = inssss[['Central Government','LEA','UGC']]
inssss_t = inssss_t.T
layout = html.Div(
    [
        dcc.Graph(id='bar-fig',
                  figure=px.line(
            insss,
            x="Years",
            y=['Total','Central Government','LEA','UGC'],
            title="Trend of Distribution of public expenditure on education in the UK by spenders from 1880 to 2019 (after normalized)",
            )
                  ),
        dcc.Graph(id='bar-fig2',
                  figure=px.bar(
            inss,
            x = "Years",
            y = ['Central Government','LEA','UGC'],
            title="Amount of public expenditure on education in the UK by spenders from 1880 to 2019",
        ).update_layout(xaxis_title="Years", yaxis_title="amount")),
        dcc.Graph(id='pie-chart2', figure={}),
        dcc.Slider(min=1880,
                   max=2019,
                   step=5,
                   value=1854,
                   tooltip={"placement": "bottom", "always_visible": True},
                   updatemode='drag',
                   persistence=True,
                   id='my-slider2',
        ),
    ]
)
@callback(
    Output(component_id='pie-chart2', component_property='figure'),
    Input(component_id='my-slider2', component_property='value')
)
def update_graph(input_value):
    fig1 = px.pie(
            inssss_t,
            values = input_value - 1880,
            names = ['Central Government','LEA','UGC'],
            title="Distribution of public expenditure on education in the UK by spenders from 1880 to 2019",
        )
    fig1.update_traces(textposition='inside', textinfo='percent+label')
    return fig1