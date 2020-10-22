# Imports from 3rd party libraries
import dash
import dash_table
import numpy as np
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import pickle



# Imports from this application
from app import app

#create models for nlp 
nn = pickle.load(open('pickled_recommender.pkl', 'rb'))
tfidf = pickle.load(open('pickled_vectorizer.pkl', 'rb'))


#import dataframe and clean for recommender function
df = pd.read_csv('https://raw.githubusercontent.com/kushyapp/cannabis-dataset/master/Dataset/Strains/strains-kushy_api.2017-11-14.csv')#, index_col='id')
df1 = df.drop(['sort', 'slug', 'image', 'thcv',
               'cbdv', 'cbn', 'cbg', 'cbgm',
               'cbgv', 'cbc', 'cbcv', 'cbv',
               'cbe', 'cbt', 'cbl', 'description',
               'crosses', 'location', 'terpenes',
               'breeder'], axis=1)
df1 = df1[df1['ailment'].notna()]

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
row = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            """
                        
                            ## Predictions

                            As a consumer of cannabis you most likely are looking to achieve something specific,
                            whether that specific feeling is just relaxation or creativity we are here to help find the right fit for you!
                            
                            """
                        ),
                    ],
                    md=5,
                ),

                dbc.Col(
                    [
                        dcc.Markdown('#### Strain Type'), 
                        dcc.Dropdown
                        (
                            id='ctype',
                            style= {
                            "color": "black",
                            },
                            options = [
                                {'label': 'Indica', 'value': 'Indica'}, 
                                {'label': 'Hybrid', 'value': 'Hybrid'}, 
                                {'label': 'Sativa', 'value': 'Sativa'}, 
                            ], 
                            value = 'Hybrid', 
                            className='mb-5', 
                        ),
                        dcc.Markdown('#### Effect'), 
                        dcc.Dropdown
                        (
                            id='effects',
                            style= {
                            "color": "black",
                            },
                            options = [
                                {'label': 'Happy', 'value': 'Happy'}, 
                                {'label': 'Dry Mouth', 'value': 'Dry Mouth'}, 
                                {'label': 'Relaxed', 'value': 'Relaxed'},
                                {'label': 'Euphoric', 'value': 'Euphoric'}, 
                                {'label': 'Uplifted', 'value': 'Uplifted'}, 
                                {'label': 'Paranoid', 'value': 'Paranoid'},
                                {'label': 'Sleepy', 'value': 'Sleepy'}, 
                                {'label': 'Anxious', 'value': 'Anxious'}, 
                                {'label': 'Creative', 'value': 'Creative'},
                                {'label': 'Energetic', 'value': 'Energetic'}, 
                                {'label': 'Hungry', 'value': 'Hungry'}, 
                                {'label': 'Focused', 'value': 'Focused'},
                                {'label': 'Tingly', 'value': 'Tingly'}, 
                                {'label': 'Talkative', 'value': 'Talkative'}, 
                                {'label': 'Horny', 'value': 'Horny'}, 
                            ], 
                            value = 'Happy', 
                            className='mb-5',
                            multi=True, 
                        ),
                        dcc.Markdown('#### Ailments'), 
                        dcc.Dropdown
                        (
                            id='ailment',
                            style= {
                            "color": "black",
                            },
                            options = [
                                {'label': 'Stress', 'value': 'Stress'}, 
                                {'label': 'Depression', 'value': 'Depression'}, 
                                {'label': 'Pain', 'value': 'Pain'},
                                {'label': 'Insomnia', 'value': 'Insomnia'}, 
                                {'label': 'Lack Of Appetite', 'value': 'Lack Of Appetite'}, 
                                {'label': 'Nausea', 'value': 'Nausea'},
                                {'label': 'Inflammation', 'value': 'Inflammation'}, 
                                {'label': 'Muscle Spasms', 'value': 'Muscle Spasms'}, 
                                {'label': 'Seizures', 'value': 'Seizures'},
                            ], 
                            value = 'Stress', 
                            className='mb-5',
                            multi=True, 
                        ),
                        dcc.Markdown('#### Flavor'), 
                        dcc.Dropdown
                        (
                            id='flavor',
                            style= {
                            "color": "black",
                            },
                            options = [
                                {'label': 'Earthy', 'value': 'Earthy'}, 
                                {'label': 'Sweet', 'value': 'Sweet'}, 
                                {'label': 'Citrus', 'value': 'Citrus'},
                                {'label': 'Berry', 'value': 'Berry'}, 
                                {'label': 'Pine', 'value': 'Pine'}, 
                                {'label': 'Lemon', 'value': 'Lemon'},
                                {'label': 'Skunk', 'value': 'Skunk'}, 
                                {'label': 'Grape', 'value': 'Grape'}, 
                                {'label': 'Blueberry', 'value': 'Blueberry'},
                                {'label': 'Lime', 'value': 'Lime'}, 
                                {'label': 'Orange', 'value': 'Orange'}, 
                                {'label': 'Pepper', 'value': 'Pepper'},
                                {'label': 'Ammonia', 'value': 'Ammonia'}, 
                                {'label': 'Mango', 'value': 'Mango'}, 
                                {'label': 'Pineapple', 'value': 'Pineapple'},
                                {'label': 'Strawberry', 'value': 'Strawberry'}, 
                                {'label': 'Lavender', 'value': 'Lavender'},
                                {'label': 'Honey', 'value': 'Honey'}, 
                                {'label': 'Coffee', 'value': 'Coffee'}, 
                                {'label': 'Rose', 'value': 'Rose'},
                                {'label': 'Vanilla', 'value': 'Vanilla'}, 
                                {'label': 'Mint', 'value': 'Mint'}, 
                                {'label': 'Apple', 'value': 'Apple'}, 
                            ], 
                            value = 'Earthy', 
                            className='mb-5',
                            multi=True, 
                        ),
                        # html.Button(id='Recommend', n_clicks=0, children='Submit'),
                        dbc.Button('Submit', id='Submit', color='primary'),
                        html.Div(html.P('')),
                        html.Div(html.P(''))
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                html.Div(id='output-state' ,className= 'lead')
            ],
            justify='center'
        )
    ]
)

