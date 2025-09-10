# client_progress.py
import pandas as pd

class ClientProgress:
    def __init__(self):
        # Crear un DataFrame para almacenar el progreso
        self.data = pd.DataFrame(columns=pd.Index(["cita", "peso", "medidas", "calorias"]))
        
    def add_progress(self, cita, peso, medidas, calorias):
        # Crear un DataFrame con la nueva fila
        new_row = pd.DataFrame([{
            "cita": cita,
            "peso": peso,
            "medidas": medidas,
            "calorias": calorias
        }])
        # Concatenar el DataFrame existente con la nueva fila
        self.data = pd.concat([self.data, new_row], ignore_index=True)

    def get_progress(self):
        return self.data