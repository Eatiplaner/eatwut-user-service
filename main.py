from flask import Flask, make_response
# from pymongo import MongoClient

app = Flask(__name__)


# def connect():
#     db_user = "mongo"
#     db_pass = "0815985051"
#     db_addr = "localhost:27017"
#     uri = "mongodb://{0}:{1}@{2}".format(db_user, db_pass, db_addr)
#     client = MongoClient(uri, serverSelectionTimeoutMS=6000)
#     return client


@app.before_first_request
def init_app():
    # TODO: init mongo db here
    # connect()
    # TODO: init grpc server here
    print("Hello Eatiplan")


@app.route("/health")
def health():
    return make_response({}, 200)
