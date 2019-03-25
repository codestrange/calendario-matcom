from datetime import timedelta
from flask import jsonify, request
from . import api
from ..auth import auth_token
from ..database import Event, User, Course, Group, Local, Resource, Tag, db
from ..errors import bad_request
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
    if 'start' in json:
        json.start -= timedelta(hours=4)
    if 'end' in json:
        json.end -= timedelta(hours=4)
    return jsonify([{
        'id': event.id,
        'title': event.title,
        'description': event.description,
        'start': event.start,
        'end': event.end
    } for event in events if check_date(event, json)])


@api.route('/events', methods=['POST'])
@auth_token.login_required
def post_event():
    json = json_load(request.json)
    check_json(json, ['title', 'description', 'start', 'end', 'courses', 'groups', 'locals',
                      'resources', 'tags'])
    if Event.query.filter_by(title=json.title).first():
        return bad_request('Ya existe un evento con el mismo título.')
    events = Event.query.filter(json.start <= Event.start).filter(Event.end <= json.end).all()
    ok = True
    for group_id in json.groups:
        for event in events:
            for group in event.groups:
                if group.id == group_id:
                    ok = False
    for local_id in json.locals:
        for event in events:
            for local in event.locals:
                if local.id == local_id:
                    ok = False
    for resource_id in json.resources:
        for event in events:
            for resource in event.resources:
                if resource.id == resource_id:
                    ok = False
    if ok:
        event = Event()
        event.title = json.title
        event.description = json.description
        event.start = json.start
        event.end = json.end
        for identifier in json.courses:
            item = Course.query.get_or_404(identifier)
            event.courses.append(item)
        for identifier in json.groups:
            item = Group.query.get_or_404(identifier)
            event.groups.append(item)
        for identifier in json.locals:
            item = Local.query.get_or_404(identifier)
            event.locals.append(item)
        for identifier in json.resources:
            item = Resource.query.get_or_404(identifier)
            event.resources.append(item)
        for identifier in json.tags:
            item = Tag.query.get_or_404(identifier)
            event.tags.append(item)
        db.session.add(event)
        db.session.commit()
        return jsonify({'message': 'Evento creado correctamente.'}), 201
    return bad_request('No es posible crear el evento.')


@api.route('/events', methods=['PUT'])
@auth_token.login_required
def put_event():
    json = json_load(request.json)
    check_json(json, ['id', 'title', 'description', 'start', 'end', 'courses', 'groups', 'locals',
                      'resources', 'tags'])
    old_event = Event.query.get_or_404(json.id)
    db.session.delete(old_event)
    db.session.commit()
    if Event.query.filter_by(title=json.title).first():
        return bad_request('Ya existe un evento con el mismo título.')
    events = Event.query.filter(json.start <= Event.start).filter(Event.end <= json.end).all()
    ok = True
    for group_id in json.groups:
        for event in events:
            for group in event.groups:
                if group.id == group_id:
                    ok = False
    for local_id in json.locals:
        for event in events:
            for local in event.locals:
                if local.id == local_id:
                    ok = False
    for resource_id in json.resources:
        for event in events:
            for resource in event.resources:
                if resource.id == resource_id:
                    ok = False
    if ok:
        event = Event()
        event.title = json.title
        event.description = json.description
        event.start = json.start
        event.end = json.end
        for identifier in json.courses:
            item = Course.query.get_or_404(identifier)
            event.courses.append(item)
        for identifier in json.groups:
            item = Group.query.get_or_404(identifier)
            event.groups.append(item)
        for identifier in json.locals:
            item = Local.query.get_or_404(identifier)
            event.locals.append(item)
        for identifier in json.resources:
            item = Resource.query.get_or_404(identifier)
            event.resources.append(item)
        for identifier in json.tags:
            item = Tag.query.get_or_404(identifier)
            event.tags.append(item)
        db.session.add(event)
        db.session.commit()
        return jsonify({'message': 'Evento cambiado correctamente.'}), 201
    return bad_request('No es posible cambiar el evento.')


@api.route('/events/<int:id>', methods=['DELETE'])
@auth_token.login_required
def delete_event(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({'message': 'Evento eliminado correctamente.'}), 201


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
