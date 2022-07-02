import os
from flask import Flask
from mongoengine import connect

from .config import config_by_name

app = Flask(__name__)


def create_app(config_name):

    config = config_by_name[config_name]
    app.config.from_object(config)

    connect(
        db=os.getenv('MONGO_DB'),
        host=os.getenv('MONGO_HOST'),
        port=int(os.getenv('MONGO_PORT') or "27017"),
        username=os.getenv('MONGO_USER'),
        password=os.getenv('MONGO_PASSWORD')
    )

    app.logger.info(
        "Mongo connected on %s:%s",
        os.getenv('MONGO_HOST'), os.getenv('MONGO_PORT')
    )

    return app
