from os import getenv
from app import create_app
from app.database.entities import CourseEntity, EventEntity, GroupEntity, LocalEntity, \
    NotificationEntity, OptionEntity, PermissionEntity, ResourceEntity, RoleEntity, TagEntity, \
    UserEntity, VoteEntity
from app.database.repositories.all import CourseRepository, EventRepository, GroupRepository, \
    LocalRepository, NotificationRepository, OptionRepository, PermissionRepository, \
    ResourceRepository, RoleRepository, TagRepository, UserRepository, VoteRepository

app = create_app(getenv('FLASK_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=app.db, unitofwork=app.unitofwork,
                CourseEntity=CourseEntity, EventEntity=EventEntity, GroupEntity=GroupEntity,
                LocalEntity=LocalEntity, NotificationEntity=NotificationEntity,
                OptionEntity=OptionEntity, PermissionEntity=PermissionEntity,
                ResourceEntity=ResourceEntity, RoleEntity=RoleEntity, TagEntity=TagEntity,
                UserEntity=UserEntity, VoteEntity=VoteEntity, CourseRepository=CourseRepository,
                EventRepository=EventRepository, GroupRepository=GroupRepository,
                LocalRepository=LocalRepository, NotificationRepository=NotificationRepository,
                OptionRepository=OptionRepository, PermissionRepository=PermissionRepository,
                ResourceRepository=ResourceRepository, RoleRepository=RoleRepository,
                TagRepository=TagRepository, UserRepository=UserRepository,
                VoteRepository=VoteRepository)
