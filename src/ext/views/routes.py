from flask import Flask, request, jsonify
from src.ext.db.models import State, db
from src.ext.api.serializer import StateSchema


def init_app(app: Flask):
    @app.route('/')
    def index():
        return {'ola': 'mundo'}

    @app.route('/state/list', methods=['GET'])
    def list_State():
        state = StateSchema(many=True)
        result = State.query.all()
        return state.jsonify(result), 200

    @app.route('/state/add', methods=['POST'])
    def sreate_State():
        state = StateSchema()
        # print(type(request.json))
        # metodo usado com relacionametos
        data = state.load(request.json, session=db.session)
        # print(data)
        db.session.add(data)
        db.session.commit()
        return state.jsonify(data), 201
