
from db import db

class UserModel(db.Model):
    __tablename__="Users"
    id=db.Column(db.Integer,unique=True, nullable=False)
    full_name=db.Column(db.String,nullable=False)
    password=db.Column(db.String,nullable=False)
    aadhar=db.Column(db.Integer,nullable=False, primary_key=True)
    DOB=db.Column(db.String(14), nullable=False)
    phone=db.Column(db.Integer,nullable=False)
    email=db.Column(db.String,nullable=False,unique=True)
    acc_type=db.Column(db.String,nullable=False,unique=True)
    acc_num=db.Column(db.Integer,unique=True, nullable=False)


# CREATE TABLE IF NOT EXISTS users (
#     id VARCHAR(70) UNIQUE NOT NULL,
#     full_name VARCHAR(20) NOT NULL, 
#     password VARCHAR(100) NOT NULL,
#     aadhar BIGINT NOT NULL PRIMARY KEY,
#     DOB VARCHAR(20) NOT NULL,
#     isApproved INT DEFAULT 0,
#     phone BIGINT NOT NULL, 
#     email VARCHAR(30) NOT NULL UNIQUE,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     modified_by VARCHAR(70),
#     FOREIGN KEY (modified_by) REFERENCES users(id)
#     );




