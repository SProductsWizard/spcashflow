from turtle import reset
from dash import dcc
from dash import html
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
from dash.dependencies import Input, Output
from WebApp.appBackendResources import *


df = db_mgr.finsightDataStatus()
res = go.Figure(
    data=[
        go.Table(
            header=dict(
                values=list(df.columns),
                fill_color="paleturquoise",
                align="left",
            ),
            cells=dict(
                values=[df[[col]] for col in df.columns],
                fill_color="lavender",
                align="left",
            ),
        )
    ]
)


layout = html.Div([dcc.Graph(figure=res)])
