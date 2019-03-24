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
        'name': course.name,
        'year': course.year,
        'semester': course.semester,
        'career': course.career
    } for course in courses])


@api.route('/courses/<int:id>')
@auth_token.login_required
def get_course(id):
    course = Course.query.get_or_404(id)
    events = [{'id': event.id, 'title': event.title} for event in course.events]
    teachers = [{
        'id': teacher.user.id,
        'username': teacher.user.username
    } for teacher in course.teachers]
    return jsonify({
        'id': course.id,
        'name': course.name,
        'year': course.year,
        'semester': course.semester,
        'career': course.career
        'events': events,
        'teachers': teachers
    })
