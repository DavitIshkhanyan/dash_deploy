import dash
from dash import dcc, html, callback
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

dash.register_page(__name__,
                   path="/employees",
                   name="Employees",
                   title="Employees"
                   )

df = pd.read_csv("/hrdataset.csv")

sorted_method = ['By department', 'By Recruitment Source']

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('Employees Number Sorted By different methods'),
            dcc.Dropdown(id="sort_method_selector", options=[{"label":label,"value":index} for index, label in enumerate(sorted_method)], multi=False, searchable=False, value=0),
            dcc.Graph(id="employees_number_graph", figure={})])
    ])

])


@callback(
    Output('employees_number_graph', 'figure'),
    Input('sort_method_selector', 'value')
)
def update_graph1(method):
    if method == 0:
        employees_count = df.groupby('Department').Employee_Name.count().reset_index()

        fig = go.Figure(data=[go.Bar(
            x=employees_count['Department'],
            y=employees_count['Employee_Name'],
            text=employees_count['Employee_Name'],
            textposition='auto',
            marker=dict(color='skyblue')
        )])
        fig.update_layout(
            title='Total number of employees in each department',
            xaxis=dict(title='Department'),
            yaxis=dict(title='Number of employees'),
            bargap=0.15,
            bargroupgap=0.1,
            plot_bgcolor='rgba(0,0,0,0)'
        )
    else:
        employees_count = df.groupby('RecruitmentSource').Employee_Name.count()
        fig = go.Figure()

        color_scale = px.colors.qualitative.Set1

        for i, (source, count) in enumerate(employees_count.items()):
            fig.add_trace(go.Bar(
                y=[source],
                x=[count],
                orientation='h',
                name=source,
                marker=dict(color=color_scale[i]),
            ))

        fig.update_layout(
            title='Number of Employees Recruited through Different Hiring Sources',
            xaxis=dict(title='Employee Count'),
            yaxis=dict(title='Recruitment Source'),
            barmode='stack',
            plot_bgcolor='rgba(0,0,0,0)'
        )

    return fig