from random import randint
from flask import Flask, render_template


app = Flask(__name__)
app.config.from_pyfile('settings.py')


@app.route("/")
def home():
    total_fireflies = randint(12, 50)
    color_seed = randint(1, 255)
    if color_seed % 51 == 0:
        color = "rgb(143, 100, 255)"  # light violet
    elif color_seed % 42 == 0:
        color = "rgb(75, 100, 130)"  # light indigo?
    elif color_seed % 36 == 0:
        color = "rgb(100, 100, 255)"  # light blue
    elif color_seed % 31 == 0:
        color = "rgb(100, 255, 100)"  # light green
    elif color_seed % 28 == 0:
        color = "rgb(255, 127, 100)"  # light orange
    elif color_seed % 25 == 0:
        color = "rgb(255, 100, 100)"  # light red
    else:
        color = "rgb(255, 255, 50)"  # default is yellow

    return render_template('home.html',
                           total_fireflies=total_fireflies,
                           color=color)
