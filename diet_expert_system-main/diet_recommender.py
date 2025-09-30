# diet_recommender.py
from typing import Dict, Any
import pandas as pd
from rules import get_diet_plan

def recommend_diet(client_rules: pd.DataFrame) -> Dict[str, Any]:
    client_rules = client_rules.iloc[0].to_dict()
    return get_diet_plan(client_rules['diet_type'], client_rules['goal'])