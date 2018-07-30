import random
from fortune.data import FORTUNES
from .response_factory import create_response
from flask import Flask

app = Flask(__name__)

MAX_RAND_INT = len(FORTUNES) - 1


@app.route('/<rtype>')
@app.route('/', defaults={'rtype': 'html'})
def root(rtype):
    index = random.randint(0, MAX_RAND_INT)
    message = FORTUNES[index]
    permalink = str(index)
    return create_response(rtype=rtype, message=message, permalink=permalink)


@app.route('/<int:id_>/<rtype>')
@app.route('/<int:id_>/', defaults={'rtype': 'html'})
def users(id_, rtype):
    message = FORTUNES[id_]
    return create_response(rtype=rtype, message=message, permalink=id_)


@app.route('/about', defaults={'rtype': 'html'})
@app.route('/about/<rtype>')
def about(rtype):
    message = 'Hello! This is Fortune! \o/'
    return create_response(rtype=rtype, message=message, permalink='about')

