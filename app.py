from flask import Flask,request,abort
import uuid
from flask_jwt_extended import JWTManager
import secrets
from flask_jwt_extended import create_access_token
import random
from flask_jwt_extended import jwt_required
from flask_smorest import Api
from resources.userblueprint import blp as UserBlueprint 
from resources.acctypeBlueprint import blp as AcctypeBlueprint 

import os

app= Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["JWT_SECRET_KEY"] = "harry"#secrets.SystemRandom().getrandbits(128)
jwt = JWTManager(app)

api = Api(app)

api.register_blueprint(UserBlueprint)
api.register_blueprint(AcctypeBlueprint)




# @app.post("/authenticate")
# def authenticate_user():
#     data=request.get_json()
#     username=data['username']
#     password=data['password']
#     for user in users[0].values():
#         if user["name"]==username:
#             if user["password"]==password:
#                 access_token=create_access_token(identity=user["acc_num"])
#                 authenticated=True
#                 return {"access_token":access_token}
#             else:
#                 return "Invalid credentials"
#     return "user doesn't exist" 


# @jwt_required()
# @app.get("/userdata")
# def getallusers():
#     return users

 
# @jwt_required()
# @app.get("/finduser")
# def get_user_by_name():
#     data=request.get_json()
#     for details in users[0].values():
#         if details["aadhar"]==data["aadhar"]:
#             return details
#     return "USER NOT FOUND"        

 

# @jwt_required()
# @app.post("/userdata")
# def createUser():
#     data=request.get_json()
#     id=str(uuid.uuid1())
#     account_num=random.randint(120000,990000)
#     data["account_num"]=account_num
#     try:
#         users[0][id]=data
#         return users 

#     except KeyError:
#         abort(404,message="Invalid id")

 
# @jwt_required()
# @app.delete("/userdata")
# def deleteUser():
#     data=request.get_json()
#     id=data["id"] 
#     try:
#         del users[0][id]
#         return users 
#     except KeyError:
#         abort(404,message="Invalid id")
    
 
# @jwt_required()
# @app.put("/userdata")
# def updateUser():
#     data=request.get_json()
#     id=data["id"]
#     feature=list(data.keys())[1]
#     updated_value=data[feature]
#     try:
#         users[0][id][feature]=updated_value
#         return users
#     except KeyError:
#         return "Invalid Key",404
    
