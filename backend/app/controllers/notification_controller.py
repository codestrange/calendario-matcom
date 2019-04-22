from flask import g, jsonify
from . import api
from ..auth import auth_token
from ..database import db, Notification


@api.route('/notifications')
@auth_token.login_required
def get_notifications():
    user = g.current_user
    notifications = user.notifications
    result = []
    mask = set()
    for item in notifications:
        noti = item.notification
        group = item.group
        if noti.id in mask:
            _notif = next(filter(lambda x: x['id'] == noti.id, result))
            if group.name != 'all':
                _notif['groups'].append({'id': group.id, 'name': group.name})
            _notif['seened'] = _notif['seened'] and item.seened
            continue
        mask.add(noti.id)
        result.append({
            'id': noti.id,
            'title': noti.title,
            'body': noti.body,
            'date': noti.date,
            'seened': item.seened,
            'groups': [{'id': group.id, 'name': group.name}]
        })
    result.reverse()
    return jsonify(result)


@api.route('/notifications/seen/<int:id>', methods=['POST'])
@auth_token.login_required
def seen_notification(id):
    user = g.current_user
    noti = Notification.query.get_or_404(id)
    for item in noti.notifications:
        if item.user.id == user.id:
            item.seened = True
    db.session.add(noti)
    db.session.commit()
    return jsonify({'message': 'Notificación marcada como vista correctamente.'}), 201
