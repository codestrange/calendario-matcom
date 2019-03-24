from flask import jsonify, request
from . import api
from ..auth import auth_token
from ..database import Local
from .. utils import json_load, check_json, check_outside, get_date


@api.route('/locals')
@auth_token.login_required
def get_locals():
    locals = Local.query.all()
    return jsonify([{
        'id': local.id,
        'name': local.name
    } for local in locals])


@api.route('/locals/free')
#@auth_token.login_required
def get_free_locals():
    json = json_load(request.json)
    check_json(json, ['start', 'end'])
    print(get_date(json.start))
    print(get_date(json.end))
    free_locals = []
    _locals = Local.query.all()
    for local in _locals:
        valid = True
        for event in local.events:
            if not check_outside(event, json):
                valid = False
                break
        if valid:
            free_locals.append(local)
    return jsonify([{
        "id": local.id,
        "name": local.name
    } for local in free_locals])


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
