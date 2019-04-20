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
        'activated': g.current_user.activated,
        'role': g.current_user.role.permissions
    })


@api.route('/profile/edit', methods=['PUT'])
@auth_token.login_required
def edit_profil():
    json = json_load(request.json)
    user = User.query.get(g.current_user.id)
    if 'username' in json:
        equal_name = User.query.filter_by(username=json.username).filter(User.id != user.id).first()
        if equal_name is None:
            user.username = json.username
            db.session.add(user)
            db.session.commit()
        else:
            return bad_request('Ya existe un usuario con ese nombre')
    if 'password' in json:
        user.password = json.password
        db.session.add(user)
        db.session.commit()
    if 'email' in json:
        equal_email = User.query.filter_by(email=json.email).filter(User.id != user.id).first()
        if equal_email is None:
            user.email = json.email
            db.session.add(user)
            db.session.commit()
        else:
            return bad_request('Ya existe un usuario con ese correo')
    # if 'first_name' in json:
    #     user.first_name = json.first_name
    #     db.session.add(user)
    #     db.session.commit()

    # if 'last_name' in json:
    #     user.last_name = json.last_name
    #     db.session.add(user)
    #     db.session.commit()
    return jsonify({'message': 'Su perfil se ha editado correctamente'}), 201


@api.route('/users')
def get_users():
    users = User.query.all()
    return jsonify([{
        'id': user.id,
        'username': user.username,
        'is_teacher': not user.teacher is None,
        'is_student': not user.student is None
    } for user in users])


@api.route('/users/<int:id>')
def get_user(id):
    user = User.query.get_or_404(id)
    groups = [{'id': group.id, 'name': group.name} for group in user.groups]
    return jsonify({
        'id': user.id,
        'username': user.username,
        'groups': groups
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
