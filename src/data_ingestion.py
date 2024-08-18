import pandas as pd  # Importing the pandas library for data manipulation
from kafka import KafkaConsumer  # Importing KafkaConsumer to read data from Kafka
from sqlalchemy import create_engine  # Importing create_engine to interact with PostgreSQL

def ingest_data():
    """
    Function to ingest sensor data from a Kafka topic and store it into a PostgreSQL database.
    """
    
    # Simulate Kafka Consumer that listens to the 'sensor_data_topic' topic
    consumer = KafkaConsumer('sensor_data_topic', bootstrap_servers=['localhost:9092'])
    
    # Creating a PostgreSQL engine connection (replace user, password, and database name with your settings)
    engine = create_engine('postgresql://user:password@localhost/predictive_maintenance')

    for message in consumer:
        # Decode and read the CSV data from Kafka messages
        data = pd.read_csv(message.value.decode('utf-8'))
        
        # Insert data into the 'sensor_data' table in PostgreSQL
        data.to_sql('sensor_data', engine, if_exists='append', index=False)

if __name__ == "__main__":
    ingest_data()
