from flask import jsonify


from . import base


@base.route("/")
def index():
    return jsonify("Hello world. We have lift off!")
