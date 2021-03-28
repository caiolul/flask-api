from flask import Flask, request, json, jsonify
from src.ext.db.models import User, db
from src.ext.api.serializer import UserShcema


def init_app(app: Flask):
    @app.route('/')
    def index():
        return {'ola': 'mundo'}

    @app.route('/user/list', methods=['GET'])
    def list_user():
        user = UserShcema(many=True)
        result = User.query.all()
        return user.jsonify(result), 200

    @app.route('/user/add', methods=['POST'])
    def create_user():
        user = UserShcema()
        data = user.loads(json.dumps(request.json))
        db.session.add(data)
        db.session.commit()
        return user.jsonify(data), 201
