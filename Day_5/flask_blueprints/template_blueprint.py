from flask import Blueprint, render_template

template_blueprint = Blueprint('template_blueprint', __name__, url_prefix='/home')


@template_blueprint.route('/')
def index():
    return render_template('index.html', title='home')


@template_blueprint.route('/welcome/<name>')
def welcome(name):
    return render_template('welcome.html', name=name)
