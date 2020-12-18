from flask import Blueprint, render_template, abort # flash, g, redirect, request, url_for
from jinja2 import TemplateNotFound
#from werkzeug.exceptions import abort

bp = Blueprint("podcast", __name__, url_prefix="/podcast")

@bp.route("/")
def index():
    return render_template("podcast/index.html")

@bp.route("/create", methods=("GET", "POST"))
def create():
    return render_template("podcast/create.html")

