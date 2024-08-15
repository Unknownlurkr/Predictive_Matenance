import pandas as pd
from kafka import KafkaConsumer
from sqlalchemy import create_engine

def ingest_data():
    # Simulating Kafka Consumer
    consumer = KafkaConsumer('sensor_data_topic', bootstrap_servers=['localhost:9092'])
    
    # Create a PostgreSQL engine
    engine = create_engine('postgresql://user:password@localhost/predictive_maintenance')

    for message in consumer:
        # Assuming each message is a CSV row
        data = pd.read_csv(message.value.decode('utf-8'))
        
        # Store data in PostgreSQL
        data.to_sql('sensor_data', engine, if_exists='append', index=False)

if __name__ == "__main__":
    ingest_data()