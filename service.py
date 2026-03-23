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

def alert(lista):
    if len(lista) >= 3:
        ultimos = lista[-3:]
        datas = [datetime.strptime(t["data"], "%d/%m/%Y") for t in ultimos]
        dif1 = (datas[1] - datas[0]).days
        dif2 = (datas[2] - datas[1]).days
        if 0 <= dif1 <= 1 and 0 <= dif2 <= 1:
            return "Você treinou em dias muito próximos. Considere descansar!"
        return None
    return None
