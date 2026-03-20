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