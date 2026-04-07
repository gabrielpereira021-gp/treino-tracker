from flask import Flask, render_template
import os
import service
import storage

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(__name__, template_folder=TEMPLATE_DIR)

def pos_busca(lista, condicao):
    treinos = service.filtrar(lista, condicao)
    if treinos:
        resultado = ""
        for treino in treinos:
            resultado += service.formatar_treino(treino)
        return resultado
    else:
        return "Nenhum treino encontrado!"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/treino")
def lista_treinos():
    lista = storage.carregar_treinos()
    
    if lista:
        resultado = ""

        for treino in lista:
            resultado += service.formatar_treino(treino)

        return resultado
    else:
        return "Nao há treinos adicionados!"

@app.route("/treino/forca")
def mostra_tipo_forca():
    lista = storage.carregar_treinos()
    
    tipo_procurado = "forca"
    condicao =  lambda treinos: treinos["tipo"] == tipo_procurado
    retorno = pos_busca(lista, condicao)
    return retorno

if __name__ == "__main__":
    app.run(debug=True)