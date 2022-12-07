from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config['SCRET_KEY'] = 'NOT A SECRET KEY'

    return app