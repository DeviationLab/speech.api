from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from utilities.errorhandler import ErrorHandler
from utilities.keys import *

eh = ErrorHandler()

# a basic request class
class MainRequest(Resource):

    def get(self):
        req = request.args.to_dict()

        # check for errors in request
        error, res = eh.throws(req)
        if error:
            return res

        return jsonify("Hello there!")

# WARNING: THIS IS JUST FOR TESTING PURPOSES. REMOVE THIS IN PRODUCTION!!!
class APIKey(Resource):
    def get(self):
        key = generateNewAPIKey()
        return jsonify(key)
