import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from pyspark.sql import SparkSession
from config import HDFS_URL, SPARK_MASTER

app = dash.Dash(__name__)

spark = SparkSession.builder.master(SPARK_MASTER).appName("PredictiveMaintenance").getOrCreate()
df = spark.read.csv(f'{HDFS_URL}/processed_data.csv', header=True, inferSchema=True).toPandas()

app.layout = html.Div([
    html.H1("Predictive Maintenance Dashboard"),
    dcc.Graph(id='vibration-graph'),
    dcc.Interval(id='interval-component', interval=1*1000, n_intervals=0)
])

@app.callback(Output('vibration-graph', 'figure'), [Input('interval-component', 'n_intervals')])
def update_graph(n):
    fig = px.line(df, x='timestamp', y='vibration', title='Vibration Over Time')
    return fig

def visualize_data():
    engine = create_engine('postgresql://user:password@localhost/predictive_maintenance')
    data = pd.read_sql('processed_data', engine)
    
    fig = px.line(data, x='timestamp', y='vibration', title='Vibration Over Time')
    fig.show()

if __name__ == "__main__":
    visualize_data()
    app.run_server(debug=True)