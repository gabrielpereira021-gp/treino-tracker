#lita de treinos
import json
import os
import storage
import service
from datetime import datetime

#criaçao alto de ficheiro e conexao com a lista
if os.path.exists("treinos.json"):
  with open("treinos.json", "r") as f:
    lista = json.load(f)
else:
  lista = []

# def para executar pos alteracao ao ficheiro json
def pos_alteração():
  storage.salvar_treinos(lista)
  resultado = service.alert(lista)
  if resultado:
    print(resultado)
  print("REALIZADO COM SUCESSO!")

# Funcao para manter a duracao sempre em numeros acima de 0
def pedir_duracao():
    while True:
        try:
           duracao = int(input("Digite a duração (min):"))
           if duracao > 0:
                return duracao
           else:
                print("A duração do treino tem de ser maior que 0!")
        except:
            print("Digite um número valido!")

# Funcao para manter a data sempre em um mesmo modelo
def pedir_data():
    while True:
        data = input("Data do treino (dd/mm/aaaa):")
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data
        except:
            print("Formato invalido! Tente novamente.")

#def para adicionar um novo treino
def adicionar_treino():
  data = pedir_data()
  tipo = input("Tipo do treino:")
  duracao = pedir_duracao()
  descricao = input("Descrição do treino:")

  treino = service.criar_treino(data, tipo, duracao, descricao)
  
  lista.append(treino)
  pos_alteração()

#def para listar todos os treinos adicionados
def listar_treinos():
  if len(lista) > 0:
    for treino in lista:
      service.mostrar_treino(treino)
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
      new_dur = input("insira a nova duração (ENTER para nao modificar):")
      if new_dur != "":
        treino["duracao"] = int(new_dur)
      new_desc = input("insira a nova descricao (ENTER para nao modificar):")
      if new_desc != "":
        treino["descricao"] = new_desc
      atualizado = True
      pos_alteração()
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
      pos_alteração()
    if not deletado:
      print("Nao há treinos com essa data!")
  else:
    print("Nao há treinos adicionados")

#def para procurar um treino pela data
def treinos_por_data(): 
  if len(lista) > 0:
    data_procurada = pedir_data()
    condicao = lambda treinos: treinos["data"] == data_procurada
    treinos = service.filtrar(lista, condicao)
    if treinos:
      for treino in treinos:
        service.mostrar_treino(treino)
    else:
      print("Nenhum treino encontrado com essa data!")
  else:
    print("Nenhum treino adicionado!")

#def para buscar todos os treinos de um tipo
def treinos_por_tipo():
  if len(lista) > 0:
    tipo_procurado = input("Digite o tipo de treino:")
    condicao = lambda treinos: treinos["tipo"] == tipo_procurado
    treinos = service.filtrar(lista, condicao)
    if treinos:
      for treino in treinos:
        service.mostrar_treino(treino)
    else:
      print("Nenhum treino encontrado com esse tipo!")
  else:
    print("Nenhum treino adicionado!")

#def para buscar treinos por duracao minima
def treinos_por_duracao():
  if len(lista) > 0:
    duracao_procurada = pedir_duracao()
    condicao = lambda treinos: treinos["duracao"] >= duracao_procurada
    treinos = service.filtrar(lista, condicao)
    if treinos:
      for treino in treinos:
        service.mostrar_treino(treino)
    else:
      print("Nenhum treino encontrado com essa duração!")
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
    print("_"*10)
    print("Treino mais longo:")
    for treino in lista:
      if treino["duracao"] == moretime:
        service.mostrar_treino(treino)
    print("treino mais curto:")
    for treino in lista:
      if treino["duracao"] == lesstime:
        service.mostrar_treino(treino)
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

def procurar_por_treinos():
  if len(lista) > 0:
    while True:
      print ("1 - Treinos por data")
      print ("2 - Treinos por tipo")
      print ("3 - Treinos por duração")
      print ("0 - Voltar")

      opcao = input("Digite a opção desejada:")

      if opcao == "1":
        print("-"*10, "Treinos por data", "-"*10)
        treinos_por_data()
      elif opcao == "2":
        print("-"*10, "Treinos por tipo", "-"*10)
        treinos_por_tipo()
      elif opcao == "3":
        print("-"*10, "Treinos por duração", "-"*10)
        treinos_por_duracao()
      elif opcao == "0":
        print("voltando ao menu principal...")
        break
      else:
        print("Opção indisponivel!")
  else:
    print("Não há treinos adicionados!")

# menu funcional
while True:
  print ("-"*10, "MENU", "-"*10)
  print ("1 - adicionar treino")
  print ("2 - listar treino")
  print ("3 - buscar por treinos")
  print ("4 - atualizar treino")
  print ("5 - deletar treino")
  print ("6 - estatisticas")
  print ("0 - sair")

  escolha = input("digiten sua escolha: ")

  if escolha == "1":
    print ("-"*10,"adicionar treino","-"*10)
    adicionar_treino()
  elif escolha == "2":
    print ("-"*10,"listar treino","-"*10)
    listar_treinos()
  elif escolha == "3":
    print ("-"*10,"buscar por treinos","-"*10)
    procurar_por_treinos()
  elif escolha == "4":
    print ("-"*10,"atualizar treino","-"*10)
    atualizar_treino()
  elif escolha == "5":
    print ("-"*10,"deletar treino","-"*10)
    deletar_treino()
  elif escolha == "6":
    print ("-"*10,"estatisticas","-"*10)
    estatistitcas()
  elif escolha == "0":
    print("saindo...")
    break
  else:
    print("opçao invalida")