from flask_sqlalchemy import SQLAlchemy

users=[{"b611a1af-502d-4d22-a8bf-b0b4db2eb5e0": {'name':"ram", "password":'$pbkdf2-sha256$6400$0ZrzXitFSGltTQnBWOsdAw$Y11AchqV4b0sUisdZd0Xr97KWoymNE0LNNrnEgY4H9M', "dob":"12/07/2002", "contact":"949494","email":"r@a.com", "acc_num":12345,"acc_type":"savings","aadhar":123333},
        "22e28cbc-087f-4b21-aae8-777786b48cb2":{'name':"mandy", "password":'$pbkdf2-sha256$6400$0ZrzXitFSGltTQnBWOsdAw$Y11AchqV4b0sUisdZd0Xr97KWoymNE0LNNrnEgY4H9M', "dob":"11/07/2001", "contact":"646464","email":"m@a.com", "acc_type":"current", "acc_num":176345,"aadhar":123833}}]

acc_types=[{"0":{"name":"savings", "max_withdrawal":5000,"min_balance": 5000, "created_at": "12:00", "updated_at": '01:00' , "modified_by": "admin1"},
            "1": {"name":"current", "max_withdrawal":10000, "min_balance": 10000, "created_at": "10:00", "updated_at": "12:00" , "modified_by": "admin2"}}]

#db = SQLAlchemy()