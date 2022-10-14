from marshmallow import  Schema, fields


class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    acc_num=fields.Integer(dump_only=True)
    full_name = fields.Str(required=True)
    password= fields.Str(required=True)
    DOB= fields.Str(required=True)
    phone=fields.Str(required=True) 
    email=fields.Str(required=True)
    acc_type=fields.Str(required=True)
    aadhar=fields.Str(required=True)

class PlainUserSchema(Schema):
    id = fields.Str(required=True)
    

class UpdateUserSchema(Schema):
    aadhar=fields.Integer(required=True)
    full_name = fields.Str(required=True)
    DOB= fields.Str(required=True)
 

class AcctypeSchema(Schema):
    id=fields.Integer(required=True)
    name= fields.Str(required=True)
    max_withdrawal_amount=fields.Integer(required=True)
    min_balance=fields.Integer(required=True)
    created_at=fields.Str(required=True)
    updated_at=fields.Str(required=True)
    modified_by=fields.Str(required=True)    

class PlainAcctypeSchema(Schema):
    id=fields.Integer(required=True)    


class UpdateAcctypeSchema(PlainUserSchema):
    id=fields.Integer(required=True)
    min_withdrawal = fields.Str(required=True)

class PlainAuthSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required =True)
