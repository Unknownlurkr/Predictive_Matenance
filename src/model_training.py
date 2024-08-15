import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from sqlalchemy import create_engine
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from config import HDFS_URL, SPARK_MASTER

def train_model():
    spark = SparkSession.builder.master(SPARK_MASTER).appName("PredictiveMaintenance").getOrCreate()
    df = spark.read.csv(f'{HDFS_URL}/processed_data.csv', header=True, inferSchema=True)
    
    assembler = VectorAssembler(inputCols=['vibration'], outputCol='features')
    data = assembler.transform(df)
    
    rf = RandomForestClassifier(labelCol='label', featuresCol='features', numTrees=100)
    model = rf.fit(data)
    
    model.write().overwrite().save(f'{HDFS_URL}/models/rf_model')

if __name__ == "__main__":
    train_model()


def train_model_v1():
    engine = create_engine('postgresql://user:password@localhost/predictive_maintenance')
    data = pd.read_sql('processed_data', engine)
    
    X = data.drop(['timestamp', 'failure'], axis=1)
    y = data['failure']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    joblib.dump(model, 'models/predictive_maintenance_model.pkl')

if __name__ == "__main__":
    train_model_v1()