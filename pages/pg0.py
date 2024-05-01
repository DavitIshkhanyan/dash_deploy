import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__,
                   path="/",
                   name="Home",
                   title="HR"
                   )


layout = dbc.Container([
    dbc.Row(
        [
            dbc.Col([html.Img(src='../assets/img.png')])
        ]
    )
])