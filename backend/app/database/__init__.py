from sqlalchemy import MetaData, Table, Column, Integer, Unicode, DateTime
from sqlalchemy.orm import sessionmaker


def get_user_table(metadata):
    return Table('user', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('username', Unicode(64), unique=True, nullable=False),
                 Column('email', Unicode(64), unique=True, nullable=False),
                 Column('password_hash', Unicode(128), nullable=False),
                 Column('firstname', Unicode(64), nullable=False),
                 Column('lastname', Unicode(64), nullable=False))


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
                 Column('id', Integer, primary_key=True),
                 Column('career', Unicode(128), nullable=False))


def get_teacher_table(metadata):
    return Table('teacher', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('department', Unicode(128), nullable=False))


def get_option_table(metadata):
    return Table('option', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('text', Unicode(256), nullable=False))


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


class Database:
    def __init__(self, metadata=None, session=None):
        self.session = session
        self.metadata = metadata

    def init_app(self, app):
        if self.metadata is None:
            self.metadata = MetaData(app.config['DATABASE_URL'])

        user_table = get_user_table(self.metadata)
        role_table = get_role_table(self.metadata)
        permission_table = get_permission_table(self.metadata)
        student_table = get_student_table(self.metadata)
        teacher_table = get_teacher_table(self.metadata)
        option_table = get_option_table(self.metadata)
        vote_table = get_vote_table(self.metadata)
        notification_table = get_notification_table(self.metadata)

        self.metadata.create_all()

        if self.session is None:
            Session = sessionmaker()
            self.session = Session()

        app.db = self
