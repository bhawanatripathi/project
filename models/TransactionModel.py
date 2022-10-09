from DB import db
import datetime    
class UserRoleModel:

    __tablename__="UserRole"
    id=db.Column(db.Integer,nullable=False,primary_key=True)
    txn_type=db.Column(db.Integer, db.foreign_key("TransactionTypeModel.id"))
    amount=db.Column(db.Integer,nullable=False)
    account_num=db.Column(db.BigInteger,db.foreign_key("AccountModel.account_num"), nullable=False)
    created_at=db.Column(db.TIMESTAMP,default=datetime.now())
   

# CREATE TABLE IF NOT EXISTS transaction(
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     txn_type INT,
#     amount  INT,
#     account_num  INT,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY(txn_type) REFERENCES  transaction_type(id) ON DELETE CASCADE,
#     FOREIGN KEY(account_num) REFERENCES  account(account_num) ON DELETE CASCADE
#     );