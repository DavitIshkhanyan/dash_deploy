import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

dash.register_page(__name__,
                   path="/departments",
                   name="Departments",
                   title="Departments"
                   )


df = pd.read_csv("/hrdataset.csv")

# First graph
fig_salary = px.box(df, x='Department', y='Salary', title='Salary Distribution by Department')

# Second graph
emp_satis = df.groupby('Department').EmpSatisfaction.mean().reset_index()

fig_satisfaction = px.scatter(emp_satis, x='Department', y='EmpSatisfaction',
                 title='Department-wise Employee Satisfaction',
                 labels={'EmpSatisfaction': 'Employee Satisfaction Score', 'Department': 'Department'})

fig_satisfaction.update_traces(mode='markers+lines', marker=dict(color='green', symbol='circle-open-dot'))

# Layout
layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Department-wise Salary and Satisfaction", className="text-center"), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="salary_distribution_graph", figure=fig_salary)], width=6),

        dbc.Col([
            dcc.Graph(id="satisfaction_graph", figure=fig_satisfaction)], width=6)
    ]
    )
], fluid=True)