from flask import jsonify
from . import api
from ..auth import auth_token
from ..database import Group


@api.route('/groups')
@auth_token.login_required
def get_groups():
    groups = Group.query.all()
    return jsonify([{
        'id': group.id,
        'name': group.name
    } for group in groups])
