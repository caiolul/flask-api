import os
import platform
from src.ext.views.routes import init_app as views_init
from src.ext.db.models import configure as configure_db
from src.ext.api.serializer import configure as config_marshmallow
from flask_migrate import Migrate
from flask import Flask

current_path = os.path.dirname(os.path.abspath(__file__))
# Config path
# sqlite3_win = 'sqlite:///'
# sqlite3_linux = 'sqlite:////'


def create_app():
    app = Flask(__name__)
    path = '%s/migrations' % (current_path)
    if(platform.system == "Windowns"):
    if (app.debug == True):
        # Env database
        # postgresql://username:password@localhost:5432/database
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:api@localhost:5432/postgres'

        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s/ext/db/testing/test.db' % (
            current_path)
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    else:
        # production database
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:api@localhost:5432/postgres'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s/ext/db/production/prod.db' % (
            current_path)
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    views_init(app)
    configure_db(app)

    config_marshmallow(app)

    Migrate(app, app.db, path)
    return app
