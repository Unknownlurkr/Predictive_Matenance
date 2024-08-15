from flask import Flask, render_template
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from sqlalchemy import create_engine
from config import POSTGRESQL_CONN

app = Flask(__name__)

@app.route('/')
def index():
    engine = create_engine(POSTGRESQL_CONN)
    df = pd.read_sql('processed_data', engine)
    
    fig = px.line(df, x='timestamp', y='vibration', title='Vibration Over Time')
    return render_template('index.html', graph_html=fig.to_html())

if __name__ == "__main__":
    app.run(debug=True)
