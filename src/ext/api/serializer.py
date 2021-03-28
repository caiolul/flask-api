from flask import Flask
from flask_marshmallow import Marshmallow

from src.ext.db.models import User

ma = Marshmallow()


def configure(app: Flask):
    ma.init_app(app)


class UserShcema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True
        load_instance = True
