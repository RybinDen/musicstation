#https://flask.palletsprojects.com/en/1.1.x/tutorial/
import os
from flask import Flask
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev", DATABASE=os.path.join(app.instance_path, "musicstation.sqlite"))
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from musicstation import db
    db.init_app(app)

    from musicstation import home, radio, podcast, player, youtube
    app.register_blueprint(home.bp)
    app.register_blueprint(radio.bp)
    app.register_blueprint(podcast.bp)
    app.register_blueprint(player.bp)
    app.register_blueprint(youtube.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")
    return app
