import pandas as pd
from sqlalchemy import create_engine

def process_data():
    engine = create_engine('postgresql://user:password@localhost/predictive_maintenance')
    sensor_data = pd.read_sql('sensor_data', engine)
    
    # Example processing: creating features like moving average, rolling statistics
    sensor_data['moving_avg'] = sensor_data['vibration'].rolling(window=10).mean()
    
    # Save processed data
    sensor_data.to_sql('processed_data', engine, if_exists='replace', index=False)

if __name__ == "__main__":
    process_data()