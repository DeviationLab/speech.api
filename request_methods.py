from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from errorhandler import ErrorHandler

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
