import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

dash.register_page(__name__,
                   path="/gender",
                   name="Gender",
                   title="Gender"
                   )


df = pd.read_csv("hrdataset.csv")

# First graph
employees_count_by_gender = df.groupby('Sex').Employee_Name.count().reset_index(name='count')
fig_gender = px.pie(employees_count_by_gender, values='count', names='Sex', title='Gender Distribution')

# Second graph
fig = px.box(df, y='Sex', x='Salary', orientation='h', color='Sex')
fig.update_layout(
    title='Salary Distribution by Gender',
    yaxis_title='Gender',
    xaxis_title='Salary',
)

# Layout
layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Gender Statistics", className="text-center"), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="gender_distribution_graph", figure=fig_gender)], width=4),

        dbc.Col([
            dcc.Graph(id="salary_distribution_graph", figure=fig)], width=8)
    ]
    )
], fluid=True)