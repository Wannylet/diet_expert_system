# client_progress.py
import pandas as pd

class ClientProgress:
    def __init__(self):
        # Crear un DataFrame para almacenar el progreso
        self.data = pd.DataFrame(columns=["cita", "peso", "medidas", "calorías"])
        
    def add_progress(self, cita, peso, medidas, calorías):
        # Añadir los datos de progreso de cada cita
        self.data = self.data.append({
            "cita": cita,
            "peso": peso,
            "medidas": medidas,
            "calorías": calorías
        }, ignore_index=True)
    
    def get_progress(self):
        return self.data