from flask import Flask, jsonify, request, Response
from flask_restful import Api, Resource

from subprocess import Popen


app = Flask(__name__)
api = Api(app)

class RunScript(Resource):
    def post(self, script_name):
        arguments_json = request.get_json()
        arguments_array = []
        arguments_string = ""

        for arg, value in arguments_json.items():
            arguments_array.append(arg)
            arguments_array.append(value)
            arguments_string += (arg + " " + value + " ")
        
        Popen(("python " + "callable_scripts/" + script_name + " " + arguments_string), shell=True)

        return Response("OK", status=200)


api.add_resource(RunScript, "/runscript/<string:script_name>")

if __name__ == '__main__':
    app.run(debug=True)