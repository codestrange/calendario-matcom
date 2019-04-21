from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash


db = SQLAlchemy(session_options={"autoflush": False})


class Permission(object):
    VIEW_PANEL = 0b00000000000000000000000000000001
    CREATE_EVENT = 0b00000000000000000000000000000010
    UPDATE_EVENT = 0b00000000000000000000000000000100
    DELETE_EVENT = 0b00000000000000000000000000001000
    ADMINISTER = 0b11111111111111111111111111111111


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
    career = db.Column(db.String(64), nullable=True)
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
    default = db.Column(db.Boolean, default=False, index=True)
    users = db.relationship('User', secondary=user_group, backref=db.backref('groups'))
    events = db.relationship('Event', secondary=event_group, backref=db.backref('groups'))
    notifications = db.relationship('UserGroupNotification',
                                    foreign_keys=[UserGroupNotification.group_id], backref='group')

    @staticmethod
    def insert():
        groups = Group.query.all()
        for group in groups:
            db.session.delete(group)
        db.session.commit()
        group_all = Group()
        group_all.name = 'all'
        group_all.default = True
        db.session.add(group_all)
        db.session.commit()

    def __repr__(self):
        return f'{self.name}'


class Interval(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    start = db.Column(db.Time, nullable=False)
    end = db.Column(db.Time, nullable=False)

    @staticmethod
    def insert():
        intervals = Interval.query.all()
        for interval in intervals:
            db.session.delete(interval)
        db.session.commit()
        intervals = []
        for i in range(1, 7):
            interval = Interval()
            interval.name = f'Turno {i}'
            intervals.append(interval)
        datetimes = [datetime(1, 1, 1, 8)] + [None] * 11
        length_event = timedelta(minutes=95)
        length_change = timedelta(minutes=10)
        for i in range(1, 12):
            datetimes[i] = datetimes[i - 1] + (length_event if i % 2 else length_change)
        for i in range(0, 12, 2):
            intervals[i // 2].start = datetimes[i].time()
            intervals[i // 2].end = datetimes[i + 1].time()
        for interval in intervals:
            db.session.add(interval)
        db.session.commit()

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
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert():
        roles = Role.query.all()
        for r in roles:
            db.session.delete(r)
        db.session.commit()
        roles = [
            ('user', 0, True),
            ('moderator', Permission.VIEW_PANEL | Permission.CREATE_EVENT | 
             Permission.UPDATE_EVENT | Permission.DELETE_EVENT, False),
            ('administrator', Permission.ADMINISTER, False)
        ]
        for r in roles:
            role = Role(name=r[0])
            role.permissions = r[1]
            role.default = r[2]
            db.session.add(role)
        db.session.commit()

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
    confirmed = db.Column(db.Boolean, default=False)
    activated = db.Column(db.Boolean, default=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
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

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        role = Role.query.filter_by(default=True).first()
        role.users.append(self)
        group = Group.query.filter_by(default=True).first()
        group.users.append(self)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def can(self, permissions):
        return self.role is not None and (self.role.permissions & permissions) == permissions

    def __repr__(self):
        return f'{self.username}'


class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    body = db.Column(db.Text, nullable=False)
    options = db.relationship('Option', backref='vote')

    def __repr__(self):
        return f'{self.title}'
