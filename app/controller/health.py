from flask import make_response

from app.main import app


@app.route("/health")
def health():
    return make_response({}, 200)
