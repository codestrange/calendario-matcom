from flask import g
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from werkzeug.security import check_password_hash
from .container import Container
from .errors import unauthorized as response_unauthorized

auth = HTTPBasicAuth()
auth_token = HTTPBasicAuth()


def verify_password(user, password):
    return check_password_hash(user.password_hash, password)


def generate_auth_token(user, expires_in=3600):
    s = Serializer(Container.instance().current_app.config['SECRET_KEY'], expires_in=expires_in)
    return s.dumps({'id': user.id}).decode('utf-8')


def verify_auth_token(token):
    s = Serializer(Container.instance().current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except:
        return None
    repository = Container.instance().current_app.unitofwork.get_repository('UserRepository')
    return repository.query().get(data['id'])


@auth.verify_password
def auth_verify_password(username, password):
    repository = Container.instance().current_app.unitofwork.get_repository('UserRepository')
    g.current_user = repository.query().filter(lambda user: user.username == username).first()
    if g.current_user is None:
        return False
    return verify_password(g.current_user, password)


@auth.error_handler
def auth_error_handler():
    error_message = 'invalid password'
    if g.current_user is None:
        error_message = 'user don\'t exist'
    return response_unauthorized(error_message)


@auth_token.verify_password
def auth_token_verify_password(token, unused):
    g.current_user = verify_auth_token(token)
    return g.current_user is not None and unused == ''


@auth_token.error_handler
def auth_token_error_handler():
    return response_unauthorized('please send your authentication token')
