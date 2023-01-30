import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
import pandas as pd


# -- Import and clean data (importing csv into pandas)
# df = pd.read_csv("intro_bees.csv")
ex = pd.read_excel(r"after prepare.xlsx",sheet_name = "expenditure")
ex = ex[['Years','Constant 1990  prices']]
en = pd.read_excel(r"after prepare.xlsx",sheet_name = "enrolment")
enn = en.copy()
ins = pd.read_excel(r"after prepare.xlsx",sheet_name = "institutional_distribution")

for column in enn.columns:
    enn[column] = enn[column]  / enn[column].abs().max()
enn['Years'] = en['Years']
print(enn)
y=["TOTAL","Primaire","Secondaire","Higher education","Special","Further Education"]


        fig2 = px.bar(
            enn,
            x = enn.loc[0].at["Grades"],
            y = ['Primaire','Secondaire','Higher education ','Special','Further Education'],
        )