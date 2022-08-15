from flask import Flask, redirect
from flask import jsonify
import requests

app = flask.Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


@app.route('/name')
def hello():
    return jsonify({'name': 'Piyush',
                    'address': 'India'})


