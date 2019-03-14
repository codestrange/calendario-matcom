from flask import g, current_app
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from .errors import unauthorized as response_unauthorized
from .database import User

auth = HTTPBasicAuth()
auth_token = HTTPBasicAuth()


def generate_auth_token(user, expires_in=3600):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expires_in)
    return s.dumps({'id': user.id}).decode('utf-8')


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except:
        return None
    return User.query.get(data['id'])


@auth.verify_password
def auth_verify_password(username, password):
    g.current_user = user = User.query.filter_by(username=username).first()
    return user and user.verify_password(password) and user.confirmed and user.activated


@auth.error_handler
def auth_error_handler():
    user = g.current_user
    error_message = 'invalid password'
    if user is None:
        error_message = 'user don\'t exist'
    elif not user.confirmed:
        error_message = 'user unconfirmed'
    elif not user.activated:
        error_message = 'user deactivated'
    return response_unauthorized(error_message)


@auth_token.verify_password
def auth_token_verify_password(token, unused):
    g.current_user = verify_auth_token(token)
    return g.current_user is not None and unused == ''


@auth_token.error_handler
def auth_token_error_handler():
    return response_unauthorized('please send your authentication token')
