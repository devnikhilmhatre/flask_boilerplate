from flask import Flask
from src.blueprints.demo1 import blueprint1
from src.blueprints.demo2 import blueprint2


def create_app():
    app = Flask(__name__)

    register_extentions(app)
    register_blueprints(app)

    return app


def register_extentions(app):
    pass


def register_blueprints(app):
    app.register_blueprint(blueprint1)
    app.register_blueprint(blueprint2)
