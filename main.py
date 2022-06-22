import os
from flask import Flask, make_response
from pymongo import MongoClient
import json
from bson import json_util


app = Flask(__name__)

def connect():
    uri = os.environ.get("DATABASE_URL")
    client = MongoClient(uri, serverSelectionTimeoutMS=6000)
    return client


@app.before_first_request
def init_app():
    # TODO: init mongo db here

    # TODO: init grpc server here
    print("test")


@app.route("/health")
def health():
    return make_response({}, 200)



@app.route("/conn_db")
def conn_db():
    client = connect()
    db = client["eatiplan-user-service"]
    User = db.User
    res = json.loads(json_util.dumps(User.find_one()))
    return res
