from os import getenv
from app import create_app
from app.database.entities import CourseEntity, EventEntity, GroupEntity, LocalEntity, \
    NotificationEntity, OptionEntity, PermissionEntity, ResourceEntity, RoleEntity, \
    StudentEntity, TagEntity, TeacherEntity, UserEntity, VoteEntity
from app.database.repositories.all import CourseRepository, EventRepository, GroupRepository, \
    LocalRepository, NotificationRepository, OptionRepository, PermissionRepository, \
    ResourceRepository, RoleRepository, StudentRepository, TagRepository, TeacherRepository, \
    UserRepository, VoteRepository

app = create_app(getenv('FLASK_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=app.db, unitofwork=app.unitofwork,
                CourseEntity=CourseEntity, EventEntity=EventEntity, GroupEntity=GroupEntity,
                LocalEntity=LocalEntity, NotificationEntity=NotificationEntity,
                OptionEntity=OptionEntity, PermissionEntity=PermissionEntity,
                ResourceEntity=ResourceEntity, RoleEntity=RoleEntity, StudentEntity=StudentEntity,
                TagEntity=TagEntity, TeacherEntity=TeacherEntity, UserEntity=UserEntity,
                VoteEntity=VoteEntity, CourseRepository=CourseRepository,
                EventRepository=EventRepository, GroupRepository=GroupRepository,
                LocalRepository=LocalRepository, NotificationRepository=NotificationRepository,
                OptionRepository=OptionRepository, PermissionRepository=PermissionRepository,
                ResourceRepository=ResourceRepository, RoleRepository=RoleRepository,
                StudentRepository=StudentRepository, TagRepository=TagRepository,
                TeacherRepository=TeacherRepository, UserRepository=UserRepository,
                VoteRepository=VoteRepository)
