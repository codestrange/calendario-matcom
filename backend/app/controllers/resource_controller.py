from flask import jsonify
from . import api
from ..auth import auth_token
from ..database import Resource


@api.route('/resources')
@auth_token.login_required
def get_resources():
    resources = Resource.query.all()
    return jsonify([{
        'id': resource.id,
        'name': resource.name
    } for resource in resources])
