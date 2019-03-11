from flask_sqlalchemy import Model, SQLAlchemy
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declared_attr
from werkzeug.security import check_password_hash, generate_password_hash


class IdModel(Model):
    @declared_attr
    def id(self):
        return Column(Integer, primary_key=True)


db = SQLAlchemy(model_class=IdModel)

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


class Course(db.Model):
    name = db.Column(db.String(64), unique=True, nullable=False)
    hour_class = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    events = db.relationship('Event', secondary=event_course,
                             lazy=True, backref=db.backref('courses', lazy=True))


class Event(db.Model):
    title = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.Text)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)


class Group(db.Model):
    name = db.Column(db.String(64), unique=True, nullable=False)
    users = db.relationship('User', secondary=user_group,
                            lazy=True, backref=db.backref('groups', lazy=True))
    events = db.relationship('Event', secondary=event_group,
                             lazy=True, backref=db.backref('groups', lazy=True))


class Local(db.Model):
    name = db.Column(db.String(64), unique=True, nullable=False)
    size = db.Column(db.Integer, nullable=False)
    events = db.relationship('Event', secondary=event_local,
                             lazy=True, backref=db.backref('locals', lazy=True))


class Notification(db.Model):
    title = db.Column(db.String(256), nullable=False)
    body = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)


class Option(db.Model):
    text = db.Column(db.String(256), nullable=False)
    vote_id = db.Column(db.Integer, db.ForeignKey('vote.id'), nullable=False)
    users = db.relationship('User', secondary=user_option,
                            lazy=True, backref=db.backref('options', lazy=True))


class Permission(db.Model):
    name = db.Column(db.String(64), unique=True, nullable=False)
    roles = db.relationship('Role', secondary=role_permission,
                            lazy=True, backref=db.backref('permissions', lazy=True))


class Resource(db.Model):
    name = db.Column(db.String(64), unique=True, nullable=False)
    kind = db.Column(db.String(64), nullable=False)
    events = db.relationship('Event', secondary=event_resource,
                             lazy=True, backref=db.backref('resources', lazy=True))


class Role(db.Model):
    name = db.Column(db.String(64), unique=True, nullable=False)
    users = db.relationship('User', secondary=user_role,
                            lazy=True, backref=db.backref('roles', lazy=True))


class Student(db.Model):
    carrer = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Tag(db.Model):
    text = db.Column(db.String(64), unique=True, nullable=False)
    events = db.relationship('Event', secondary=event_tag,
                             lazy=True, backref=db.backref('tags', lazy=True))


class Teacher(db.Model):
    department = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    courses = db.relationship('Course', secondary=teacher_course,
                              lazy=True, backref=db.backref('teachers', lazy=True))


class User(db.Model):
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    student = db.relationship('Student', backref='user', lazy=True, uselist=False)
    teacher = db.relationship('Teacher', backref='user', lazy=True, uselist=False)

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Vote(db.Model):
    title = db.Column(db.String(256), nullable=False)
    body = db.Column(db.Text, nullable=False)
    options = db.relationship('Option', backref='vote', lazy=True)
