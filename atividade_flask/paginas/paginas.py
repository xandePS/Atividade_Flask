# -*- coding: utf-8 -*-
"""
Título: Rotas de Páginas
Descrição: Rotas HTML com templates
Data: 03/06/2026
"""
__author__ = "Alexandre Pereira da Silva"
__email__ = "alexandre.silva12@aluno.cps.sp.gov.br"
__turma__ = "DSM - 2º Semestre"
__version__ = "0.1"

from flask import Blueprint, render_template

paginas_bp = Blueprint(
    "paginas",
    __name__,
    template_folder="../templates/paginas",
)


@paginas_bp.route("/")
def home():
    return render_template("index.html", title="Início")
