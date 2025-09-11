# app.py
from gui.gui import DietExpertGUI
from clients_info import ClientsInfo
from diet_recommender import recommend_diet
from regression_model import RegressionModel

def main():
    # Crear instancias de los diferentes módulos --
    
    # Cargar archivo con progresos de clientes e instanciar un objeto con DataFrame del cliente actual
    clients_info = ClientsInfo()

    client_progress = clients_info.get_client_progress()
    client_rules = clients_info.get_client_rules()

    # REGISTROS HARDCODEADOS (de prueba)
    clients_info.add_client_progress(
        appointment="2025-09-11",
        weight=70.5,
        measurements=95,
        calories=1800
    )

    clients_info.add_client_rules(
        diet_type="vegetariano",
        goal="pérdida de peso"
    )    

    # Instanciar un objeto con dieta recomendada acorde a reglas
    diet_recommender = recommend_diet(client_rules)
    regression_model = RegressionModel(client_progress)

    # Lanzar la interfaz gráfica
    gui = DietExpertGUI(clients_info, diet_recommender, regression_model)
    gui.run()

if __name__ == "__main__":
    main()