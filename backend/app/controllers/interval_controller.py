from flask import jsonify
from . import api
from ..database import Interval


@api.route('/intervals')
def get_intervals():
    intervals = Interval.query.all()
    return jsonify([{
        'id': interval.id,
        'name': interval.name,
        'start': str(interval.start),
        'end': str(interval.end)
    } for interval in intervals])
