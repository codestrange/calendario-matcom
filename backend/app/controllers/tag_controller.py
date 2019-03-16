from flask import jsonify
from . import api
from ..auth import auth_token
from ..database import Tag


@api.route('/tags')
@auth_token.login_required
def get_tags():
    tags = Tag.query.all()
    return jsonify([{
        'id': tag.id,
        'text': tag.text
    } for tag in tags])
