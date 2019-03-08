from werkzeug.security import generate_password_hash

class CourseEntity:
    def __init__(self, name, year, freq, sem, id=None):
        self.id = id
        self.name = name
        self.year = year
        self.freq = freq
        self.sem = sem
        self.events = []


class EventEntity:
    def __init__(self, title, description, start_date, end_date, id=None):
        self.id = id
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.courses = []
        self.groups = []
        self.locals = []
        self.resources = []
        self.tags = []


class GroupEntity:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name
        self.users = []
        self.events = []
        self.notifications = []


class LocalEntity:
    def __init__(self, name, size, id=None):
        self.id = id
        self.name = name
        self.size = size
        self.events = []


class NotificationEntity:
    def __init__(self, text, date, id=None):
        self.id = id
        self.text = text
        self.date = date
        self.users = []
        self.groups = []


class OptionEntity:
    def __init__(self, text, vote=None, id=None):
        self.id = id
        self.text = text
        self.vote = vote
        self.users = []


class PermissionEntity:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name
        self.roles = []


class ResourceEntity:
    def __init__(self, name, kind, id=None):
        self.id = id
        self.name = name
        self.kind = kind
        self.events = []


class RoleEntity:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name
        self.users = []
        self.permissions = []


class StudentEntity:
    def __init__(self, career, user=None, id=None):
        self.id = id
        self.career = career
        self.user = user


class TagEntity:
    def __init__(self, text, id=None):
        self.id = id
        self.text = text
        self.events = []


class TeacherEntity:
    def __init__(self, department, user=None, id=None):
        self.id = id
        self.department = department
        self.user = user


class UserEntity:
    def __init__(self, username, email, password, id=None):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.roles = []
        self.options = []
        self.groups = []
        self.notifications = []

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


class VoteEntity:
    def __init__(self, title, body, id=None):
        self.id = id
        self.title = title
        self.body = body
        self.options = []