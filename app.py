# import flask
# from flask import request
# import pandas as pd
# from datetime import datetime as dt

# data = pd.read_csv('data.csv', names=['s', 'e', 'm']).set_index('m')

# series = pd.Series(index=range(data.s.min(), dt.now().year + 1))
# for m in data.index:
#     series.loc[data.loc[m].s:data.loc[m].e] = m

# app = flask.Flask(__name__)


# @app.route('/', methods=['GET'])
# def home():
#     year = int(request.args['year'])
#     try:
#         return series.loc[year]
#     except KeyError:
#         return f'Invalid input ({series.index.min()} - {series.index.max()})'
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from the url parameter /getmsg/?name=
    name = request.args.get("name", None)

    # For debugging
    print(f"Received: {name}")

    response = {}

    # Check if the user sent a name at all
    if not name:
        response["ERROR"] = "No name found. Please send a name."
    # Check if the user entered a number
    elif str(name).isdigit():
        response["ERROR"] = "The name can't be numeric. Please send a string."
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome API!"

    # Return the response in json format
    return jsonify(response)


@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome API!",
            # Add this option to distinct the POST request
            "METHOD": "POST"
        })
    else:
        return jsonify({
            "ERROR": "No name found. Please send a name."
        })


@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Welcome to our medium-greeting-api!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)