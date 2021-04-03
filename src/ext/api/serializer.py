from flask import Flask
from flask_marshmallow import Marshmallow

from src.ext.db.models import State

ma = Marshmallow()


def configure(app: Flask):
    ma.init_app(app)


class StateSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = State
        include_fk = True
        load_instance = True
