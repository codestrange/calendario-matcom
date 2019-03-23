from os import getenv
from app import create_app
from app.database import db, Course, Event, Group, Interval, Local, Notification, Option, \
    Permission, Resource, Role, Student, Tag, Teacher, User, Vote, UserGroupNotification

app = create_app(getenv('FLASK_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, Course=Course, Event=Event, Group=Group, Interval=Interval,
                Local=Local, Notification=Notification, Option=Option, Permission=Permission,
                Resource=Resource, Role=Role, Student=Student, Tag=Tag, Teacher=Teacher,
                User=User, Vote=Vote, UserGroupNotification=UserGroupNotification)
