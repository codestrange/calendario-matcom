from flask import jsonify, request
from datetime import datetime, timedelta
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


def get_date(str_date):
    year = int(str_date.split('-')[0])
    month = int(str_date.split('-')[1])
    day = int(str_date.split('-')[2].split('T')[0])
    hour = int(str_date.split('T')[1].split(':')[0])
    minute = int(str_date.split('T')[1].split(':')[1])
    second = int(str_date.split('T')[1].split(':')[2].split('.')[0])
    return datetime(year, month, day, hour, minute, second) - timedelta(hours=4)


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
        left = get_date(json.start) <= event.start
    if 'end' in json:
        right = event.end <= get_date(json.end)
    return left and right


@api.route('/events', methods=['POST'])
@auth_token.login_required
def query_events():
    json = json_load(request.json)
    check_json(json, ['courses', 'groups', 'locals', 'resources', 'tags', 'users'])
    all_events = Event.query.all()
    users = [user for user in User.query.all() if user.id in json.users]
    for user in users:
        for group in user.groups:
            if not group.id in json.groups:
                json.groups.append(group.id)
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


@api.route('/events/<int:id>')
@auth_token.login_required
def get_event(id):
    event = Event.query.get_or_404(id)
    event_courses = [{'id': course.id, 'name': course.name} for course in event.courses]
    event_groups = [{'id': group.id, 'name': group.name} for group in event.groups]
    event_locals = [{'id': local.id, 'name': local.name} for local in event.locals]
    event_resources = [{'id': resource.id, 'name': resource.name} for resource in event.resources]
    event_tags = [{'id': tag.id, 'text': tag.text} for tag in event.tags]
    return jsonify({
        'id': event.id,
        'title': event.title,
        'description': event.description,
        'start': event.start,
        'end': event.end,
        'courses': event_courses,
        'groups': event_groups,
        'locals': event_locals,
        'resources': event_resources,
        'tags': event_tags
    })
