import json
import os
from datetime import datetime

# Funcao de criacao de treino separada do codigo principal
def criar_treino(data_formatada, tipo, duracao_validada, descricao):
    if not tipo:
        raise ValueError("É nescessario ter um tipo valido, ex (força, tecnica, corrida...)")
    if duracao_validada <= 0:
        raise ValueError("A duração tem que ser um número positivo.")

    return {
        "data": data_formatada, 
        "tipo": tipo, 
        "duracao": duracao_validada, 
        "descricao": descricao
    }

# Função de alerta de descanso a cada 3 dias consecutivos
def alert(lista):
    if len(lista) >= 3:
        ordenados = organizar_por_data(lista)
        ultimos = ordenados[-3:]
        datas = [datetime.strptime(t["data"], "%d/%m/%Y") for t in ultimos]
        dif1 = (datas[1] - datas[0]).days
        dif2 = (datas[2] - datas[1]).days
        if 0 <= dif1 <= 1 and 0 <= dif2 <= 1:
            return "Você treinou em dias muito próximos. Considere descansar!"
        return None
    return None

#função para organizacao da lista por data
def organizar_por_data(lista):
    return sorted(
        lista,
        key=lambda t: datetime.strptime(t["data"], "%d/%m/%Y")
    )
    
#def de procura global
def filtrar(lista, condicao):
    treinos_found = []

    for treinos in lista:
        if condicao(treinos):
            treinos_found.append(treinos)
    return treinos_found

def validar_data(data):
    try:
        data_obj = datetime.strptime(data, "%Y-%m-%d")
        data_formatada = data_obj.strftime("%d/%m/%Y")
        return data_formatada
    except:
        return None

def validar_duracao(duracao):
    try:
        duracao_num = float(duracao)
        if duracao_num > 0:
            return duracao_num
        else:
            return None
    except:
        return None

def validar_dados(data, tipo, duracao, descricao):
    erros = []

    data_formatada = validar_data(data)
    if not data_formatada:
        erros.append("Data inválida")
    duracao_validada = validar_duracao(duracao)
    if not duracao_validada:
        erros.append("Duração inválida")
    if not tipo:
        erros.append("Tipo inválido")
    
    if erros:
        return False, erros
    return True, criar_treino(data_formatada, tipo, duracao_validada, descricao)