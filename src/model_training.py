import pandas as pd  # Importing the pandas library for data manipulation
from sklearn.model_selection import train_test_split  # Importing train_test_split for splitting data
from sklearn.ensemble import RandomForestClassifier  # Importing RandomForestClassifier model
import joblib  # Importing joblib for model serialization
from sqlalchemy import create_engine  # Importing create_engine to interact with PostgreSQL

def train_model():
    """
    Function to train a RandomForestClassifier model using the processed sensor data.
    The trained model is saved for later use.
    """
    
    # Creating a PostgreSQL engine connection
    engine = create_engine('postgresql://user:password@localhost/predictive_maintenance')
    
    # Read processed data from PostgreSQL
    data = pd.read_sql('processed_data', engine)
    
    # Separate features (X) and target (y)
    X = data.drop(['timestamp', 'failure'], axis=1)  # Drop irrelevant columns
    y = data['failure']  # The target variable
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the RandomForestClassifier model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Save the trained model to a file
    joblib.dump(model, 'models/predictive_maintenance_model.pkl')

if __name__ == "__main__":
    train_model()
