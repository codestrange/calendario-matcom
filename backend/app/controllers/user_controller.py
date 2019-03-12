from json import loads
from flask import jsonify, abort, request
from marshmallow import Schema, fields, post_load, validates, ValidationError
from . import api
from ..auth import auth_token
from ..database import db, User
from ..exceptions import ValidationResponseError


class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)

    @post_load
    def load(self, data):
        return User(**data)

class UserValidatorSchema(UserSchema):
    @validates('username')
    def validate_username(self, username):
        if User.query.filter_by(username=username).first():
            raise ValidationError('Username already in use.')

    @validates('email')
    def validate_email(self, email):
        if User.query.filter_by(email=email).first():
            raise ValidationError('Email already registered.')


@api.route('/users/', methods=['GET'])
@auth_token.login_required
def get_users():
    users = User.query.all()
    schema = UserSchema(many=True, only=('id', 'username', 'email'))
    return jsonify(schema.dump(users).data)


@api.route('/users/<int:id>/', methods=['GET'])
@auth_token.login_required
def get_user(id):
    user = User.query.get(id)
    schema = UserSchema(only=('id', 'username', 'email'))
    if user is None:
        abort(404)
    return jsonify(schema.dump(user).data)


@api.route('/users/', methods=['POST'])
# @auth_token.login_required
def post_user():
    json = loads(request.json) if isinstance(request.json, str) else request.json
    errors = UserValidatorSchema().validate(json)
    if errors:
        raise ValidationResponseError(errors)
    user = UserSchema().load(json).data
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered.'}), 201


@api.route('/users/<int:id>/', methods=['PUT'])
@auth_token.login_required
def put_user(id):
    user = User.query.get(id)
    if user is None:
        abort(404)
    json = loads(request.json) if isinstance(request.json, str) else request.json
    errors = UserSchema().validate(json)
    if errors:
        raise ValidationResponseError(errors)
    new = UserSchema().load(json).data
    if User.query.filter(User.username == new.username and User.id != id).first():
        raise ValidationResponseError({'username': ['Username already in use.']})
    if User.query.filter(User.email == new.email and User.id != id).first():
        raise ValidationResponseError({'email': ['Email already registered.']})
    user.username = new.username
    user.email = new.email
    user.password_hash = new.password_hash
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User updated.'}), 201


@api.route('/users/<int:id>/', methods=['DELETE'])
@auth_token.login_required
def delete_user(id):
    user = User.query.get(id)
    if user is None:
        abort(404)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted.'})
