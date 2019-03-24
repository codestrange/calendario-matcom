from flask import jsonify, request
from . import api
from ..auth import auth_token
from ..database import Event, User
from ..utils import check_json, query, merge, check_date, json_load


@api.route('/events/query', methods=['POST'])
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


@api.route('/events')
@auth_token.login_required
def get_events():
    events = Event.query.all()
    return jsonify([{
        'id': event.id,
        'title': event.title
    } for event in events])


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
