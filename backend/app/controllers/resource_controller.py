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


@api.route('/resources/<int:id>')
@auth_token.login_required
def get_resource(id):
    resource = Resource.query.get_or_404(id)
    events = [{'id': event.id, 'title': event.title} for event in resource.events]
    return jsonify({
        'id': resource.id,
        'name': resource.name,
        'events': events
    })
