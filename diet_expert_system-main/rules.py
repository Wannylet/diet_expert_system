# rules.py}
from typing import Dict

def get_diet_plan(diet_type: str, goal: str) -> Dict[str, int]:
    # Reglas basadas en el tipo de dieta y objetivo
    if diet_type == "vegetariano" and goal == "pérdida de peso":
        return {
            "calories": 1500,
            "protein": 60,
            "carbs": 200,
            "fats": 50
            }
    elif diet_type == "bajo en carbohidratos" and goal == "aumento muscular":
        return {
            "calories": 2500,
            "protein": 100,
            "carbs": 150,
            "fats": 80
        }
        # Añadir más reglas según necesidades