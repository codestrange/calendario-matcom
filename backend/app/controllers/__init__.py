from flask import Blueprint

api = Blueprint('api', __name__)

from . import auth_controller, user_controller#, role_controller
