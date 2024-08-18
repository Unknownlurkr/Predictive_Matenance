import pandas as pd  # Importing the pandas library for data manipulation
from sqlalchemy import create_engine  # Importing create_engine to interact with PostgreSQL

def process_data():
    """
    Function to process the sensor data by calculating features like moving averages
    and storing the processed data back into the PostgreSQL database.
    """
    
    # Creating a PostgreSQL engine connection
    engine = create_engine('postgresql://user:password@localhost/predictive_maintenance')
    
    # Read sensor data from the 'sensor_data' table
    sensor_data = pd.read_sql('sensor_data', engine)
    
    # Example processing: Calculating moving average for the 'vibration' column over a window of 10 data points
    sensor_data['moving_avg'] = sensor_data['vibration'].rolling(window=10).mean()
    
    # Save processed data back into PostgreSQL under the table 'processed_data'
    sensor_data.to_sql('processed_data', engine, if_exists='replace', index=False)

if __name__ == "__main__":
    process_data()
