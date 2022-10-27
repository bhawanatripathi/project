
from urllib import response
from flask_smorest import Blueprint,abort
from flask import request
import uuid
from db import db
import random
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt
from models.Usermodel import UserModel
from schema.schema import PlainUserSchema, UserSchema
import socket

blp = Blueprint("userblueprint", __name__, description="Operations on users")

Api_key="PMAK-6350bf4168f31579d464ebdb-872772de3c32c604eaf06823df7aa4d2a5"
@blp.route("/userdata")
class User(MethodView):
    @jwt_required()
    @blp.response(201, UserSchema(many=True))
    def get(self):
            return UserModel.query.all()
            

    #@jwt_required(locations=['cookies'])
    @blp.response(201, UserSchema)
    def post(self):
        # if sender_api_key!=Api_key:
        #     abort(401, message="Admin privilege required.")
        
        data=request.get_json()
        id=str(uuid.uuid1())
        account_num=random.randint(120000,990000)
        data["acc_num"]=account_num
        data["id"]=id

        new_user=UserModel(**data)
        #return new_user
        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            print("ERROR THROWN {}".format(e))
            abort(500, message="An error occurred while inserting the item.")

        return new_user


    @jwt_required()
    @blp.response(201, PlainUserSchema)
    def delete(self,sender_api_key):
        if sender_api_key!=Api_key:
            abort(401, message="Admin privilege required.")
        
        data=request.get_json()
        aadhar=data["aadhar"] 
        del_user = UserModel.query.get_or_404(aadhar)
        db.session.delete(del_user)
        db.session.commit()
        return {"message":"User DELETED"},200



    @jwt_required()
    @blp.response(201, UserSchema)
    def put(self,sender_api_key):
        if sender_api_key!=Api_key:
            abort(401, message="Admin privilege required.")
        
        data=request.get_json()
        aadhar=data["aadhar"]
        user = UserModel.query.get_or_404(aadhar)
        if user:
            user.full_name=data["full_name"]
            user.DOB=data["DOB"] 
       
        db.session.add(user)
        db.session.commit()

        return user
        
        
@jwt_required()
@blp.route("/finduser/<int:aadhar>")
class findUser(MethodView):
    @blp.response(200, UserSchema)
    def get(self,aadhar):
        user = UserModel.query.get_or_404(aadhar)
        return user        


     