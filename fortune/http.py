import random
from data import FORTUNES

from flask import Flask, render_template

app = Flask(__name__)

MAX_RAND_INT = len(FORTUNES) - 1


@app.route("/")
def root():
    index = random.randint(0, MAX_RAND_INT)
    message = FORTUNES[index]
    permalink = str(index)
    return render_template('index.html', message=message, permalink=permalink)


@app.route("/<int:id>")
def users(id):
    message = FORTUNES[id]
    return render_template('index.html', message=message, permalink=id)


@app.route("/about")
def about():
    message = 'Hello! This is Fortune! \o/'
    return render_template('index.html', message=message, permalink='about')


if __name__ == '__main__':
    app.run()
