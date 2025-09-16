# gui.py
import tkinter as tk
from tkinter import messagebox
from clients_info import ClientsInfo
from diet_recommender import recommend_diet
from regression_model import RegressionModel
from diet_chart import generate_report

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
            self.instaciate_data(password)
            self.login_window.destroy()
            self.create_main_window()
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

    def create_main_window(self):
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
        
        self.create_main_widgets()
        self.window.mainloop()

    def create_main_widgets(self):
        # Sección: Datos de cliente
        tk.Label(self.window, text="Ingrese sus datos de progreso", font=("Arial", 14)).pack(pady=10)
        
        form_frame = tk.Frame(self.window)
        form_frame.pack(pady=5)
        
        tk.Label(form_frame, text="Cita (YYYY-MM-DD):").grid(row=0, column=0, sticky="e")
        tk.Entry(form_frame, textvariable=self.appointment_var).grid(row=0, column=1)
        
        tk.Label(form_frame, text="Peso (kg):").grid(row=1, column=0, sticky="e")
        tk.Entry(form_frame, textvariable=self.weight_var).grid(row=1, column=1)
        
        tk.Label(form_frame, text="Medidas (cm):").grid(row=2, column=0, sticky="e")
        tk.Entry(form_frame, textvariable=self.measurements_var).grid(row=2, column=1)
        
        tk.Label(form_frame, text="Calorías actuales:").grid(row=3, column=0, sticky="e")
        tk.Entry(form_frame, textvariable=self.calories_var).grid(row=3, column=1)
        
        tk.Button(self.window, text="Registrar Progreso", command=self.add_progress).pack(pady=10)
        
        # Sección: Reglas de dieta
        tk.Label(self.window, text="Reglas de dieta", font=("Arial", 14)).pack(pady=10)
        rules_frame = tk.Frame(self.window)
        rules_frame.pack(pady=5)

        # Obtener las reglas del cliente
        client_rules = self.clients_info.get_client_rules()
        if not client_rules.empty:
            rules = client_rules.iloc[-1]  # Tomar la última fila
            diet_type = rules['diet_type']
            goal = rules['goal']
        else:
            diet_type = "No disponible"
            goal = "No disponible"

        # Mostrar las reglas como labels
        tk.Label(rules_frame, text=f"Tipo de dieta: {diet_type}", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=2)
        tk.Label(rules_frame, text=f"Objetivo: {goal}", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=2)
        
        # Sección: Recomendación y predicción
        tk.Button(self.window, text="Recomendar Dieta", command=self.show_recommendation).pack(pady=10)
        tk.Button(self.window, text="Predecir Calorías Futuras", command=self.show_prediction).pack(pady=10)
        
        # Sección: Generar reporte
        tk.Button(self.window, text="Generar Reporte PDF", command=self.generate_report_pdf).pack(pady=10)

    def add_progress(self):
        a = self.appointment_var.get()
        b = self.weight_var.get()
        c = self.measurements_var.get()
        d = self.calories_var.get()
        
        self.clients_info.add_client_progress(a, b, c, d)
        messagebox.showinfo("Éxito", "Progreso registrado correctamente.")

    def show_recommendation(self):
        client_rules = self.clients_info.get_client_rules()
        diet_plan = recommend_diet(client_rules)
        
        # Construir mensaje amigable
        if diet_plan:
            msg = (
                f"Dieta Recomendada:\n\n"
                f"Calorías: {diet_plan.get('calories', 'N/A')} kcal\n"
                f"Proteínas: {diet_plan.get('protein', 'N/A')} g\n"
                f"Carbohidratos: {diet_plan.get('carbs', 'N/A')} g\n"
                f"Grasas: {diet_plan.get('fats', 'N/A')} g"
            )
        else:
            msg = "No se encontró una dieta adecuada para las reglas actuales del cliente."
    
        messagebox.showinfo("Dieta Recomendada", msg)
    
    def show_prediction(self):
        self.regression_model = RegressionModel(self.client_progress)
        self.regression_model.train_model()
        
        predicted_calories = self.regression_model.predict_diet()

        messagebox.showinfo("Predicción de calorías", f"Calorías estimadas: {predicted_calories:.2f}")
    
    def generate_report_pdf(self):
        client_progress = self.clients_info.get_client_progress()
        generate_report(client_progress)
        messagebox.showinfo("Reporte", "Reporte PDF generado en 'diet_expert_system/reports'")

    def instaciate_data(self, password):
        self.clients_info = ClientsInfo(password)

        self.client_progress = self.clients_info.get_client_progress()
        self.client_rules = self.clients_info.get_client_rules()
        self.diet_recommender = recommend_diet(self.client_rules)
        self.regression_model = RegressionModel(self.client_progress)
        self.regression_model.train_model()


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
        self.regression_model.train_model()