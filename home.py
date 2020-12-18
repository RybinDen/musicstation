from flask import Blueprint, render_template, make_response
from jinja2 import TemplateNotFound

bp = Blueprint("home", __name__, template_folder='templates')

@bp.route('/')
def index():
    return render_template('home.html')
@bp.route('/data')
def data():
    #return render_template('data.json'), {'Content-Type': 'application/json'}
    return render_template('playlist.m3u'), {'Content-Type': 'audio/x-mpegurl; charset=UTF-8'}
@bp.route('/download/<file>')
def download(file):
    resp = make_response('this is the content of my text file')
    resp.headers['Content-Type'] = 'text/plain;charset=UTF-8'
    resp.headers['Content-Disposition'] = 'attachment;filename=' + file
    return resp
@bp.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        return render_template('404.html'), 404
