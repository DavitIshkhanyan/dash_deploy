import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

dash.register_page(__name__,
                   path="/other",
                   name="Non-White Employees",
                   title="Non-White Employees"
                   )


df = pd.read_csv("/hrdataset.csv")


count_of_employee = df[df.RaceDesc != 'White'].groupby('Position').Employee_Name.count().reset_index()
count_of_employee = count_of_employee.rename(columns={'Employee_Name': 'Total_employee_count'})

height = 40 + len(count_of_employee) * 25

fig = px.bar(count_of_employee, x='Total_employee_count', y='Position', color='Position', labels={'Total_employee_count': 'Total Employee Count', 'Position': 'Position'})
fig.update_layout(title='Total Employee Count by Position (Non-White Employees)', yaxis={'categoryorder':'total ascending'}, height=height)

# Layout
layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Non-White Employees", className="text-center"), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="tolerant_graph", figure=fig)], width=12),
    ]
    )
], fluid=True)