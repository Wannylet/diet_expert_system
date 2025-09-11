# regression_model.py
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

class RegressionModel:
    def __init__(self, client_progress) -> None:
        self.model = LinearRegression()
        self.client_progress = client_progress
    
    def train_model(self):
        # Usar todas las filas para entrenar
        X = self.client_progress[['weight', 'measurements']]
        Y = self.client_progress['calories']
        self.model.fit(X, Y)
        
    def predict_diet(self) -> float:
        latest_data = self.client_progress.iloc[-1]
        size = np.array([[latest_data['weight'], latest_data['measurements']]])
        predicted_calories = self.model.predict(size)
        return predicted_calories[0]