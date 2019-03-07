from json import loads
from flask import jsonify, abort, request
from marshmallow import Schema, fields, post_load, validates, ValidationError
from . import api
from ..auth import auth_token
from ..container import Container
from ..database.entities import UserEntity
from ..exceptions import ValidationResponseError


class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)

    @post_load
    def make_user(self, data):
        return UserEntity(**data)

class UserValidatorSchema(UserSchema):
    @validates('username')
    def validate_username(self, value):
        repo = Container.instance().current_app.unitofwork.get_repository('UserRepository')
        if repo.query().filter(lambda x: x.username == value).first() is not None:
            raise ValidationError('Username already in use.')

    @validates('email')
    def validate_email(self, value):
        repo = Container.instance().current_app.unitofwork.get_repository('UserRepository')
        if repo.query().filter(lambda x: x.email == value).first() is not None:
            raise ValidationError('Email already registered.')


@api.route('/users/', methods=['GET'])
@auth_token.login_required
def get_users():
    repo = Container.instance().current_app.unitofwork.get_repository('UserRepository')
    users = repo.query().all()
    schema = UserSchema(many=True, only=('id', 'username', 'email'))
    return jsonify(schema.dump(users).data)


@api.route('/users/<int:id>/', methods=['GET'])
@auth_token.login_required
def get_user(id):
    repo = Container.instance().current_app.unitofwork.get_repository('UserRepository')
    user = repo.query().get(id)
    schema = UserSchema(only=('id', 'username', 'email'))
    if user is None:
        abort(404)
    return jsonify(schema.dump(user).data)


@api.route('/users/', methods=['POST'])
@auth_token.login_required
def post_user():
    repo = Container.instance().current_app.unitofwork.get_repository('UserRepository')
    json = loads(request.json) if isinstance(request.json, str) else request.json
    errors = UserValidatorSchema().validate(json)
    if errors:
        raise ValidationResponseError(errors)
    user = UserSchema().load(json).data
    repo.add(user)
    Container.instance().current_app.unitofwork.commit()
    return jsonify({'message': 'User registered.'}), 201


@api.route('/users/<int:id>/', methods=['PUT'])
@auth_token.login_required
def put_user(id):
    repo = Container.instance().current_app.unitofwork.get_repository('UserRepository')
    user = repo.query().get(id)
    if user is None:
        abort(404)
    json = loads(request.json) if isinstance(request.json, str) else request.json
    errors = UserSchema().validate(json)
    if errors:
        raise ValidationResponseError(errors)
    new = UserSchema().load(json).data
    if repo.query().filter(lambda x: x.username == new.username and x.id != id).first() is not None:
        raise ValidationResponseError({'username': ['Username already in use.']})
    if repo.query().filter(lambda x: x.email == new.email and x.id != id).first() is not None:
        raise ValidationResponseError({'email': ['Email already registered.']})
    user.username = new.username
    user.email = new.email
    user.password_hash = new.password_hash
    repo.add(user)
    Container.instance().current_app.unitofwork.commit()
    return jsonify({'message': 'User updated.'}), 201


@api.route('/users/<int:id>/', methods=['DELETE'])
@auth_token.login_required
def delete_user(id):
    repo = Container.instance().current_app.unitofwork.get_repository('UserRepository')
    user = repo.query().get(id)
    if user is None:
        abort(404)
    repo.delete(user)
    Container.instance().current_app.unitofwork.commit()
    return jsonify({'message': 'User deleted.'})
