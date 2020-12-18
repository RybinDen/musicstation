from flask import Blueprint, render_template, abort # flash, g, redirect, request, url_for
from jinja2 import TemplateNotFound
#from werkzeug.exceptions import abort

bp = Blueprint("youtube", __name__, url_prefix="/youtube")

@bp.route("/")
def index():
    return render_template("youtube/index.html", radio='my radio')

@bp.route("/create", methods=("GET", "POST"))
def create():
    return render_template("youtube/create.html")

