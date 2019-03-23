from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from .admin import admin, ModelView, UserModelView
from .config import config
from .database import db, Course, Event, Group, Interval, Local, Notification, Option, Permission, \
    Resource, Role, Student, Tag, Teacher, User, Vote, UserGroupNotification

migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    admin.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    admin.add_view(ModelView(Course, db.session))
    admin.add_view(ModelView(Event, db.session))
    admin.add_view(ModelView(Group, db.session))
    admin.add_view(ModelView(Interval, db.session))
    admin.add_view(ModelView(Local, db.session))
    admin.add_view(ModelView(Notification, db.session))
    admin.add_view(ModelView(Option, db.session))
    admin.add_view(ModelView(Permission, db.session))
    admin.add_view(ModelView(Resource, db.session))
    admin.add_view(ModelView(Role, db.session))
    admin.add_view(ModelView(Student, db.session))
    admin.add_view(ModelView(Tag, db.session))
    admin.add_view(ModelView(Teacher, db.session))
    admin.add_view(UserModelView(User, db.session))
    admin.add_view(ModelView(Vote, db.session))
    admin.add_view(ModelView(UserGroupNotification, db.session))

    from .controllers import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
