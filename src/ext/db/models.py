from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure(app: Flask):
    db.init_app(app)
    app.db = db


class State(db.Model):
    cnpj = db.Column(db.String(120), unique=True,
                     nullable=False, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120),  nullable=False)
    country = db.relationship('Country', backref='State', lazy=True)


class Country(db.Model):
    cnpj = db.Column(db.String(120), unique=True,
                     nullable=False, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120),  nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey('state.cnpj'),
                         nullable=False)
    cnes = db.relationship('Upa', backref='Country', lazy=True)


class Upa(db.Model):
    cnes = db.Column(db.String(120), unique=True,
                     nullable=False, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120),  nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.cnpj'),
                           nullable=False)
