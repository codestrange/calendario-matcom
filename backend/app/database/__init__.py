from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker, mapper, relation
from .entities import CourseEntity, EventEntity, GroupEntity, LocalEntity, NotificationEntity, \
    OptionEntity, PermissionEntity, ResourceEntity, RoleEntity, StudentEntity, TagEntity, \
    TeacherEntity, UserEntity, VoteEntity
from .tables import get_course_table, get_event_table, get_group_table, get_local_table, \
    get_notification_table, get_option_table, get_permission_table, get_resource_table, \
    get_role_table, get_student_table, get_tag_table, get_teacher_table, get_user_table, \
    get_vote_table, get_event_course_table, get_event_group_table, get_event_local_table, \
    get_event_resource_table, get_event_tag_table, get_role_permission_table, \
    get_user_group_table, get_user_group_notification_table, get_user_option_table, \
    get_user_role_table, get_teacher_course_table


class Database:
    def __init__(self, metadata=None, session=None):
        self.session = session
        self.metadata = metadata

    def init_app(self, app):
        if self.metadata is None:
            self.metadata = MetaData(app.config['DATABASE_URL'])

        # Tablas de Entidades
        course_table = get_course_table(self.metadata)
        event_table = get_event_table(self.metadata)
        group_table = get_group_table(self.metadata)
        local_table = get_local_table(self.metadata)
        notification_table = get_notification_table(self.metadata)
        option_table = get_option_table(self.metadata)
        permission_table = get_permission_table(self.metadata)
        resource_table = get_resource_table(self.metadata)
        role_table = get_role_table(self.metadata)
        student_table = get_student_table(self.metadata)
        tag_table = get_tag_table(self.metadata)
        teacher_table = get_teacher_table(self.metadata)
        user_table = get_user_table(self.metadata)
        vote_table = get_vote_table(self.metadata)

        # Tablas de Relaciones
        event_course_table = get_event_course_table(self.metadata)
        event_group_table = get_event_group_table(self.metadata)
        event_local_table = get_event_local_table(self.metadata)
        event_resource_table = get_event_resource_table(self.metadata)
        event_tag_table = get_event_tag_table(self.metadata)
        role_permission_table = get_role_permission_table(self.metadata)
        user_group_table = get_user_group_table(self.metadata)
        user_group_notification_table = get_user_group_notification_table(self.metadata)
        user_option_table = get_user_option_table(self.metadata)
        user_role_table = get_user_role_table(self.metadata)
        teacher_course_table = get_teacher_course_table(self.metadata)

        mapper(CourseEntity, course_table, properties=dict(
            events=relation(EventEntity, secondary=event_course_table),
            teachers=relation(TeacherEntity, secondary=teacher_course_table)
        ))

        mapper(EventEntity, event_table, properties=dict(
            courses=relation(CourseEntity, secondary=event_course_table),
            groups=relation(GroupEntity, secondary=event_group_table),
            locals=relation(LocalEntity, secondary=event_local_table),
            resources=relation(ResourceEntity, secondary=event_resource_table),
            tags=relation(TagEntity, secondary=event_tag_table)
        ))

        mapper(GroupEntity, group_table, properties=dict(
            users=relation(UserEntity, secondary=user_group_table),
            events=relation(EventEntity, secondary=event_group_table),
            notifications=relation(NotificationEntity, secondary=user_group_notification_table)
        ))

        mapper(LocalEntity, local_table, properties=dict(
            events=relation(EventEntity, secondary=event_local_table)
        ))

        mapper(NotificationEntity, notification_table, properties=dict(
            users=relation(UserEntity, secondary=user_group_notification_table),
            groups=relation(GroupEntity, secondary=user_group_notification_table)
        ))

        mapper(OptionEntity, option_table, properties=dict(
            users=relation(UserEntity, secondary=user_option_table)
        ))

        mapper(PermissionEntity, permission_table, properties=dict(
            roles=relation(RoleEntity, secondary=role_permission_table)
        ))

        mapper(ResourceEntity, resource_table, properties=dict(
            events=relation(EventEntity, secondary=event_resource_table)
        ))

        mapper(RoleEntity, role_table, properties=dict(
            users=relation(UserEntity, secondary=user_role_table),
            permissions=relation(PermissionEntity, secondary=role_permission_table)
        ))

        mapper(StudentEntity, student_table, properties=dict(
            user=relation(UserEntity, uselist=False)
        ))

        mapper(TagEntity, tag_table, properties=dict(
            events=relation(EventEntity, secondary=event_tag_table)
        ))

        mapper(TeacherEntity, teacher_table, properties=dict(
            user=relation(UserEntity, uselist=False),
            courses=relation(CourseEntity, secondary=teacher_course_table)
        ))

        mapper(UserEntity, user_table, properties=dict(
            roles=relation(RoleEntity, secondary=user_role_table),
            options=relation(OptionEntity, secondary=user_option_table),
            groups=relation(GroupEntity, secondary=user_group_table),
            notifications=relation(NotificationEntity, secondary=user_group_notification_table)
        ))

        mapper(VoteEntity, vote_table, properties=dict(
            options=relation(OptionEntity, backref='vote')
        ))

        self.metadata.create_all()

        if self.session is None:
            Session = sessionmaker()
            self.session = Session()

        app.db = self
