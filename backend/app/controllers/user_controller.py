from flask import jsonify, request, g
from . import api
from ..auth import auth, auth_simple, auth_token, generate_auth_token, \
    generate_confirmation_token, verify_confirmation_token
from ..database import db, User
from ..errors import bad_request
from ..utils import check_json, json_load


@api.route('/token')
@auth.login_required
def get_token():
    return jsonify({'token': generate_auth_token(g.current_user)})


@api.route('/profile')
@auth_token.login_required
def get_profile():
    return jsonify({
        'id': g.current_user.id,
        'username': g.current_user.username,
        'email': g.current_user.email,
        'confirmed': g.current_user.confirmed,
        'activated': g.current_user.activated
    })


@api.route('/register', methods=['POST'])
def post_register():
    json = json_load(request.json)
    check_json(json, ['username', 'email', 'password'])
    user = User(username=json.username, email=json.email, password=json.password)
    if User.query.filter_by(username=user.username).first():
        return bad_request('El nombre de usuario ya está registrado.')
    if User.query.filter_by(email=user.email).first():
        return bad_request('El correo electrónico ya está registrado')
    # temporal
    user.confirmed = True
    db.session.add(user)
    db.session.commit()
    token = generate_confirmation_token(user)
    print(f'\nToken: {token}\n')
    # send email
    return jsonify({'message': 'Usuario registrado aún sin confirmar.'}), 201


@api.route('/confirm', methods=['POST'])
@auth_simple.login_required
def post_confirm():
    json = json_load(request.json)
    check_json(json, ['token'])
    if g.current_user.confirmed:
        return bad_request('El usuario ya esta confirmado.')
    user = verify_confirmation_token(json.token)
    if user and user.id == g.current_user.id:
        user.confirmed = True
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'Usuario confirmado.'}), 201
    else:
        return bad_request('El enlace de confirmación es invalido o ha expirado.')
