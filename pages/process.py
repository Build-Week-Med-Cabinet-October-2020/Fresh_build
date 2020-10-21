# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
row = html.Div(
    [
        dbc.Row(
            [
                dcc.Markdown(
                    """
                
                    ## Process

                    Our process uses two diffrent models, the first one uses TFIDF vectorization to turn our data into 
                    values that we can work with and manipulate into a way that we can use them in the second model to make 
                    recomendations for the user.

                    The second model is called nearest neighbors, it takes the data from the first model and gives a value
                    to each observation, and it finds the observations nearest to a given observation that the user will input

                    We made a function that passes user input into the TFIDF vectorization and then it uses the nearest neighbors
                    model to recommend the three nearest marjuana strains that suits all the users specified parameters`

                    """
                ),
            ]
        ),

        dbc.Row(
            [
                dbc.Col(
                    html.Div(html.Img(src=app.get_asset_url('nearestNeighbors.png'), style={'height':'83%','width':'83%'})),
                ),
                dbc.Col(
                    html.Div(html.Img(src=app.get_asset_url('equation.png'))), 
                ),
            ]
        )

    ],
)

layout = row