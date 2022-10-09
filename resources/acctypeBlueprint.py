from flask_smorest import Blueprint,abort
from flask import request
import uuid
import random
from flask.views import MethodView
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required

from db import acc_types

blp = Blueprint("stores", __name__, description="Operations on stores")


@blp.route("/acctype")
class Acctype(MethodView):
    
    def get(self):
        return acc_types

    def put(self):
        data=request.get_json()
        feature=list(data.keys())[1]
        updated_value=list(data.values())[1]
        acc_types[0][data["id"]][feature]=updated_value
        return acc_types[0][data["id"]]    
 
    def post(self):
        data=request.get_json()
        id=list(data.keys())[0]
        acc_types[0][id]=data[id] 
        return acc_types


    def delete(self):
        data=request.get_json()
        del acc_types[0][data["id"]]
        return acc_types       