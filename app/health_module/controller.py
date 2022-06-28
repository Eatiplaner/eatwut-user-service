from flask import make_response
from . import health_module


@health_module.route("/health")
def health():
    return make_response({}, 200)