layout = row

@app.callback(
    Output("output-state", "children"),
    [Input("Submit", "n_clicks")],
    [
        State("ctype", "value"),
        State("effects", "value"),
        State("ailment", "value"),
        State("flavor", "value"),
    ],
)
def recommender(n_clicks, input1, input2, input3, input4):
    # take in button submit and inputs from survery to create recommend output
    if n_clicks:
        effs = ' '.join(input2)
        ail = ' '.join(input3)
        fla = ' '.join(input4)
        new = pd.DataFrame([[input1, effs, ail, fla]], columns=['type', 'effects', 'ailment', 'flavor'])
        new['text'] = new['type'] + ', ' + new['effects'] + ', ' + new['ailment'] + ', ' + new['flavor']
        recommendations = nn.kneighbors(tfidf.transform(new['text']).todense())[1]
        data = np.array(
            [
                df1.iloc[recommendations[0][0]],
                df1.iloc[recommendations[0][1]],
                df1.iloc[recommendations[0][2]]
            ]
        )
        dfNew  = pd.DataFrame(columns=list(df1.columns), data=data)
        dfNew.drop(['thc','thca','cbd','cbda'], inplace=True, axis=1)

        y = str(
            {
                "recommendations": [
                    {
                        "recommendation 1": {
                            "name": df1.iloc[recommendations[0][0]]["name"],
                            "type": df1.iloc[recommendations[0][0]]["type"],
                            "effects": df1.iloc[recommendations[0][0]]["effects"],
                            "ailments": df1.iloc[recommendations[0][0]]["ailment"],
                            "flavors": df1.iloc[recommendations[0][0]]["flavor"],
                        },
                        "recommendation 2": {
                            "name": df1.iloc[recommendations[0][1]]["name"],
                            "type": df1.iloc[recommendations[0][1]]["type"],
                            "effects": df1.iloc[recommendations[0][1]]["effects"],
                            "ailments": df1.iloc[recommendations[0][1]]["ailment"],
                            "flavors": df1.iloc[recommendations[0][1]]["flavor"],
                        },
                        "recommendation 3": {
                            "name": df1.iloc[recommendations[0][2]]["name"],
                            "type": df1.iloc[recommendations[0][2]]["type"],
                            "effects": df1.iloc[recommendations[0][2]]["effects"],
                            "ailments": df1.iloc[recommendations[0][2]]["ailment"],
                            "flavors": df1.iloc[recommendations[0][2]]["flavor"],
                        },
                    }
                ]
            }
        )
        #df = pd.read_json(path_or_buf=x, orient='index')
        x = dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in dfNew.columns],
            data=dfNew.to_dict('records'),
            style_cell={
                'textAlign': 'left',
                'backgroundColor': 'rgba(50,50,50,0)',
                'color': 'white'
            }
        )
        return x


if __name__ == '__main__':
    app.run_server(debug=True)          
               
