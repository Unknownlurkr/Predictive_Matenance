import pandas as pd
import joblib
from sqlalchemy import create_engine

def predict_maintenance(input_data):
    model = joblib.load('models/predictive_maintenance_model.pkl')
    data = pd.read_csv(input_data)
    
    predictions = model.predict(data)
    return predictions

if __name__ == "__main__":
    input_data = 'data/processed_data.csv'
    predictions = predict_maintenance(input_data)
    print(predictions)