# app.py
from gui.gui import DietExpertGUI
from client_progress import ClientProgress
from diet_recommender import recommend_diet
from regression_model import RegressionModel

def main():
    # Crear instancias de los diferentes módulos
    client_data = ClientProgress()
    diet_recommender = recommend_diet()
    regression_model = RegressionModel()
    # Lanzar la interfaz gráfica
    gui = DietExpertGUI(client_data, diet_recommender, regression_model)
    gui.run()

if __name__ == "__main__":
    main()