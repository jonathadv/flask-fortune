import random
from data import FORTUNES

from flask import Flask
app = Flask(__name__)


MAX_RAND_INT = len(FORTUNES)-1


@app.route("/")
def root():
    return FORTUNES[random.randint(0, MAX_RAND_INT)]


@app.route("/<string:id>")
def users(id):
    return FORTUNES[id]


@app.route("/about")
def about():
    return "Hello! This is Fortune! \o/"

