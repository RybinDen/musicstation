from flask import Blueprint, render_template, abort # flash, g, redirect, request, url_for
from jinja2 import TemplateNotFound
#from werkzeug.exceptions import abort

bp = Blueprint("player", __name__, url_prefix="/player")

@bp.route("/")
def index():
    return render_template("player/index.html")

@bp.route("/search", methods=("GET", "POST"))
def search():
    return render_template("player/create.html")

@bp.route("/radio/update/<int:id>", methods=("GET", "POST"))
def update(id):
    return render_template("player/update.html", post=post)

@bp.route("/radio/delete/<int:id>", methods=("POST",))
def delete(id):
    return redirect(url_for("player.index"))
