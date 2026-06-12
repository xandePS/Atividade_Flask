# -*- coding: utf-8 -*-
"""
Aplicação Flask - Exercícios
-- Inicializa o Flask e registra os blueprints de rotas e páginas
Data: 09/06/2026
"""
__author__ = "Alexandre Pereira da Silva"
__email__ = "alexandre.silva12@aluno.cps.sp.gov.br"
__turma__ = "DSM - 2º Semestre"
__version__ = "0.1"

from flask import Flask

from paginas.paginas import paginas_bp
from rotas.rotas import rotas_bp

app = Flask(__name__)
app.register_blueprint(rotas_bp)
app.register_blueprint(paginas_bp)

if __name__ == "__main__":
    app.run(debug=True)
