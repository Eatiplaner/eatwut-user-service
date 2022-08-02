import os
from flask import Flask
from mongoengine import connect

from .config import config_by_name

app = Flask(__name__)


def create_app(config_name):

    config = config_by_name[config_name]
    app.config.from_object(config)

    if not config.TESTING:
        mongo_connect()

    return app


def mongo_connect():
    db = os.getenv('MONGO_DB')
    host = os.getenv('MONGO_HOST')
    port = int(os.getenv('MONGO_PORT') or "27017")
    username = os.getenv('MONGO_INITDB_ROOT_USERNAME')
    password = os.getenv('MONGO_INITDB_ROOT_PASSWORD')

    host = f'mongodb://{username}:{password}@{host}:{port}/{db}'

    app.logger.info(
        "Mongo connected on %s",
        host
    )
    connect(host=host)
