import os
from flask import Flask, make_response
from pymongo import MongoClient
from bson import json_util
import json

app = Flask(__name__)


def connect():
    uri = os.environ.get("DATABASE_URL")
    client = MongoClient(uri,
                         serverSelectionTimeoutMS=10000,
                         connectTimeoutMS=10000)
    return client


@app.before_first_request
def init_app():
    # TODO: init mongo db here
    # connect()
    # TODO: init grpc server here
    print("Hello Eatiplaner")


@app.route("/health")
def health():
    return make_response({}, 200)


@app.route("/test_findone_user")
def test_findone_user():
    client = connect()
    try:
        info = client.server_info()
        print(info)
    finally:
        print("Server Down")

    db = client["eatiplaner-user-service"]
    user = db.user
    result = json.loads(json_util.dumps(user.find_one()))
    return result
