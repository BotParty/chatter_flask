import os
from flask import Flask, Blueprint
import settings
from api.restplus import api
from api.endpoint.speech import ns as speech_namespace

app = Flask(__name__)


def configure_app(flask_app):
    print("configure")
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(speech_namespace)
    flask_app.register_blueprint(blueprint)
    print("initialize app")


def main():
    initialize_app(app)
    app.run(debug=True)


if __name__ == "__main__":
    main()
