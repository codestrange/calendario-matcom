from flask import jsonify
from . import api
from ..auth import auth_token
from ..database import Interval


@api.route('/intervals')
@auth_token.login_required
def get_intervals():
    intervals = Interval.query.all()
    return jsonify([{
        'id': interval.id,
        'name': interval.name,
        'start': str(interval.start),
        'end': str(interval.end)
    } for interval in intervals])
