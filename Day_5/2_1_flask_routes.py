
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        return 'Hello from GET'
    if request.method == 'POST':
        return 'Hello from POST'


@app.route('/home/<name>')
def home(name):
    return f'Hello {name}!!!!'


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
