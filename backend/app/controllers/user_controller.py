from flask import jsonify, request, g
from . import api
from ..auth import auth_token
from ..database import db, User
from ..errors import bad_request
from ..utils import check_json, json_load


@api.route('/profile', methods=['GET'])
@auth_token.login_required
def get_profile():
    user = g.current_user
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'confirmed': user.confirmed,
        'activated': user.activated
    })


@api.route('/register', methods=['POST'])
def register():
    json = json_load(request.json)
    response = check_json(json, ['username', 'email', 'password'])
    if response:
        return response
    user = User(json.username, json.email, json.password)
    if User.query.filter_by(username=user.username).first():
        return bad_request({'message': 'the username is already registered'})
    if User.query.filter_by(email=user.email).first():
        return bad_request({'message': 'the email is already registered'})
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'user registered'}), 201
