from flask import Flask
from .redirect_blueprint import redirect_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(redirect_bp)
    return app
