from flask import Blueprint, render_template, request, redirect

redirect_bp = Blueprint('redirect_bp', __name__)


@redirect_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        username = request.form.get("username")
        return render_template('welcome.html', username=username)


@redirect_bp.route('/new', methods=['POST'])
def new():
    if request.method == 'POST':
        return redirect('/')
