from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash


db = SQLAlchemy()

user_role = db.Table('user_role',
                     db.Column('user_id',
                               db.Integer, db.ForeignKey('user.id'), primary_key=True),
                     db.Column('role_id',
                               db.Integer, db.ForeignKey('role.id'), primary_key=True))

user_group = db.Table('user_group',
                      db.Column('user_id',
                                db.Integer, db.ForeignKey('user.id'), primary_key=True),
                      db.Column('group_id',
                                db.Integer, db.ForeignKey('group.id'), primary_key=True))

user_option = db.Table('user_option',
                       db.Column('user_id',
                                 db.Integer, db.ForeignKey('user.id'), primary_key=True),
                       db.Column('option_id',
                                 db.Integer, db.ForeignKey('option.id'), primary_key=True))

role_permission = db.Table('role_permission',
                           db.Column('role_id',
                                     db.Integer, db.ForeignKey('role.id'), primary_key=True),
                           db.Column('permission_id',
                                     db.Integer, db.ForeignKey('permission.id'), primary_key=True))

event_course = db.Table('event_course',
                        db.Column('event_id',
                                  db.Integer, db.ForeignKey('event.id'), primary_key=True),
                        db.Column('course_id',
                                  db.Integer, db.ForeignKey('course.id'), primary_key=True))

event_group = db.Table('event_group',
                       db.Column('event_id',
                                 db.Integer, db.ForeignKey('event.id'), primary_key=True),
                       db.Column('group_id',
                                 db.Integer, db.ForeignKey('group.id'), primary_key=True))

event_local = db.Table('event_local',
                       db.Column('event_id',
                                 db.Integer, db.ForeignKey('event.id'), primary_key=True),
                       db.Column('local_id',
                                 db.Integer, db.ForeignKey('local.id'), primary_key=True))

event_resource = db.Table('event_resource',
                          db.Column('event_id',
                                    db.Integer, db.ForeignKey('event.id'), primary_key=True),
                          db.Column('resource_id',
                                    db.Integer, db.ForeignKey('resource.id'), primary_key=True))

event_tag = db.Table('event_tag',
                     db.Column('event_id',
                               db.Integer, db.ForeignKey('event.id'), primary_key=True),
                     db.Column('tag_id',
                               db.Integer, db.ForeignKey('tag.id'), primary_key=True))

teacher_course = db.Table('teacher_course',
                          db.Column('teacher_id',
                                    db.Integer, db.ForeignKey('teacher.id'), primary_key=True),
                          db.Column('course_id',
                                    db.Integer, db.ForeignKey('course.id'), primary_key=True))


class UserGroupNotification(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True)
    notification_id = db.Column(db.Integer, db.ForeignKey('notification.id'), primary_key=True)

    def __repr__(self):
        return f'{self.user.username, self.group.name, self.notification.title}'


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    hour_class = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    events = db.relationship('Event', secondary=event_course, backref='courses')

    def __repr__(self):
        return f'{self.name}'


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.Text)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'{self.title}'


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    users = db.relationship('User', secondary=user_group, backref=db.backref('groups'))
    events = db.relationship('Event', secondary=event_group, backref=db.backref('groups'))
    notifications = db.relationship('UserGroupNotification',
                                    foreign_keys=[UserGroupNotification.group_id], backref='group')

    def __repr__(self):
        return f'{self.name}'


class Local(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    size = db.Column(db.Integer, nullable=False)
    events = db.relationship('Event', secondary=event_local, backref='locals')

    def __repr__(self):
        return f'{self.name}'


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    body = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    notifications = db.relationship('UserGroupNotification',
                                    foreign_keys=[UserGroupNotification.notification_id],
                                    backref='notification')

    def __repr__(self):
        return f'{self.title}'


class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(256), nullable=False)
    vote_id = db.Column(db.Integer, db.ForeignKey('vote.id'), nullable=False)
    users = db.relationship('User', secondary=user_option, backref='options')

    def __repr__(self):
        return f'{self.text}'


class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    roles = db.relationship('Role', secondary=role_permission, backref='permissions')

    def __repr__(self):
        return f'{self.name}'


class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    kind = db.Column(db.String(64), nullable=False)
    events = db.relationship('Event', secondary=event_resource, backref='resources')

    def __repr__(self):
        return f'{self.name}'


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    users = db.relationship('User', secondary=user_role, backref='roles')

    def __repr__(self):
        return f'{self.name}'


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carrer = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'{self.user.username}'


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(64), unique=True, nullable=False)
    events = db.relationship('Event', secondary=event_tag, backref='tags')

    def __repr__(self):
        return f'{self.text}'


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    courses = db.relationship('Course', secondary=teacher_course, backref='teachers')

    def __repr__(self):
        return f'{self.user.username}'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    student = db.relationship('Student', backref='user', uselist=False)
    teacher = db.relationship('Teacher', backref='user', uselist=False)
    notifications = db.relationship('UserGroupNotification',
                                    foreign_keys=[UserGroupNotification.user_id], backref='user')


    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'{self.username}'


class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    body = db.Column(db.Text, nullable=False)
    options = db.relationship('Option', backref='vote')

    def __repr__(self):
        return f'{self.title}'
