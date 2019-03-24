from flask import jsonify, request
from . import api
from ..auth import auth_token
from ..database import Group
from ..utils import json_load, check_json


@api.route('/groups')
@auth_token.login_required
def get_groups():
    groups = Group.query.all()
    return jsonify([{
        'id': group.id,
        'name': group.name
    } for group in groups])


@api.route('/groups/<int:id>')
@auth_token.login_required
def get_group(id):
    group = Group.query.get_or_404(id)
    events = [{'id': event.id, 'title': event.title} for event in group.events]
    users = [{'id': user.id, 'username': user.username} for user in group.users]
    return jsonify({
        'id': group.id,
        'name': group.name,
        'events': events,
        'users': users
    })
