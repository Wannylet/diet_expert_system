import os
import pandas as pd

class ClientsInfo:
    def __init__(self, client_password: str) -> None:
        self.client_password = client_password
        
        self.clients_progress_path = "clients_info/clients_progress.csv"
        self.clients_rules_path = "clients_info/clients_rules.csv"

        # Inicializar DataFrames vacíos por si no existen los archivos (contra, cita, peso, medidas, calorias) (contra, tipo dieta, meta)
        self.clients_progress = pd.DataFrame(columns=pd.Index(["password", "appointment", "weight", "measurements", "calories"]))
        self.clients_rules = pd.DataFrame(columns=pd.Index(["password", "diet_type", "goal"]))

        if os.path.exists(self.clients_progress_path):
            self.clients_progress = pd.read_csv(self.clients_progress_path)
        
        if os.path.exists(self.clients_rules_path):
            self.clients_rules = pd.read_csv(self.clients_rules_path)
    
    def add_client_progress(self, appointment: str, weight: float, measurements: float, calories: int) -> None:
        new_row = pd.DataFrame([{
            "password": self.client_password,
            "appointment": appointment,
            "weight": weight,
            "measurements": measurements,
            "calories": calories
        }])


        self.clients_progress = pd.concat([self.clients_progress, new_row], ignore_index=True)
        self.clients_progress.to_csv(self.clients_progress_path, index=False)

    def add_client_rules(self, diet_type: str, goal: str) -> None:
        new_row = pd.DataFrame([{
            "password": self.client_password,
            "diet_type": diet_type,
            "goal": goal
        }])

        self.clients_rules = pd.concat([self.clients_rules, new_row], ignore_index=True)
        self.clients_rules.to_csv(self.clients_rules_path, index=False)
    
    def get_clients_progress(self):
        return self.clients_progress
    
    def get_clients_rules(self):
        return self.clients_rules
    
    def get_client_password(self):
        return self.client_password
    
    def get_client_progress(self):
        return self.clients_progress[self.clients_progress["password"] == self.client_password]

    def get_client_rules(self):
        return self.clients_rules[self.clients_rules["password"] == self.client_password]