from DB import db
import datetime    
class UserRoleModel:

    __tablename__="UserRole"
    id=db.Column(db.Integer,nullable=False,primary_key=True)
    name=db.Column(db.String,default="Savings")
    max_withdrawal_amount=db.Column(db.Integer,default=0)
    min_balance=db.Column(db.Integer,default=5000)    
    created_at=db.Column(db.TIMESTAMP,default=datetime.now())
    updated_at=db.Column(db.TIMESTAMP,default=datetime.now())
    modified_by=db.Column(db.String,  db.foreign_key("Users.id"))





    


# CREATE TABLE IF NOT EXISTS account_type (
#     id INT PRIMARY KEY AUTO_INCREMENT, 
#     name VARCHAR(20) DEFAULT 'savings',
#     max_withdrawal_amount INT DEFAULT 0,
#     min_balance INT DEFAULT 5000,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     modified_by VARCHAR(70),
#     FOREIGN KEY (modified_by) REFERENCES users(id)
# );
