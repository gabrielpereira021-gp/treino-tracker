import json
import os
from datetime import datetime

def carregar_treinos():
    if os.path.exists("treinos.json"):
        with open("treinos.json", "r") as f:
            return json.load(f)
    else:
        return []

def salvar_treinos(lista):
    with open("treinos.json", "w") as f:
        json.dump(lista, f, indent=4)
