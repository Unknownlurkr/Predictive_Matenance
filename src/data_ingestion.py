import pandas as pd
from kafka import KafkaConsumer
from sqlalchemy import create_engine
from hdfs import InsecureClient
from config import KAFKA_TOPIC, KAFKA_BOOTSTRAP_SERVERS, HDFS_URL

def ingest_data():
    consumerV1 = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    hdfs_client = InsecureClient(HDFS_URL, user='hdfs') # predictive_mat_csv in file
    
    for message in consumerV1:
        data = message.value.decode('utf-8')
        hdfs_client.write('/data/sensor_data.txt', data, append=True)
    
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