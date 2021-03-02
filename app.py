from flask import Flask, jsonify, request
from flask_restful import Resource, Api

from request_methods import MainRequest

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

# adding the defined resources along with their corresponding urls
api.add_resource(MainRequest, '/')

# driver function
if __name__ == '__main__':

    app.run(debug = True)
