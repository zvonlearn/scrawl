import os

from flask import Flask
from . import pages


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        PAGESPATH = './texts' #todo: ask user for path
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(pages.bp)
    app.add_url_rule('/', endpoint='index')

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
