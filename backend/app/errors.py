from flask import jsonify
from .controllers import api
from .exceptions import ValidationResponseError


def bad_request(errors):
    response = jsonify(errors)
    return response, 400


def unauthorized(message):
    response = jsonify({'error': 'unauthorized', 'message': message})
    return response, 401


def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    return response, 403


@api.errorhandler(ValidationResponseError)
def validation_error(e):
    return bad_request(e.args[0])
