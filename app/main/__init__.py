from flask import Flask
from mongoengine import connect

from app.model.address import Address
from app.model.user import User

from .config import config_by_name


app = Flask(__name__)


def create_app(config_name):

    config = config_by_name[config_name]
    app.config.from_object(config)

    connect(
        db=config.MONGO_DB,
        host=config.MONGO_HOST,
        port=int(config.MONGO_PORT or "27017"),
        username=config.MONGO_USER,
        password=config.MONGO_PASSWORD
    )

    # NOTE: Test saving user will remove later
    home_address = Address(district="District 1",
                           city="Danang", type="home").save()
    User(
        username="username",
        password="123456",
        first_name="louis",
        last_name="nguyen",
        email="eatiplaner@gmail.com",
        addresses=[home_address],
    ).save()

    app.logger.info(
        "Mongo connected on %s:%s",
        config.MONGO_HOST, config.MONGO_PORT
    )

    return app
