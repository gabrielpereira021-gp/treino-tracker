from datetime import datetime

def pedir_data():
    while True:
        data = input("Data do treino (dd-mm-aaaa):")
        try:
            datetime.strptime(data, "%d-%m-%Y")
            return data
        except:
            print("Formato invalido! Tente novamente.")
