from modules.users.service import UsersService

from werkzeug.exceptions import BadRequest, HTTPException
from flask_restx import Namespace, Resource
from flask import request

api = Namespace(
    "Users", path="/api/v1/users"
)


@api.route("")
class UsersController(Resource):
    def post(self):
        try:
            requestBody = request.json
            paramsToCheck = ['name', 'branch']
            missingParams = []
            for param in paramsToCheck:
                if param not in requestBody.keys():
                    missingParams.append(param)
            if len(missingParams) > 0:
                raise BadRequest(f"Bad Request: '{', '.join(missingParams)}' required")
                
            userDTO = UsersService.create(requestBody['name'], requestBody['branch'])
            return userDTO, 201

        except Exception as e:
            if isinstance(e, HTTPException):
                return {"message": e.description}, e.code

            api.logger.error("Error: %s", str(e))
            return {"message": "Internal Server Error"}, 500
        

@api.route("/auth")
class UserController(Resource):
    def post(self):
        try:
            requestBody = request.json
            paramsToCheck = ['id', 'password']
            missingParams = []
            for param in paramsToCheck:
                if param not in requestBody.keys():
                    missingParams.append(param)
            if len(missingParams) > 0:
                raise BadRequest(f"Bad Request: '{', '.join(missingParams)}' required")
            
            userDTO = UsersService.validate(requestBody['id'], requestBody['password'])
            return userDTO, 200
        
        except Exception as e:
            if isinstance(e, HTTPException):
                return {"message": e.description}, e.code

            api.logger.error("Error: %s", str(e))
            return {"message": "Internal Server Error"}, 500