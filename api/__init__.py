import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# db variable initialization
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getcwd()}/resident.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
        
    return app
