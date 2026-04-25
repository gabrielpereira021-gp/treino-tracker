from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, make_response
from dotenv import load_dotenv
import os
import service
import storage

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(__name__, template_folder=TEMPLATE_DIR)
app.secret_key = os.getenv("SECRET_KEY")

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

    ordem = request.args.get("ordem", "desc")

    if ordem == "asc":
        lista = service.organizar_por_data(lista)
    else:
        lista = list(reversed(service.organizar_por_data(lista)))
    
    return render_template("treinos.html", treinos=lista)

@app.route("/add", methods=["POST", "GET"])
def add_treino():
    lista = storage.carregar_treinos()

    if request.method == "GET":
        response = make_response(render_template("add_treinos.html"))
        response.headers["Cache-Control"] = "no-cache, no-store, must-revaliedade"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response
    
    if request.method == "POST":
        data = request.form['data']
        tipo = request.form['tipo']
        duracao = request.form['duracao']
        descricao = request.form['descricao']

        valido, dados_ou_erros = service.validar_dados(data, tipo, duracao, descricao, id = None)

        if valido:
            lista.append(dados_ou_erros)
            storage.salvar_treinos(lista)
            flash("Treino adicionado com sucesso!")
            return redirect(url_for("lista_treinos"))
        else:
            flash("Dado(s) invalido(s)!")
            return redirect(url_for("add_treino"))

@app.route("/del/<id>", methods=["POST"])
def deletar_treino(id):
    lista = storage.carregar_treinos()

    lista = service.del_treino(lista, id)
    storage.salvar_treinos(lista)
    return redirect(url_for("lista_treinos"))

@app.route("/edit/<id>", methods=["POST", "GET"])
def edit_treino_app(id):
    lista = storage.carregar_treinos()

    if request.method == "GET":
        for treino in lista:
            if treino["id"] == id:
                from datetime import datetime
                treino_edit = dict(treino)  # copia para não alterar o original
                treino_edit["data"] = datetime.strptime(treino["data"], "%d/%m/%Y").strftime("%Y-%m-%d")
                return render_template("edit.html", treino=treino_edit)

    if request.method == "POST":
        data = request.form['data']
        tipo = request.form['tipo']
        duracao = request.form['duracao']
        descricao = request.form['descricao']

        valido, dados_ou_erros = service.validar_dados(data, tipo, duracao, descricao, id)

        if valido:
            lista = service.edit_treino(lista, id, dados_ou_erros)
            storage.salvar_treinos(lista)
            flash("Treino editado com sucesso!")
            return redirect(url_for("lista_treinos"))
        else:
            flash("Dado(s) invalido(s)!")
            return redirect(url_for("add_treino"))

if __name__ == "__main__":
    app.run(debug=True)
