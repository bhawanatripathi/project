from flask_smorest import Blueprint,abort
from flask import request
import uuid
import random
from flask.views import MethodView
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from db import users
from passlib.hash import pbkdf2_sha256


blp = Blueprint("userblueprint", __name__, description="Operations on users")

@blp.route("/userdata")
class User(MethodView):

    def get(self):
        return users

    def post(self):
        data=request.get_json()
        id=str(uuid.uuid1())
        account_num=random.randint(120000,990000)
        data["account_num"]=account_num
        try:
            users[0][id]=data
            return users 

        except KeyError:
            abort(404,message="Invalid id")

    
    def delete(self):
        data=request.get_json()
        id=data["id"] 
        try:
            del users[0][id]
            return users 
        except KeyError:
            abort(404,message="Invalid id")        

    def put(self):
        data=request.get_json()
        id=data["id"]
        feature=list(data.keys())[1]
        updated_value=data[feature]
        try:
            users[0][id][feature]=updated_value
            return users
        except KeyError:
            return "Invalid Key",404
        

@blp.route("/finduser/<int:aadhar>")
class findUser(MethodView):
    def get(self,aadhar):
        for details in users[0].values():
            if details["aadhar"]==aadhar:
                return details
        return "USER NOT FOUND"        



@blp.route("/login")
class login(MethodView):
    
    def post(self):
        data=request.get_json()
        username=data['username']
        password=data['password']
        for user in users[0].values():
            if user["name"]==username:
                if pbkdf2_sha256.verify(user["password"], password):
                    access_token=create_access_token(identity=user["acc_num"])
                    authenticated=True
                    return {"access_token":access_token}
                else:
                    return "Invalid credentials"
        return "user doesn't exist" 

        