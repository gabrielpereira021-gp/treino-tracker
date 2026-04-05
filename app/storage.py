import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAMINHO = os.path.join(BASE_DIR, "data", "treinos.json")

def carregar_treinos():
    if os.path.exists(CAMINHO):
        with open(CAMINHO, "r") as f:
            return json.load(f)
    else:
        return []

def salvar_treinos(lista):
    with open(CAMINHO, "w") as f:
        json.dump(lista, f, indent=4)
