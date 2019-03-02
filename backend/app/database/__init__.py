from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker, mapper, relation
from .entities import CourseEntity, EventEntity, GroupEntity, LocalEntity, NotificationEntity, \
    OptionEntity, PermissionEntity, ResourceEntity, RoleEntity, TagEntity, UserEntity, VoteEntity
from .tables import get_course_table, get_event_table, get_group_table, get_local_table, \
    get_notification_table, get_option_table, get_permission_table, get_resource_table, \
    get_role_table, get_tag_table, get_user_table, get_vote_table, get_event_course_table, \
    get_event_group_table, get_event_local_table, get_event_resource_table, get_event_tag_table, \
    get_role_permission_table, get_user_group_table, get_user_group_notification_table, \
    get_user_option_table, get_user_role_table


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
        group_table = get_group_table(self.metadata) 
        course_table = get_course_table(self.metadata)
        event_table = get_event_table(self.metadata)
        tag_table = get_tag_table(self.metadata)
        local_table = get_local_table(self.metadata)
        resource_table = get_resource_table(self.metadata)
        type_table = get_type_table(self.metadata)

        self.metadata.create_all()

        if self.session is None:
            Session = sessionmaker()
            self.session = Session()

        app.db = self
