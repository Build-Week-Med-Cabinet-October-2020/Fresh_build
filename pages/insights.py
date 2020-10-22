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
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights

            I learned a lot during this build. One of the biggest things was about what a JSON file is and how we can use the JSON
            to do many cool things. A json is a really simple way to store data for later use, it is a dictionary of dictionaries
            you can kind of think of a json as a tiny SQL database that you can access using the right keys to grab a single row or
            observation. Whats really cool is how well JavaScript can use the JSON to their advantage to do other things.

            Something else I learned about was the methods and algorithms used to make the predictions possible. I could not understand
            vectorization at the start, but I got it eventually. It is the act of turning words into numbers and then doing stuff with those numbers
            it helps a computer understand what a written language is and how it can be used to find something such as similarity in writing
            style between two different people.

            All in all this was a good build that taught me new things, like the two mentioned above and about what a Github workflow looks like
            working with a team of people rather than just yourself. If there was one thing that I could change it would be that our group
            didn't get a team lead, so we lost the experience of having to work under someone and instead just ended up talking to each other
            about our ideas and how to implement them.

            """
        ),

    ],
)

layout = dbc.Row([column1])
