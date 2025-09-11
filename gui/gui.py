# gui.py
import tkinter as tk
from tkinter import messagebox, ttk
from diet_chart import generate_report

class DietExpertGUI:
    def __init__(self, clients_info, diet_recommender, regression_model):
        self.clients_info = clients_info
        self.diet_recommender = diet_recommender
        self.regression_model = regression_model
        
        self.window = tk.Tk()
        self.window.title("Sistema Experto de Dietas")
        self.window.geometry("600x600")
        
        # Variables Tkinter para entradas
        self.weight_var = tk.DoubleVar()
        self.measurements_var = tk.DoubleVar()
        self.calories_var = tk.DoubleVar()
        self.appointment_var = tk.StringVar()
        
        self.diet_type_var = tk.StringVar()
        self.goal_var = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Sección: Datos de cliente
        tk.Label(self.window, text="Ingrese sus datos de progreso", font=("Arial", 14)).pack(pady=10)
        
        form_frame = tk.Frame(self.window)
        form_frame.pack(pady=5)
        
        tk.Label(form_frame, text="Cita:").grid(row=0, column=0, sticky="e")
        tk.Entry(form_frame, textvariable=self.appointment_var).grid(row=0, column=1)
        
        tk.Label(form_frame, text="Peso (kg):").grid(row=1, column=0, sticky="e")
        tk.Entry(form_frame, textvariable=self.weight_var).grid(row=1, column=1)
        
        tk.Label(form_frame, text="Medidas (cm):").grid(row=2, column=0, sticky="e")
        tk.Entry(form_frame, textvariable=self.measurements_var).grid(row=2, column=1)
        
        tk.Label(form_frame, text="Calorías actuales:").grid(row=3, column=0, sticky="e")
        tk.Entry(form_frame, textvariable=self.calories_var).grid(row=3, column=1)
        
        tk.Button(self.window, text="Registrar Progreso", command=self.add_progress).pack(pady=10)
        
        # Sección: Reglas de dieta
        tk.Label(self.window, text="Configuración de dieta", font=("Arial", 14)).pack(pady=10)
        rules_frame = tk.Frame(self.window)
        rules_frame.pack(pady=5)
        
        tk.Label(rules_frame, text="Tipo de dieta:").grid(row=0, column=0, sticky="e")
        tk.Entry(rules_frame, textvariable=self.diet_type_var).grid(row=0, column=1)
        
        tk.Label(rules_frame, text="Objetivo:").grid(row=1, column=0, sticky="e")
        tk.Entry(rules_frame, textvariable=self.goal_var).grid(row=1, column=1)
        
        tk.Button(self.window, text="Actualizar Reglas", command=self.update_rules).pack(pady=10)
        
        # Sección: Recomendación y predicción
        tk.Button(self.window, text="Recomendar Dieta", command=self.show_recommendation).pack(pady=10)
        tk.Button(self.window, text="Predecir Calorías Futuras", command=self.show_prediction).pack(pady=10)
        
        # Sección: Generar reporte
        tk.Button(self.window, text="Generar Reporte PDF", command=self.generate_report_pdf).pack(pady=10)
    
    # --- Métodos ---
    def add_progress(self):
        new_row = {
            "appointment": self.appointment_var.get(),
            "weight": self.weight_var.get(),
            "measurements": self.measurements_var.get(),
            "calories": self.calories_var.get()
        }
        self.clients_info.add_client_progress(**new_row)
        messagebox.showinfo("Éxito", "Progreso registrado correctamente.")
    
    def update_rules(self):
        diet_type = self.diet_type_var.get()
        goal = self.goal_var.get()
        self.clients_info.add_client_rules(diet_type, goal)
        messagebox.showinfo("Éxito", "Reglas de dieta actualizadas.")
    
    def show_recommendation(self):
        client_rules = self.clients_info.get_client_rules()
        diet_plan = self.diet_recommender(client_rules)
        messagebox.showinfo("Dieta Recomendada", f"{diet_plan}")
    
    def show_prediction(self):
        predicted_calories = self.regression_model.predict_diet()
        messagebox.showinfo("Predicción de calorías", f"Calorías estimadas: {predicted_calories:.2f}")
    
    def generate_report_pdf(self):
        client_progress = self.clients_info.get_client_progress()
        generate_report(client_progress)
        messagebox.showinfo("Reporte", "Reporte PDF generado en 'reports/diet_report.pdf'")
    
    def run(self):
        self.window.mainloop()