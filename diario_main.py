def adicionar_treino():
    print("adicione a data do seu terino")
    data = int(input("data:"))
    print("adicione o tipo do treino")
    tipo = input("tipo:")
    print("adicione a duracao do treino")
    duracao = int(input("duracao:"))
    print("adicione uma descricao do treino")
    descricao = input("descricao:")
    treino = {"data": data, "tipo": tipo, "duracao": duracao, "descricao": descricao}
    treinos.append(treino) 
