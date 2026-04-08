from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import os
import service
import storage

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(__name__, template_folder=TEMPLATE_DIR)
app.secret_key = "@Ban021"

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
    
    return render_template("treinos.html", treinos=lista)

@app.route("/treino/forca")
def mostra_tipo_forca():
    lista = storage.carregar_treinos()
    
    tipo_procurado = "forca"
    filtrados =  service.filtrar(lista, lambda treinos: treinos["tipo"] == tipo_procurado)
    
    return render_template("treinos.html", treinos=filtrados)

@app.route("/add", methods=["POST", "GET"])
def add_treino():
    lista = storage.carregar_treinos()

    if request.method == "GET":
        return render_template("add_treinos.html")
    
    if request.method == "POST":
        data = request.form['data']
        tipo = request.form['tipo']
        duracao = request.form['duracao']
        descricao = request.form['descricao']

        valido, dados_ou_erros = service.validar_dados(data, tipo, duracao, descricao)

        if valido:
            lista.append(dados_ou_erros)
            storage.salvar_treinos(lista)
            flash("Treino adicionado com sucesso!")
            return redirect(url_for("lista_treinos"))
        else:
            flash("Dado(s) invalido(s)!")
            return redirect(url_for("add_treino"))
            




if __name__ == "__main__":
    app.run(debug=True)