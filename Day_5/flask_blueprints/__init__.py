from flask import Flask
from .test_blueprint import test_blueprint
from .template_blueprint import template_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(test_blueprint)
    app.register_blueprint(template_blueprint)
    return app
