import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from sqlalchemy import create_engine

def train_model():
    engine = create_engine('postgresql://user:password@localhost/predictive_maintenance')
    data = pd.read_sql('processed_data', engine)
    
    X = data.drop(['timestamp', 'failure'], axis=1)
    y = data['failure']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    joblib.dump(model, 'models/predictive_maintenance_model.pkl')

if __name__ == "__main__":
    train_model()