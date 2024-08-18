from flask import Flask, render_template  # Importing Flask for web app creation
import pandas as pd  # Importing the pandas library for data manipulation
import plotly.express as px  # Importing Plotly for data visualization
from plotly.io import to_html  # Importing to_html to convert Plotly graphs to HTML
from sqlalchemy import create_engine  # Importing create_engine to interact with PostgreSQL

# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def index():
    """
    Function to render the home page with the sensor data visualization.
    """
    
    # Creating a PostgreSQL engine connection
    engine = create_engine('postgresql://user:password@localhost/predictive_maintenance')
    
    # Read processed data from PostgreSQL
    data = pd.read_sql('processed_data', engine)
    
    # Create a line plot for 'vibration' over time
    fig = px.line(data, x='timestamp', y='vibration', title='Vibration Over Time')
    
    # Convert the plotly figure to HTML to embed in the web page
    graph_html = to_html(fig, full_html=False)
    
    # Render the HTML template and pass the graph HTML to it
    return render_template('index.html', graph_html=graph_html)

if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode
