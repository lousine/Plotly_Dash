import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

df = pd.read_csv('C:\\Users\\user\\PlotlyDash\\owid-covid-data.csv')

fig = px.scatter_geo(df, locations="iso_code", color="total_cases",
                     hover_name="location", size="total_cases",
                     animation_frame="date",
                     projection="natural earth")

fig2 = px.bar(df, x='continent', y='new_deaths',
             labels={'continent'},
             animation_frame="date",
             height=450)

dff = pd.read_csv('C:\\Users\\user\\PlotlyDash\\covid-l.csv')
dff.loc[dff['population'] < 80000000, 'location'] = 'Other countries'
fig3 = px.pie(dff, values='total_cases', names='location')


colors = {
        'full-background':  '#FFFACD',
        'block-borders':    '#484848'
}

margins = {
        'block-margins': '10px 10px 10px 10px',
        'block-margins': '4px 4px 4px 4px'
}

sizes = {
        'subblock-heights': '4px 4px 4px 4px'
}

div_title = html.Div(children =	html.H1('Coronavirus Statistics'),
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'text-align': 'center'
							}
					)

div_1_1 = html.Div(children = ['Total Coronavirus Cases Worldwide (2021)',
                                  dcc.Graph(
                                      id='graph1',
                                      figure=fig)],             
					style ={
                            'border': '1px {} solid'.format(colors['block-borders']),
                            'margin': margins['block-margins'],
                            'width': '49%',
                            'height': sizes['subblock-heights'],
                            }
                )

div_1_2 = html.Div(children = ['Daily Death Cases by Continent (2021)',
                               dcc.Graph(
                                      id='graph2',
                                      figure=fig2)],
                    style ={
                            'border': '1px {} solid'.format(colors['block-borders']),
                            'margin': margins['block-margins'],
                            'width': '49%',
                            'height': sizes['subblock-heights']
                    }
                )

div_raw1 = html.Div(children =    [div_1_1,
                                div_1_2
                                ],
                    style ={
                            'border': '3px {} solid'.format(colors['block-borders']),
                            'margin': margins['block-margins'],
                            'display': 'flex',
                            'flex-flaw': 'row-wrap'
                            })

div_2_1 = html.Div(children = ['Total Cases Worldwide by April 20, 2021',
                               dcc.Graph(
                                      id='graph3',
                                      figure=fig3)],
                    style ={
                            'border': '1px {} solid'.format(colors['block-borders']),
                            'margin': margins['block-margins'],
                            'width': '49%',
                            'height': sizes['subblock-heights'],
                    }
                )

div_2_2 = html.Div(children = ['Data Table',
                               dash_table.DataTable(
                                   id='table',
                                   columns=[{"name": i, "id": i} for i in df.columns],
                                   data=df.to_dict('records'), 
                                   fixed_rows={'headers': True},
                                   style_table={'height': 400}
                                   )],
                    style = {
                            'border': '1px {} solid'.format(colors['block-borders']),
                            'margin': margins['block-margins'],
                            'width': '49%',
                            'height': sizes['subblock-heights'],
                    }
                )

div_raw2 = html.Div(children =    [div_2_1,
                                div_2_2
                                ],
                    style ={
                            'border': '3px {} solid'.format(colors['block-borders']),
                            'margin': margins['block-margins'],
                            'display': 'flex',
                            'flex-flaw': 'row-wrap'
                            })

app.layout = html.Div(  [
                        div_title,
                        div_raw1,
                        div_raw2
                        ],
                        style = {
                            'backgroundColor': colors['full-background']
                        }
                    )

app.run_server(debug=True, port = 8088)