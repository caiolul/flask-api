from flask import Flask
# from src.ext.db import ...


def init_app(app: Flask):
    @app.route('/')
    def index():
        return {'ola': 'mundo'}

    @app.route('/state', methods=['GET', 'POST'])
    def register_state():
        return{'patos': ['500 vacinados', '500 sem vacinação']}
