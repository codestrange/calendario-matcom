from flask import jsonify
from . import api
from ..database import Course


@api.route('/courses')
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
        'career': course.career,
        'events': events,
        'teachers': teachers
    })
