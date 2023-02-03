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


ennn = enn.copy()
#data normalization
for column in ennn.columns:
    ennn[column] = ennn[column]  / ennn[column].abs().max()
ennn['Years'] = enn['Years']

print(ennn)