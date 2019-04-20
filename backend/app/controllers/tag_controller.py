from flask import jsonify
from . import api
from ..database import Tag


@api.route('/tags')
def get_tags():
    tags = Tag.query.all()
    return jsonify([{
        'id': tag.id,
        'text': tag.text
    } for tag in tags])


@api.route('/tags/<int:id>')
def get_tag(id):
    tag = Tag.query.get_or_404(id)
    events = [{'id': event.id, 'title': event.title} for event in tag.events]
    return jsonify({
        'id': tag.id,
        'text': tag.text,
        'events': events
    })
