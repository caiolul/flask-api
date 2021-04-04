from flask import Flask, request, jsonify
from src.ext.db.models import State, db
from src.ext.api.serializer import StateSchema


def init_app(app: Flask):
    @app.route('/')
    def index():
        return {'ola': 'mundo'}

    @app.route('/state/list', methods=['GET'])
    def list_state():
        state = StateSchema(many=True)
        result = State.query.all()
        return state.jsonify(result), 200

    @app.route('/state/add', methods=['POST'])
    def create_state():
        state = StateSchema()
        query = State.query.filter(State.cnpj == request.json['cnpj'])

        data = state.load(request.json, session=db.session)
        if(query.first() == None):
            db.session.add(data)
            db.session.commit()
            return state.jsonify(data), 201
        else:
            return jsonify({'Response': 'State already exists'}), 400

    @app.route('/state/delete/<cnpj>', methods=['DELETE'])
    def delete_state(cnpj):
        state = State.query.filter(State.cnpj == cnpj).delete()

        if(state == True):
            db.session.commit()

            return jsonify({"Delete": "State using the following CNPJ -> " + cnpj}), 200
        else:
            return jsonify({"Response": "State not found"}), 404

    @app.route('/state/update/<cnpj>', methods=['PUT'])
    def update_state(cnpj):

        state = StateSchema()
        data = State.query.filter(State.cnpj == cnpj)
        if(data.first() != None):
            data.update(request.json)
            db.session.commit()
            return state.jsonify(request.json), 201
        else:

            return jsonify({"Response": "State not found"}), 404
