from flask import jsonify,request
from . import api
from ..auth import auth_token
from ..database import Local
from ..utils import check_json, json_load
from .event_controller import get_date

def check_date1(event, json):   
    left = right = True
    if 'start' in json and not 'end' in json:    
        left = right = event.end <= get_date(json.start)
    elif 'end' in json and not 'start' in json:
        left = right = event.start >= get(json.end)
    elif 'start' in json and 'end' in json:
        left = right = (event.end <= get_date(json.start) or event.start >= get_date(json.end) )             
    return left and right


@api.route('/locals')
@auth_token.login_required
def get_locals():
    json = json_load(request.json)       
    locals = Local.query.all()    
    free_locals = []
    for local in locals:        
        valid = True
        events_at = local.events
        for event in events_at:
            if not check_date1(event,json):
                valid = False
                break
        if valid:
            free_locals.append(local)
    return jsonify([{
        'id': local.id,
        'local': local.name,
        'size': local.size}
        for local in free_locals])  


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
