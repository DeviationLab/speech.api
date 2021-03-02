from flask import jsonify

# defining our request structure
validKeys = ["text","api_key","params"] # the keys, that are valid and handeled
validParameters = [] # TODO
requiredKeys = ["text","api_key"] # the keys, that are always required

# TODO: SQL Database for api_key handeling/creation
api_keys = ["f81c3ce5-5700-4b9c-b50f-08a0dc8549dc-19c97b26"]

# a universal helpMessage
helpMessage = " For more information please go to http://speech.api.deviationlab.ml/docs or open an issue on our GitHub repo."

# a class which test request
class ErrorHandler():
    def __init__(self):
        # define the test pipeline
        self.testPipeline = [
            RequestSyntaxError,
            UnknownAPIKeyError,
            ]
    # checks if a request passes the test pipeline
    def throws(self, req):
        for e in self.testPipeline:
            throwed = e(req)
            if throwed:
                return True, jsonify(throwed)
        return False, jsonify(req)

    # emergency exit
    def throwUnknownError(self):
        return RequestUnknownError()

###### Errors ######

# throw an error, when a unhandled error happens
def RequestUnknownError():
    # In case of fire:
    #   1. git commit
    #   2. git push
    #   3. leave building
    return {"message": "An unknown error occured." + helpMessage}

# throw an error, if the syntax is wrong
def RequestSyntaxError(req):
    # check if all required keys are present
    if False in [key in req.keys() for key in requiredKeys]:
        return {"message": f"A syntax error occured (Passed keys: {list(req.keys())}). The following keys are always required: {requiredKeys}." + helpMessage}
    # check if all keys are valid
    if False in [key in validKeys for key in req.keys()]:
        return {"message": f"A syntax error occured (Passed keys: {list(req.keys())}). Encountered invalid key(s) {[key for key in req.keys() if key not in validKeys]}." + helpMessage}

# throw an error, if the APIKey is wrong/not registered
def UnknownAPIKeyError(req):
    if req['api_key'] not in api_keys:
        return {"message": f"{req['api_key']} is not a valid API key. Get one at http://speech.api.deviationlab.ml/." + helpMessage}
