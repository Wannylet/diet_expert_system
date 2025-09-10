# app.py
from gui.gui import DietExpertGUI
from client_progress import ClientProgress
from diet_recommender import recommend_diet
from regression_model import RegressionModel

def main():
    # Crear instancias de los diferentes módulos
    client_data = ClientProgress()
    client_info = {"diet_type": "vegetariano", "goal": "pérdida de peso"}
    diet_recommender = recommend_diet(client_info)
    regression_model = RegressionModel()
    # Lanzar la interfaz gráfica
    gui = DietExpertGUI(client_data, diet_recommender, regression_model)
    gui.run()

if __name__ == "__main__":
    main()