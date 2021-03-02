from flask import Flask, jsonify, request
from flask_restful import Resource, Api

from utilities.request_methods import *

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

# adding the defined resources along with their corresponding urls
api.add_resource(MainRequest, '/')

# WARNING: THIS IS JUST FOR TESTING PURPOSES. REMOVE THIS IN PRODUCTION!!!
api.add_resource(APIKey, '/generateAPIKey')

# driver function
if __name__ == '__main__':

    app.run(debug = True)
