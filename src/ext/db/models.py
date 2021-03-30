from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure(app: Flask):
    db.init_app(app)
    # db.create_all()
    app.db = db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),  nullable=False)
    email = db.Column(db.String(120),  nullable=False)
