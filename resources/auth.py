
from http import client
#from msilib.schema import Error
from flask import jsonify, request, render_template

from db import db 
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from models.AuthModel import AuthModel
from schema.schema import PlainAuthSchema
from flask_jwt_extended import create_access_token,get_jwt,jwt_required
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
     create_refresh_token,
    get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies,get_csrf_token,
)

blp = Blueprint("Authentication",__name__,description="Operations on authentication")

@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(PlainAuthSchema)
    @blp.response(200,PlainAuthSchema)
    def post(self,register_data):
        if AuthModel.query.filter(AuthModel.username == register_data["username"]).first():
            abort(409,message="A user with that name already exists")
        new_user = AuthModel(
                username = register_data["username"],
                password = pbkdf2_sha256.hash(register_data["password"])
            )
        try:
            db.session.add(new_user)
            db.session.commit()
            return new_user
        except Exception as e:
            print("error thrown is {}".format(e))
        

        return {"message":"User created Successfully"},201

@blp.route("/login")

class UserLogin(MethodView):
    @blp.arguments(PlainAuthSchema)
    def post(self,login_data):
        #ip=login_data["client_ip"]
        user = AuthModel.query.filter(AuthModel.username == login_data["username"]).first()
        if user and pbkdf2_sha256.verify(login_data["password"],user.password):
            access_token=create_access_token(identity=user.id)
            resp = jsonify({'access_csrf': get_csrf_token(access_token)})
            set_access_cookies(resp, access_token)
            
            return resp, 200          
        abort(401,message="Invalid Credentials, please check and try again")

@blp.route('/', methods=['GET'])
class csrf(MethodView):
    def get(self):
            return render_template("form.html")#, csrf_token=(get_raw_jwt() or {}).get("csrf"))
        # else:
        #     # handle POST request
        #     current_user = get_jwt_identity()        