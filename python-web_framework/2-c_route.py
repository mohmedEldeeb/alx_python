""" This module creates a flask web application """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes = False)
def sayHello():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes = False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes = False)
def pramText(text):
    res = 'C {}'.format(text.replace('_', ' '))
    return res

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)