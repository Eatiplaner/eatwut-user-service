from flask import Flask
from mongoengine import connect

from app.health_module.controller import health_module

from .config import config_by_name

app = Flask(__name__)


def create_app(config_name):

    config = config_by_name[config_name]
    app.config.from_object(config)
    register_modules()

    connect(
        db=config.MONGO_DB,
        host=config.MONGO_HOST,
        port=int(config.MONGO_PORT or "27017"),
        username=config.MONGO_USER,
        password=config.MONGO_PASSWORD
    )

    app.logger.info(
        "Mongo connected on %s:%s",
        config.MONGO_HOST, config.MONGO_PORT
    )

    return app


def register_modules():
    app.register_blueprint(health_module)
