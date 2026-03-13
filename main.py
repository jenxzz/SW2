from flask import Flask, jsonify
import os

app = Flask(__name__)

jogos = [
    {"id": 1, "nome": "God of War"},
    {"id": 2, "nome": "Super Bomberman"},
    {"id": 3, "nome": "Beyound Two Souls"},
]

@app.route("/jogos", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de Jogos - Acesse /jogos"})

@app.route("/", methods=["GET"])
def listar_jogos():
    return jsonify(jogos)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)