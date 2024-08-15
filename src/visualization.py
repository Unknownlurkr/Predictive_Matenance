import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

def visualize_data():
    engine = create_engine('postgresql://user:password@localhost/predictive_maintenance')
    data = pd.read_sql('processed_data', engine)
    
    fig = px.line(data, x='timestamp', y='vibration', title='Vibration Over Time')
    fig.show()

if __name__ == "__main__":
    visualize_data()