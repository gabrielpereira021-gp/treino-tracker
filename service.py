import json
import os
import storage
from datetime import datetime

# Funcao de criacao de treino separada do codigo principal
def criar_treino(data, tipo, duracao, descricao):
    if not tipo:
        raise ValueError("É nescessario ter um tipo valido, ex (força, tecnica, corrida...)")
    if duracao <= 0:
        raise ValueError("A duração tem que ser um número positivo.")

    return {
        "data": data, 
        "tipo": tipo, 
        "duracao": duracao, 
        "descricao": descricao
    }

# Funcao para mostrar os treinos de melho forma no terminal
def mostrar_treino(treino):
    print(f"Data:", treino["data"])
    print(f"Tipo:", treino["tipo"])
    print(f"Duração:", treino["duracao"], "min")
    print(f"Descrição:", treino["descricao"])
    print("_"*10)

