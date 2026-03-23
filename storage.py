import json
import os
from datetime import datetime



def salvar_treinos(lista):
    with open("treinos.json", "w") as f:
        json.dump(lista, f, indent=4)
