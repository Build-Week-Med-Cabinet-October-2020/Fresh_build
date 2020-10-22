# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Marijuana Recommender

            This app will help guide you on the right path to enjoying your high everytime!
            
            ✅ MedCabinet is designed with the user in mind, we take your input to help narrow down your choices of weed that will help fit your lifestyle.
            
            ❌ MedCabinet is delicatly enhanced to give each user the best possible feedback. Working closely with a expert team of data scientist we have sourced get the highest quality information to help our patients with incredible accuracy.

            Marijuana can help treat a multitude of diffrent ailments, but one of the harder questions is 
            what strain is right for you. Do you want the strain that helps you be more creative and able to focus, the one 
            that is supposed to calm you down and make you less anxious, or a certain mix of both?
            
            This app was made to help answer these
            questions in a meaningful and usable way. It is simple to use and can give a recommendation backed
            by data on what the user should buy for their personal treatment.

            """
        ),
        dcc.Link(dbc.Button('Find out what you need', color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        html.Div(html.Img(src=app.get_asset_url('herb.jpg'), style={'height': '80%', 'width': '80%'}))
    ]
)

layout = dbc.Row([column1, column2])
