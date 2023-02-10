import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash import dcc, html, Input, Output, callback
"""
Program name: page2.py
Student number: 20054718

Layout of second page, including graphs, slider and callback.
"""
dash.register_page(__name__)

en = pd.read_excel(r"after prepare.xlsx",sheet_name = "enrolment")
enn = en.copy()
ennn = en.copy()
ennnn = en.copy()
for column in ennn.columns:
    ennn[column] = ennn[column]  / ennn[column].abs().max()
ennn['Years'] = enn['Years']
enn_t = ennnn[['Primaire','Secondaire','Higher education ','Special','Further Education']]
enn_t = enn_t.T
layout = html.Div(
    [
        dcc.Graph(id='bar-fig',
                  figure=px.line(
            ennn,
            x="Years",
            y=['Primaire','Secondaire','Higher education ','Special','Further Education'],
            title="Trend of enrolment distributed by level in UK public education from 1854 to 2019 (after normalized)",
            )
        ),
        dcc.Graph(id='bar-fig2',
                  figure=px.bar(
            enn,
            x = "Years",
            y = ['Primaire','Secondaire','Higher education ','Special','Further Education'],
            title="Amount of enrolment distributed by level in UK public education from 1854 to 2019",
        ).update_layout(xaxis_title="Years", yaxis_title="amount")
                  ),
        dcc.Graph(id='pie-chart', figure={}),
        dcc.Slider(min=1854,
                   max=2019,
                   step=5,
                   value=1854,
                   tooltip={"placement": "bottom", "always_visible": True},
                   updatemode='drag',
                   persistence=True,
                   id='my-slider',
        ),
        ])
@callback(
    Output(component_id='pie-chart', component_property='figure'),
    Input(component_id='my-slider', component_property='value')
)
def update_graph(input_value):
    """
       update graph according to slider input.

       Args:
       input_value: input year value of slider

       Return
       pie chart relate to input onformation.
    """
    fig1 = px.pie(
            enn_t,
            values = input_value - 1854,
            names = ['Primaire','Secondaire','Higher education ','Special','Further Education'],
            title="Amount of enrolment distributed by level in UK public education from 1854 to 2019",
        )
    fig1.update_traces(textposition='inside', textinfo='percent+label')
    return fig1