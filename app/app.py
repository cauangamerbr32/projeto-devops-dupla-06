import os
from flask import Flask, jsonify

# ===== VARIAÇÃO DA DUPLA (mude estes valores) =====
NOME_DUPLA = "dupla-06"
MENSAGEM = "Olá, Dupla-06"
PORTA = 5006
# ==================================================

VERSAO = os.environ.get("APP_VERSION", "v1")
app = Flask(__name__)


@app.route("/saude")
def saude():
    return jsonify(status="ok", versao=VERSAO)


@app.route("/aluno")
def aluno():
    return jsonify(dupla=NOME_DUPLA, mensagem=MENSAGEM)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORTA)
