from datetime import datetime

def pedir_data():
    while True:
        data = input("Data do treino (dd-mm-aaaa):")
        try:
            datetime.strptime(data, "%d-%m-%Y")
            return data
        except:
            print("Formato invalido! Tente novamente.")

def criar_treino():
  data = pedir_data()
  print("adicione o tipo do treino")
  tipo = input("tipo:")
  print("adicione a duracao do treino")
  print("pf add apenas numeros")
  duracao = int(input("duracao:"))
  print("adicione uma descricao do treino")
  descricao = input("descricao:")
  treino = {
    "data": data, 
    "tipo": tipo, 
    "duracao": duracao, 
    "descricao": descricao
  }
  return treino

def mostrar_treino(treino):
    print(f"Data:", treino["data"])
    print(f"Tipo:", treino["tipo"])
    print(f"Duração:", treino["duracao"], "min")
    print(f"Descrição:", treino["descricao"])
    print("_"*10)