import pandas as pd
import joblib
from sqlalchemy import create_engine
from pyspark.sql import SparkSession
from pyspark.ml.classification import RandomForestClassificationModel
from config import HDFS_URL, SPARK_MASTER

def predict_maintenance(input_data):
    spark = SparkSession.builder.master(SPARK_MASTER).appName("PredictiveMaintenance").getOrCreate()
    model = RandomForestClassificationModel.load(f'{HDFS_URL}/models/rf_model')
    
    df = spark.read.csv(input_data, header=True, inferSchema=True)
    predictions = model.transform(df)
    predictions.show()

if __name__ == "__main__":
    input_data = f'{HDFS_URL}/processed_data.csv'
    predict_maintenance(input_data)

"""
def predict_maintenance(input_data):
    model = joblib.load('models/predictive_maintenance_model.pkl')
    data = pd.read_csv(input_data)
    
    predictions = model.predict(data)
    return predictions

if __name__ == "__main__":
    input = 'data/processed_data.csv'
    predictions = predict_maintenance(input)
    print(predictions)
"""
