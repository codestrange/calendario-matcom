from flask import jsonify, g
from . import api
from ..auth import auth, generate_auth_token


@api.route('/token/')
@auth.login_required
def get_token():
    return jsonify({
        'id': g.current_user.id,
        'token': generate_auth_token(g.current_user)
    })
