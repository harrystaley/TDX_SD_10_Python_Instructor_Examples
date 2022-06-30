from flask import Blueprint

test_blueprint = Blueprint('test_blueprint', __name__)


@test_blueprint.route('/')
def index():
    return 'Hello world!!!'


@test_blueprint.route('/hello/<name>')
def hello(name):
    return f'Hello {name}!!!!'
