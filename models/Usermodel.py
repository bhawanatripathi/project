
from enum import unique
from db import db

class UserModel(db.Model):
    __tablename__="Users"
    id=db.Column(db.Integer,unique=True, nullable=False)
    full_name=db.Column(db.String,nullable=False)
    password=db.Column(db.String,nullable=False)
    aadhar=db.Column(db.Integer,nullable=False, primary_key=True)
    DOB=db.Column(db.String(12), nullable=False)
    phone=db.Column(db.Integer,nullable=False)
    email=db.Column(db.String,nullable=False,unique=True)
    acc_type=db.Column(db.String,nullable=False,unique=False)
    acc_num=db.Column(db.Integer,unique=True, nullable=False)
    
  