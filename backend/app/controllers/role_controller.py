from json import loads
from flask import jsonify, abort, request
from marshmallow import Schema, fields, post_load, validates, ValidationError
from . import api
from ..auth import auth_token
from ..container import Container
from ..database.entities import RoleEntity
from ..exceptions import ValidationResponseError


class RoleSchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True)

    @post_load
    def make_role(self, data):
        return RoleEntity(**data)

class RoleValidatorSchema(RoleSchema):
    @validates('name')
    def validate_name(self, value):
        repo = Container.instance().current_app.unitofwork.get_repository('RoleRepository')
        if repo.query().filter(lambda x: x.name == value).first() is not None:
            raise ValidationError('Name already in use.')


@api.route('/roles/', methods=['GET'])
@auth_token.login_required
def get_roles():
    repo = Container.instance().current_app.unitofwork.get_repository('RoleRepository')
    roles = repo.query().all()
    schema = RoleSchema(many=True)
    return jsonify(schema.dump(roles).data)


@api.route('/roles/<int:id>/', methods=['GET'])
@auth_token.login_required
def get_role(id):
    repo = Container.instance().current_app.unitofwork.get_repository('RoleRepository')
    role = repo.query().get(id)
    schema = RoleSchema()
    if role is None:
        abort(404)
    return jsonify(schema.dump(role).data)


@api.route('/roles/', methods=['POST'])
@auth_token.login_required
def post_role():
    repo = Container.instance().current_app.unitofwork.get_repository('RoleRepository')
    json = loads(request.json) if isinstance(request.json, str) else request.json
    errors = RoleValidatorSchema().validate(json)
    if errors:
        raise ValidationResponseError(errors)
    role = RoleSchema().load(json).data
    repo.add(role)
    Container.instance().current_app.unitofwork.commit()
    return jsonify({'message': 'Role created.'}), 201


@api.route('/roles/<int:id>/', methods=['PUT'])
@auth_token.login_required
def put_role(id):
    repo = Container.instance().current_app.unitofwork.get_repository('RoleRepository')
    role = repo.query().get(id)
    if role is None:
        abort(404)
    json = loads(request.json) if isinstance(request.json, str) else request.json
    errors = RoleSchema().validate(json)
    if errors:
        raise ValidationResponseError(errors)
    new = RoleSchema().load(json).data
    if repo.query().filter(lambda x: x.name == new.name and x.id != id).first() is not None:
        raise ValidationResponseError({'name': ['Name already in use.']})
    role.name = new.name
    repo.add(role)
    Container.instance().current_app.unitofwork.commit()
    return jsonify({'message': 'Role updated.'}), 201


@api.route('/roles/<int:id>/', methods=['DELETE'])
@auth_token.login_required
def delete_role(id):
    repo = Container.instance().current_app.unitofwork.get_repository('RoleRepository')
    role = repo.query().get(id)
    if role is None:
        abort(404)
    repo.delete(role)
    Container.instance().current_app.unitofwork.commit()
    return jsonify({'message': 'Role deleted.'})
