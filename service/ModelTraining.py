import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime
import joblib
import warnings

class ModelTraining:
    def __init__(self):
        self.model = None
        self.scaler = None
        self.X_train_columns = None
    
    def train_model(self):# Load the model and scaler (do this ONCE when the app starts)
        try:
            self.model = tf.keras.models.load_model("wildfire_prediction_model_with_class_weights.h5")
            self.scaler = joblib.load("my_scaler.pkl")
            self.X_train_columns = pd.read_csv("/content/historical_environmental_data.csv").drop(columns=["timestamp"]).columns  # Store X_train columns

            print("Model and scaler loaded successfully.") # Print statement to verify the loading
        except Exception as e:
            print(f"Error loading model or scaler: {e}")
            exit()  # Exit the app if loading fails

    def predict_fire(self, data):
        df_new = pd.read_csv(data) # Assumes you get a single row of data
        # If you expect multiple rows, adjust accordingly (e.g., df_new = pd.DataFrame(data))
        # Convert timestamp if needed
        if 'timestamp' in df_new.columns:
            df_new['timestamp'] = df_new['timestamp'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S").timestamp())

        X_new = df_new.drop(columns=["timestamp"]) if 'timestamp' in df_new.columns else df_new

        # Ensure X_new has the SAME columns and order as X_train
        X_new = X_new[X_train_columns]

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            X_new_scaled = scaler.transform(X_new)

        X_new_reshaped = X_new_scaled.reshape(X_new_scaled.shape[0], 1, X_new_scaled.shape[1])

        predictions = self.model.predict(X_new_reshaped)

        # Process predictions and return JSON response
        probabilities = predictions[0].tolist()  # Convert to list for JSON
        predicted_class = np.argmax(predictions[0])
        severity_labels = {0: "No Fire", 1: "Low", 2: "Medium", 3: "High"}
        predicted_severity = severity_labels[predicted_class]

        response = {
            'probabilities': probabilities,
            'predicted_severity': predicted_severity
        }

        return response


    
