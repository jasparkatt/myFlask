# import flask class
from flask import Flask, render_template
from string import Template
#create an flask instance
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route('/name')
def welcome():
    return "welcome to the fishing map"