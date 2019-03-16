from flask import jsonify
from . import api
from ..auth import auth_token
from ..database import Course


@api.route('/courses')
@auth_token.login_required
def get_courses():
    courses = Course.query.all()
    return jsonify([{
        'id': course.id,
        'name': course.name
    } for course in courses])
