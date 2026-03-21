from datetime import datetime

# Funcao para manter formato de data  sempre o mesmo
def pedir_data():
    while True:
        data = input("Data do treino (dd-mm-aaaa):")
        try:
            datetime.strptime(data, "%d-%m-%Y")
            return data
        except:
            print("Formato invalido! Tente novamente.")

# Funcao de criacao de treino separada do codigo principal
def criar_treino():
  data = pedir_data()
  tipo = input("Tipo do treino:")
  duracao = pedir_duracao()
  descricao = input("Descrição do treino:")
  treino = {
    "data": data, 
    "tipo": tipo, 
    "duracao": duracao, 
    "descricao": descricao
  }
  return treino

# Funcao para mostrar os treinos de melho forma no terminal
def mostrar_treino(treino):
    print(f"Data:", treino["data"])
    print(f"Tipo:", treino["tipo"])
    print(f"Duração:", treino["duracao"], "min")
    print(f"Descrição:", treino["descricao"])
    print("_"*10)

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