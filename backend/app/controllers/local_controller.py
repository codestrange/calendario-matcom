from flask import jsonify
from . import api
from ..auth import auth_token
from ..database import Local


@api.route('/locals')
@auth_token.login_required
def get_locals():
    locals = Local.query.all()
    return jsonify([{
        'id': local.id,
        'name': local.name
    } for local in locals])


@api.route('/locals/<int:id>')
@auth_token.login_required
def get_local(id):
    local = Local.query.get_or_404(id)
    events = [{'id': event.id, 'title': event.title} for event in local.events]
    return jsonify({
        'id': local.id,
        'name': local.name,
        'events': events
    })
