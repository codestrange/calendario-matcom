from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from werkzeug.security import check_password_hash, generate_password_hash
from ..container import Container


class UserEntity:
    def __init__(self, username, email, password, id=None, roles=None):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.roles = [] if roles is None else roles

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expires_in=3600):
        s = Serializer(Container.instance().current_app.config['SECRET_KEY'], expires_in=expires_in)
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(Container.instance().current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        repository = Container.instance().current_app.unitofwork.get_repository('UserRepository')
        return repository.query().get(data['id'])
