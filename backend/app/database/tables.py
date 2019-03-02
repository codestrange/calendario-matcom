from sqlalchemy import Table, Column, Integer, Unicode, DateTime, ForeignKey


def get_user_table(metadata):
    return Table('user', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('username', Unicode(64), unique=True, nullable=False),
                 Column('email', Unicode(64), unique=True, nullable=False),
                 Column('password_hash', Unicode(128), nullable=False))


# Agregarle un campor Integer para que contenga la informacion de los permisos
# en tiempo constante
def get_role_table(metadata):
    return Table('role', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', Unicode(64), unique=True, nullable=False))


# Agregarle un campo Integer que sea el codigo para luego desde la tabla Role
# poder saber si tiene un permiso especifico en tiempo constate
def get_permission_table(metadata):
    return Table('permission', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', Unicode(64), unique=True, nullable=False))


def get_student_table(metadata):
    return Table('student', metadata,
                 Column('id', None, ForeignKey('user.id'), primary_key=True),
                 Column('career', Unicode(128), nullable=False))


def get_teacher_table(metadata):
    return Table('teacher', metadata,
                 Column('id', None, ForeignKey('user.id'), primary_key=True),
                 Column('department', Unicode(128), nullable=False))


def get_option_table(metadata):
    return Table('option', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('text', Unicode(256), nullable=False),
                 Column('vote_id', None, ForeignKey('vote.id')))


def get_vote_table(metadata):
    return Table('vote', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('title', Unicode(64), nullable=False),
                 Column('body', Unicode(256), nullable=False))


def get_notification_table(metadata):
    return Table('notification', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('text', Unicode(256), nullable=False),
                 Column('datetime', DateTime, nullable=False))


def get_group_table(metadata):
    return Table('group', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', Unicode(64), unique=True, nullable=False))


def get_course_table(metadata):
    return Table('course', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', Unicode(64), unique=True, nullable=False),
                 Column('hours_class', Integer, nullable=False),
                 Column('year', Integer, nullable=False),
                 Column('semester', Integer, nullable=False))


def get_event_table(metadata):
    return Table('event', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('title', Unicode(64), nullable=False),
                 Column('description', Unicode(256), nullable=False),
                 Column('start', DateTime, nullable=False),
                 Column('end', DateTime, nullable=False))


def get_tag_table(metadata):
    return Table('tag', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('text', Unicode(64), unique=True, nullable=False))


def get_local_table(metadata):
    return Table('local', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', Unicode(64), unique=True, nullable=False),
                 Column('size', Integer, nullable=False))


def get_resource_table(metadata):
    return Table('resource', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', Unicode(64), unique=True, nullable=False),
                 Column('kind', Unicode(64), nullable=False))


def get_user_role_table(metadata):
    return Table('user_role', metadata,
                 Column('user_id', None, ForeignKey('user.id'), primary_key=True),
                 Column('role_id', None, ForeignKey('role.id'), primary_key=True))


def get_user_group_table(metadata):
    return Table('user_group', metadata,
                 Column('user_id', None, ForeignKey('user.id'), primary_key=True),
                 Column('group_id', None, ForeignKey('group.id'), primary_key=True))


def get_role_permission_table(metadata):
    return Table('role_permission', metadata,
                 Column('role_id', None, ForeignKey('role.id'), primary_key=True),
                 Column('permission_id', None, ForeignKey('permission.id'), primary_key=True))


def get_user_option_table(metadata):
    return Table('user_option', metadata,
                 Column('user_id', None, ForeignKey('user.id'), primary_key=True),
                 Column('option_id', None, ForeignKey('option.id'), primary_key=True))


def get_event_course_table(metadata):
    return Table('event_course', metadata,
                 Column('event_id', None, ForeignKey('event.id'), primary_key=True),
                 Column('course_id', None, ForeignKey('course.id'), primary_key=True))


def get_event_group_table(metadata):
    return Table('event_group', metadata,
                 Column('event_id', None, ForeignKey('event.id'), primary_key=True),
                 Column('group_id', None, ForeignKey('group.id'), primary_key=True))


def get_event_local_table(metadata):
    return Table('event_local', metadata,
                 Column('event_id', None, ForeignKey('event.id'), primary_key=True),
                 Column('local_id', None, ForeignKey('local.id'), primary_key=True))


def get_event_resource_table(metadata):
    return Table('event_resource', metadata,
                 Column('event_id', None, ForeignKey('event.id'), primary_key=True),
                 Column('resource_id', None, ForeignKey('resource.id'), primary_key=True))


def get_event_tag_table(metadata):
    return Table('event_tag', metadata,
                 Column('event_id', None, ForeignKey('event.id'), primary_key=True),
                 Column('tag_id', None, ForeignKey('tag.id'), primary_key=True))


def get_user_group_notification_table(metadata):
    return Table('user_group_notification', metadata,
                 Column('user_id', None, ForeignKey('user.id'), primary_key=True),
                 Column('group_id', None, ForeignKey('group.id'), primary_key=True),
                 Column('notification_id', None, ForeignKey('notification.id'), primary_key=True))
