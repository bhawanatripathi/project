from flask import Flask
from flask_jwt_extended import JWTManager
from flask_smorest import Api
from resources.userblueprint import blp as UserBlueprint 
from flask_migrate import Migrate
from db import db
import os
from resources.auth import blp as AuthBlueprint
import socket

def create_app(db_url=None):
    app= Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["JWT_SECRET_KEY"] = "harry"#secrets.SystemRandom().getrandbits(128)
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)    
    migrate = Migrate(app, db)

    app.config["JWT_SECRET_KEY"] ="jose"
    jwt = JWTManager(app)
    api = Api(app)

    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        return {"client_IP":IPAddr}
    
    with app.app_context():
        db.create_all()
        
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(AuthBlueprint)
    
    return app

