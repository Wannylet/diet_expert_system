# gui.py
import tkinter as tk
from tkinter import messagebox
from clients_info import ClientsInfo
from diet_recommender import recommend_diet
from regression_model import RegressionModel

class MainGUI():
    def __init__(self):
        # Inicializar datos
        self.clients_info = None
        self.client_progress = None
        self.client_rules = None
        self.diet_recommender = None
        self.regression_model = None

        # Inicializar ventana
        self.login_window = tk.Tk()
        self.login_window.title("Login - Sistema Experto de Dietas")
        self.login_window.geometry("350x200")

        # Variable para contraseña
        self.password_var = tk.StringVar()
        self.create_login_widgets()
    
    def run(self):
        self.login_window.mainloop()

    def create_login_widgets(self):
        tk.Label(self.login_window, text="Ingrese su contraseña", font=("Arial", 12)).pack(pady=20)
        tk.Entry(self.login_window, textvariable=self.password_var, show="*").pack(pady=5)
        tk.Button(self.login_window, text="Ingresar", command=self.login).pack(pady=5)
        tk.Button(self.login_window, text="Registrarse", command=self.open_registration_window).pack(pady=5)

    def login(self):
        password = self.password_var.get()
        self.clients_info = ClientsInfo(password)

        if self.clients_info.get_client_exist():
            self.login_window.destroy()
            #self.create_main_window()
        else:
            messagebox.showwarning("Error", "Cliente no encontrado. Regístrese primero.")

    def open_registration_window(self):
        reg_win = tk.Toplevel(self.login_window)
        reg_win.title("Registro de Cliente")
        reg_win.geometry("400x650")

        # ---- Datos de acceso y reglas ----
        tk.Label(reg_win, text="Nueva Contraseña:").pack(pady=5)
        new_pass_var = tk.StringVar()
        tk.Entry(reg_win, textvariable=new_pass_var, show="*").pack(pady=5)

        tk.Label(reg_win, text="Tipo de dieta:").pack(pady=5)
        diet_var = tk.StringVar()
        tk.Entry(reg_win, textvariable=diet_var).pack(pady=5)

        tk.Label(reg_win, text="Objetivo:").pack(pady=5)
        goal_var = tk.StringVar()
        tk.Entry(reg_win, textvariable=goal_var).pack(pady=5)

        # ---- Primer progreso ----
        tk.Label(reg_win, text="Cree su primer progreso", font=("Arial", 12, "bold")).pack(pady=10)

        tk.Label(reg_win, text="Cita (YYYY-MM-DD):").pack(pady=5)
        appointment_var = tk.StringVar()
        tk.Entry(reg_win, textvariable=appointment_var).pack(pady=5)

        tk.Label(reg_win, text="Peso (kg):").pack(pady=5)
        weight_var = tk.DoubleVar()
        tk.Entry(reg_win, textvariable=weight_var).pack(pady=5)

        tk.Label(reg_win, text="Medidas (cm):").pack(pady=5)
        measurements_var = tk.DoubleVar()
        tk.Entry(reg_win, textvariable=measurements_var).pack(pady=5)

        tk.Label(reg_win, text="Calorías actuales:").pack(pady=5)
        calories_var = tk.DoubleVar()
        tk.Entry(reg_win, textvariable=calories_var).pack(pady=5)
        
        # ---- Botón de registro ----
        def register_client():
            password = new_pass_var.get()

            diet_type = diet_var.get()
            goal = goal_var.get()

            appointment = appointment_var.get()
            weight = weight_var.get()
            measurements = measurements_var.get()
            calories = calories_var.get()

            self.create_data(password, diet_type, goal, appointment, weight, measurements, calories)

            messagebox.showinfo("Registro exitoso", "Cliente registrado correctamente")
            reg_win.destroy()

        tk.Button(reg_win, text="Registrar", command=register_client).pack(pady=15)

    def instaciate_data(self, password):
        self.clients_info = ClientsInfo(password)

        self.client_progress = self.clients_info.get_client_progress()
        self.client_rules = self.clients_info.get_client_rules
        self.diet_recommender = recommend_diet(self.client_rules)
        self.regression_model = RegressionModel(self.client_progress)

    def create_data(self, password, diet_type, goal, appointment, weight, measurements, calories):
        self.clients_info = ClientsInfo(password)

        self.clients_info.add_client_rules(
            diet_type=diet_type,
            goal=goal
        )
        
        self.clients_info.add_client_progress(
            appointment=appointment,
            weight=weight,
            measurements=measurements,
            calories=calories
        )

        self.client_progress = self.clients_info.get_client_progress()
        self.client_rules = self.clients_info.get_client_rules()
        self.diet_recommender = recommend_diet(self.client_rules)
        self.regression_model = RegressionModel(self.client_progress)