from flask import jsonify, request
from . import api
from ..auth import auth_token
from ..database import Event, User
from ..utils import check_json, json_load


def query(items, events, attr):
    result = []
    if items:
        for event in events:
            for item in attr(event):
                if item.id in items:
                    result.append(event)
                    break
    else:
        result = events
    return result


def merge(left, right):
    result = []
    ids = [item.id for item in right]
    for item in left:
        if item.id in ids:
            result.append(item)
    return result


def check_date(event, json):
    left = right = True
    if 'start' in json:
        left = json.start <= event.start
    if 'end' in json:
        right = event.end <= json.end
    return left and right


@api.route('/events')
@auth_token.login_required
def get_events():
    json = json_load(request.json)
    check_json(json, ['courses', 'groups', 'locals', 'resources', 'tags', 'users'])
    all_events = Event.query.all()
    users = [user for user in User.query.all() if user.id in json.users]
    for user in users:
        for group in user.groups:
            if not group.id in json.groups:
                json.groups.append(group.id)
    print(json.groups)
    events = query(json.courses, all_events, lambda x: x.courses)
    events = merge(events, query(json.groups, all_events, lambda x: x.groups))
    events = merge(events, query(json.locals, all_events, lambda x: x.locals))
    events = merge(events, query(json.resources, all_events, lambda x: x.resources))
    events = merge(events, query(json.tags, all_events, lambda x: x.tags))
    return jsonify([{
        'id': event.id,
        'title': event.title,
        'description': event.description,
        'start': event.start,
        'end': event.end
    } for event in events if check_date(event, json)])
