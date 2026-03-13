from flask import Flask, jsonify

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
    app.run(port=5001)