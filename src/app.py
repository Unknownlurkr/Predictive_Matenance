from flask import Flask, render_template
import pandas as pd
import plotly.express as px
from plotly.io import to_html
from sqlalchemy import create_engine

app = Flask(__name__)

@app.route('/')
def index():
    engine = create_engine('postgresql://user:password@localhost/predictive_maintenance')
    data = pd.read_sql('processed_data', engine)
    
    fig = px.line(data, x='timestamp', y='vibration', title='Vibration Over Time')
    graph_html = to_html(fig, full_html=False)
    return render_template('index.html', graph_html=graph_html)

if __name__ == "__main__":
    app.run(debug=True)