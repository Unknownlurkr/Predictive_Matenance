import pandas as pd
from sqlalchemy import create_engine
from pyspark.sql import SparkSession
from config import HDFS_URL, SPARK_MASTER

def process_data():
    spark = SparkSession.builder.master(SPARK_MASTER).appName("PredictiveMaintenance").getOrCreate()
    df = spark.read.text(f'{HDFS_URL}/data/sensor_data.txt')
    
    # Sample processing (parsing, filtering, etc.)
    processed_df = df.selectExpr("split(value, ',')[0] as timestamp", "split(value, ',')[1] as vibration")
    processed_df.write.csv(f'{HDFS_URL}/processed_data.csv')
    engine = create_engine('postgresql://user:password@localhost/predictive_maintenance')
    sensor_data = pd.read_sql('sensor_data', engine)
    
    # Example processing: creating features like moving average, rolling statistics
    sensor_data['moving_avg'] = sensor_data['vibration'].rolling(window=10).mean()
    
    # Save processed data
    sensor_data.to_sql('processed_data', engine, if_exists='replace', index=False)

if __name__ == "__main__":
    process_data()