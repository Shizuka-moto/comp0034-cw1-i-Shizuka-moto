import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html, Input, Output


ex = pd.read_excel(r"after prepare.xlsx",sheet_name = "expenditure")
exx = ex[['Years','Constant 1990  prices','Education Price Index']]

exx = exx.T

print(exx)