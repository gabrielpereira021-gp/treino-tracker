#lita de treinos
import json
import os
import utils
from datetime import datetime

#criaçao alto de ficheiro e conexao com a lista
if os.path.exists("treinos.json"):
  with open("treinos.json", "r") as f:
    lista = json.load(f)
else:
  lista = []

#def para adicionar um novo treino
def adicionar_treino():
  treino = utils.criar_treino()
  lista.append(treino)
  with open("treinos.json", "w") as f:
    json.dump(lista, f, indent=4)
  print("treino adicionado com sucesso!")

#def para procurar um treino pela data
def procurar_treino():
  if len(lista) > 0:
    data_procurada = input("Digite a data (dd-mm-aaaa):")
    encontrado = False
    for treino in lista:
      if treino["data"] == data_procurada:
        print("Data:", treino["data"])
        print("Tipo:", treino["tipo"]) 
        print("Duracao:", treino["duracao"])
        print("descricao", treino["descricao"])
        encontrado = True
    if not encontrado:
      print("nenhum treino encontrado com essa data.")
  else:
    print("Nenhum treino adicionado!")

#def para listar todos os treinos adicionados
def listar_treinos():
  if len(lista) > 0:
    print(lista)
  else:
    print("Nao há treinos adicionados!")

#def para fazer a atualizacao de infomacoes do treino
def atualizar_treino():
  if len(lista) > 0:
    tr_az = input("Digite a data do treino:")
    atualizado = False
    for treino in lista:
      treino["data"] == tr_az
      new_data = input("insira a nova data (ENTER para nao modificar):")
      if new_data != "":
        treino["data"] = new_data
      new_type = input("insira a novo tipo (ENTER para nao modificar):")
      if new_type != "":
        treino["tipo"] = new_type
      new_dur = input("insira a nova duracao (ENTER para nao modificar):")
      if new_dur != "":
        treino["duracao"] = int(new_dur)
      new_desc = input("insira a nova descricao (ENTER para nao modificar):")
      if new_desc != "":
        treino["descricao"] = new_desc
      atualizado = True
      with open("treinos.json", "w") as f:
        json.dump(lista, f, indent=4)
      print("treino adicionado com sucesso!")
    if not atualizado:
      print("Nenhum treino com essa data")
  else:
    print("Nao há treinos adicionados!")

#def para deletar treinos
def deletar_treino():
  if len(lista) > 0:
    print("Digite a data do treino que deseja deletar:")
    del_t = input("dd-mm-aaaa:")
    deletado = False 
    for treino in lista:
      if treino["data"] == del_t:
        lista.remove(treino)
        deletado = True
      with open("treinos.json", "w") as f:
        json.dump(lista, f, indent=4)
      print("treino deletado com sucesso!")
    if not deletado:
      print("Nao há treinos com essa data!")
  else:
    print("Nao há treinos adicionados")

#def para buscar todos os treinos de um tipo
def buscar_tipo():
  if len(lista) > 0:
    tipo_procurado = input("Digite o tipo de treino:")
    encontrado = False
    for treino in lista:
      if treino["tipo"] == tipo_procurado:
        print("Data:", treino["data"])
        print("Tipo:", treino["tipo"]) 
        print("Duracao:", treino["duracao"])
        print("descricao", treino["descricao"])
        print("_"*30)
        encontrado = True
    if not encontrado:
      print("nenhum treino encontrado deste tipo.")
  else:
    print("Nenhum treino adicionado!")

#def para buscar treinos por duracao minima
def buscar_duracao():
  if len(lista) > 0:
    duracao_procurada = int(input("Digite a duracao minima:"))
    encontrado = False
    for treino in lista:
      if treino["duracao"] >= duracao_procurada:
        print("Data:", treino["data"])
        print("Tipo:", treino["tipo"]) 
        print("Duracao:", treino["duracao"])
        print("descricao", treino["descricao"])
        print("_"*30)
        encontrado = True
    if not encontrado:
      print("nenhum treino encontrado deste tipo.")
  else:
    print("Nenhum treino adicionado!")
  
#def para as estatisticas de treinos
def estatistitcas():
  if len(lista) > 0:
    total = len(lista)
    duracoes = [treino["duracao"] for treino in lista]
    total_time = sum(duracoes)
    len_time = len(duracoes)
    moretime = max(duracoes)
    lesstime = min(duracoes)
    media_time = total_time/len_time
    print("Total de treinos:", total)
    print("Tempo total treinado", total_time, "min")
    print("Duracao média:", f"{media_time:.2f}", "min")
    print("Treino mais longo:")
    for treino in lista:
      if treino["duracao"] == moretime:
        print("Data:", treino["data"])
        print("Tipo:", treino["tipo"]) 
        print("Duracao:", treino["duracao"])
        print("descricao", treino["descricao"])
        print("_"*30)
    print("treino mais curto:")
    for treino in lista:
      if treino["duracao"] == lesstime:
        print("Data:", treino["data"])
        print("Tipo:", treino["tipo"]) 
        print("Duracao:", treino["duracao"])
        print("descricao", treino["descricao"])
        print("_"*30)
    print("Tipo de treino:") 
    tipos = [treino["tipo"] for treino in lista]
    contagem = {}
    for tipo in tipos:
      if tipo in contagem:
        contagem[tipo] += 1
      else:
        contagem[tipo] = 1
    moretype = max(contagem.values())
    print(contagem)
    print("Tipo mais frequente:")
    for tipo in contagem:
      if contagem[tipo] == moretype:
        print(tipo)
    
      
  else:
    print("Nao há treinos adicionados!")

# menu funcional
while True:
  print ("1 - adicionar treino")
  print ("2 - buscar treino por data")
  print ("3 - listar treino")
  print ("4 - atualizar treino")
  print ("5 - deletar treino")
  print ("6 - buscar treino por tipo")
  print ("7 - buscar treino por duracao")
  print ("8 - estatisticas")
  print ("0 - sair")

  escolha = input("digiten sua escolha: ")

  if escolha == "1":
    print ("-"*10,"adicionar treino","-"*10)
    adicionar_treino()
  elif escolha == "2":
    print ("-"*10,"procurar treino","-"*10)
    procurar_treino()
  elif escolha == "3":
    print ("-"*10,"listar treino","-"*10)
    listar_treinos()
  elif escolha == "4":
    print ("-"*10,"atualizar treino","-"*10)
    atualizar_treino()
  elif escolha == "5":
    print ("-"*10,"deletar treino","-"*10)
    deletar_treino()
  elif escolha == "6":
    print ("-"*10,"buscar treino por tipo","-"*10)
    buscar_tipo()
  elif escolha == "7":
    print ("-"*10,"buscar treino por duracao","-"*10)
    buscar_duracao()
  elif escolha == "8":
    print ("-"*10,"estatisticas","-"*10)
    estatistitcas()
  elif escolha == "0":
    print("saindo...")
    break
  else:
    print("opçao invalida")