from flask import Flask, make_response

app = Flask(__name__)

@app.before_first_request
def init_app():
    #TODO: init mongo db here
    #TODO: init grpc server here
    return true

@app.route("/health")
def health():
    return make_response({}, 200)
