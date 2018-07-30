import random
from fortune.data import FORTUNES
from .response_factory import create_response
from flask import Flask, render_template

app = Flask(__name__)

MAX_RAND_INT = len(FORTUNES) - 1


@app.route('/<rtype>')
@app.route('/', defaults={'rtype': 'html'})
def root(rtype):
    index = random.randint(0, MAX_RAND_INT)
    message = FORTUNES[index]
    permalink = str(index)

    resp = create_response(rtype=rtype, message=message, permalink=permalink)
    return resp


@app.route('/<int:id_>/<rtype>')
@app.route('/<int:id_>/', defaults={'rtype': 'html'})
def users(id_, rtype):
    message = FORTUNES[id_]
    resp = create_response(rtype=rtype, message=message, permalink=id_)
    return resp


@app.route('/about')
def about():
    message = 'Hello! This is Fortune! \o/'
    return render_template('index.html', message=message, permalink='about')
