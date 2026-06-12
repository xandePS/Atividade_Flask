# -*- coding: utf-8 -*-
"""
Rotas de API
Descrição: Rotas flask
Data: 03/06/2026
"""
__author__ = "Alexandre Pereira da Silva"
__email__ = "alexandre.silva12@aluno.cps.sp.gov.br"
__turma__ = "DSM - 2º Semestre"
__version__ = "0.1"

import re

from flask import Blueprint, jsonify, request

rotas_bp = Blueprint("rotas", __name__)

MENSAGENS_STATUS = {
    200: "Sucesso geral.",
    201: "Sucesso na criação.",
    400: "Erro do cliente (sintaxe).",
    401: "Falta autenticação.",
    404: "Recurso não encontrado.",
    500: "Erro no servidor.",
}

PRODUTOS = [
    {"id": 1, "nome": "Notebook Dell Inspiron 15", "preco": 4299.90},
    {"id": 2, "nome": "Mouse Logitech MX Master 3", "preco": 549.90},
    {"id": 3, "nome": "Teclado Mecânico Redragon K552", "preco": 289.00},
    {"id": 4, "nome": "Monitor LG UltraWide 29\"", "preco": 1599.00},
    {"id": 5, "nome": "Headset HyperX Cloud II", "preco": 499.90},
    {"id": 6, "nome": "SSD Samsung 1TB NVMe", "preco": 389.90},
    {"id": 7, "nome": "Webcam Logitech C920", "preco": 459.00},
    {"id": 8, "nome": "Roteador Wi-Fi 6 TP-Link Archer", "preco": 379.90},
    {"id": 9, "nome": "Tablet Samsung Galaxy Tab A9", "preco": 1199.00},
    {"id": 10, "nome": "Smartwatch Apple Watch SE", "preco": 2299.00},
]

LISTA_VAZIA = False


def _validar_cpf(cpf):
    cpf = re.sub(r"\D", "", cpf or "")
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(0, i))
        digito = (soma * 10 % 11) % 10
        if int(cpf[i]) != digito:
            return False
    return True


@rotas_bp.route("/message")
def message():
    return "Cadastro Salvo com sucesso"


@rotas_bp.route("/message/<status>")
def message_status(status):
    try:
        codigo = int(status)
    except ValueError:
        return "Recurso não encontrado.", 404
    if codigo not in MENSAGENS_STATUS:
        return "Recurso não encontrado.", 404
    return MENSAGENS_STATUS[codigo], codigo


@rotas_bp.route("/auth/login", methods=["POST"])
def auth_login():
    usuario = request.form.get("usuario", "")
    senha = request.form.get("senha", "")
    if usuario == "alexandre" and senha == "102030":
        return "OK", 200
    return "Unauthorized", 401


@rotas_bp.route("/cliente", methods=["POST"])
def cliente():
    nome = request.form.get("nome", "")
    cpf = request.form.get("cpf", "")
    if not nome or not cpf:
        return jsonify({"status": 400, "mensagem": "Erro do cliente (sintaxe)."}), 400
    if not _validar_cpf(cpf):
        return jsonify({"status": 400, "mensagem": "CPF Invalído."}), 400
    return jsonify({"status": 201, "mensagem": "Sucesso na criação."}), 201


@rotas_bp.route("/convert/celsius/<temp>")
def convert_celsius(temp):
    try:
        temp = float(temp)
    except ValueError:
        return jsonify({"erro": "Temperatura deve ser um número válido"}), 400
    fahrenheit = temp * 1.8 + 32
    return jsonify({"celsius": temp, "fahrenheit": fahrenheit}), 200


@rotas_bp.route("/search")
def search():
    q = request.args.get("q")
    if q is None or q.strip() == "":
        return "Parâmetro de busca obrigatório", 400
    return f"Você pesquisou por: {q}"


@rotas_bp.route("/api/register", methods=["POST"])
def api_register():
    dados = request.get_json(silent=True) or request.form
    nome = dados.get("nome", "")
    idade = dados.get("idade")
    try:
        idade = int(idade)
    except (TypeError, ValueError):
        return jsonify({"erro": "Erro do cliente (sintaxe)."}), 400
    if idade < 18:
        return jsonify({"erro": "Cadastro permitido apenas para maiores de idade"}), 403
    return jsonify({"mensagem": f"Usuário {nome} cadastrado"}), 201


@rotas_bp.route("/products")
def products():
    if LISTA_VAZIA:
        return "", 204
    return jsonify(PRODUTOS)


@rotas_bp.route("/admin/dashboard")
def admin_dashboard():
    api_key = request.headers.get("X-Api-Key")
    if api_key == "senhateste":
        return "Acesso ao painel administrativo liberado", 200
    return "Unauthorized", 401
