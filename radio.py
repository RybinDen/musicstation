from flask import Blueprint, jsonify, render_template, request, make_response # flash, g, redirect, url_for
from jinja2 import TemplateNotFound
from pyradios import RadioBrowser
import subprocess

bp = Blueprint("radio", __name__, url_prefix="/radio")

@bp.route("/")
def index():
    rb = RadioBrowser()
    countStation = rb.countries('ru') # количество станций  по коду страны
    response = rb.stations_by_countrycode('ru',order='clickcount', limit=20)
    return render_template("radio/index.html", countStation = countStation[0]['stationcount'])

# счетчик кликов по станции
@bp.route('/click')
def click():
    stationuuid = request.args.get('stationuuid')
    rb = RadioBrowser()
    response = rb.click_counter(stationuuid)
    p = subprocess.Popen(["C:/Program Files/VideoLAN/VLC/vlc.exe", response['url'], '--play-and-exit'])
    return jsonify(response)

@bp.route("/search", methods=("GET", "POST"))
def search():
    name = request.form.get('name')
    rb = RadioBrowser()
    response = rb.search(name=name, limit=5)
    return jsonify(data=response)
@bp.route("/load")
def load():
    limit = 20  # num posts to return per request
    if request.args:
        offset = int(request.args.get("c"))
        rb = RadioBrowser()
        countStation = rb.countries('ru') # количество станций  по коду страны
        response = rb.stations_by_countrycode('ru',order='clickcount', offset=offset, limit=limit)
        counter = int(request.args.get("c")) # количество загруженных станций, возвращается с параметром
        if counter == 0:
            print(f"Returning posts 0 to {limit}")
            res = make_response(jsonify(response), 200) # выбрать записи 0 -> limit
        elif counter == countStation[0]['stationcount']:
            print("No more radiostations")
            res = make_response(jsonify({}), 200)
        else:
            print(f"Returning posts {counter} to {counter + limit}")
            res = make_response(jsonify(response), 200) # Slice counter -> limit from the db
    return res
#request.data Contains the incoming request data as string in case it came with a mimetype Flask does not handle.
# request.args: the key/value pairs in the URL query string
# request.form: the key/value pairs in the body, from a HTML post form, or JavaScript request that isn't JSON encoded
# request.files: the files in the body, which Flask keeps separate from form. HTML forms must use enctype=multipart/form-data or files will not be uploaded.
# request.values: combined args and form, preferring args if keys overlap
# request.json: parsed JSON data. The request must have the application/json content type, or use request.get_json(force=True) to ignore the content type.
#All of these are MultiDict instances (except for json). You can access values using:
# request.form['name']: use indexing if you know the key exists
# request.form.get('name'): use get if the key might not exist
# request.form.getlist('name'): use getlist if the key is sent multiple times and you want a list of values. get only returns the first value.
