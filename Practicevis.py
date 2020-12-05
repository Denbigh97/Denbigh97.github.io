import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_cors import CORS
import csv
import os
from config import URI  
import pandas as pd
from sqlalchemy import create_engine

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('Cleaned_data1121.csv')
df

def data_selector(df):
    columns=df.columns
    data_options= [{'label' :k, 'value' :k} for k in columns]
    return dcc.Dropdown(
            id='data_selector',
            options=data_options,
            multi=True,
            #setting a default value, this is not required, but makes development easier.
            value=['Location_X', 'Location_Y'])

@app.callback(Output('data_selector', 'options'),
              [Input('datatable-upload-container’, ‘data’)])

def update_dropdown(rows):

    df = pd.DataFrame(rows)
    print('updating menus')
    columns=df.columns
    col_labels=[{'label' :k, 'value' :k} for k in columns]
    return col_labels

@app.callback(Output(‘datatable-upload-graph’, ‘figure’),
[State('datatable-upload-container’, ‘data’)]),
[Input(‘data_selector’, ‘value’)])

def display_graph(value):
 df = pd.DataFrame(rows)
 return {
 ‘data’: [{
#first column that was selected
 ‘x’: df[value[0]],
#second column that was selected
 ‘y’: df[[value[1],
 ‘type’: ‘bar’
 }]
 }




if __name__ == '__main__':
    app.run_server(debug=True)