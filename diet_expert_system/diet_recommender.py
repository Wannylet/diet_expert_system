# diet_recommender.py
from rules import get_diet_plan

def recommend_diet(client_info):
    # Basado en la información del cliente, devolver un plan de dieta
    diet_plan = get_diet_plan(client_info['diet_type'],
    client_info['goal'])
    return diet_plan