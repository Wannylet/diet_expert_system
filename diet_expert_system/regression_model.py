# regression_model.py
from sklearn.linear_model import LinearRegression
import numpy as np

class RegressionModel:
    def __init__(self):
        self.model = LinearRegression()
    
    def train_model(self, X, y):
        # Entrenar el modelo con los datos de los clientes
        self.model.fit(X, y)
        
    def predict_diet(self, client_info):
        # Predecir la dieta usando los datos estadísticos
        size = np.array([[client_info['peso'], client_info['medidas']]])
        predicted_calories = self.model.predict(size)
        return predicted_calories