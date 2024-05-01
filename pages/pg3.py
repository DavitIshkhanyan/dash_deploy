import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

dash.register_page(__name__,
                   path="/maritalDesc",
                   name="Marital Desc",
                   title="Marital Desc"
                   )


df = pd.read_csv("hrdataset.csv")

# First graph
mean_df = df.groupby('MaritalDesc')['PerfScoreID'].mean().reset_index()
fig_performance = px.bar(mean_df, y='MaritalDesc', x='PerfScoreID', title='Mean Performance Score by Marital Status', orientation='h')

# Second graph
number_of_leaves = df.groupby('MaritalDesc')['Absences'].sum().reset_index()
fig_absences = px.bar(number_of_leaves, x='MaritalDesc', y='Absences', title='Total Absences by Marital Status')

# Layout
layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Performance Score and Absences by Marital Status", className="text-center"), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="performance_score_graph", figure=fig_absences)], width={
            'size':10,
            "offset":1
        }),
    ]
    ),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="multi_stock_selector_graph", figure=fig_performance)
        ], width={
            'size':10,
            "offset":1
        })])
], fluid=True)