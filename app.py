from flask import Flask
from flask_jwt_extended import JWTManager
from flask_smorest import Api
from resources.userblueprint import blp as UserBlueprint 
from flask_migrate import Migrate
from db import db
import os
from resources.auth import blp as AuthBlueprint
import socket
from flask_wtf import CSRFProtect

def create_app(db_url=None):
    app= Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config['JWT_COOKIE_SECURE'] = False
    app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
    app.config['JWT_COOKIE_CSRF_PROTECT'] = True
    app.config['JWT_CSRF_CHECK_FORM'] = True
    
    db.init_app(app)    
    migrate = Migrate(app, db)
    csrf = CSRFProtect()
    csrf.init_app(app)

    app.config["SECRET_KEY"] ="jose"
    jwt = JWTManager(app)
    api = Api(app)

    
    with app.app_context():
        db.create_all()
        
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(AuthBlueprint)

    return app
