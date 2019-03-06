from .sqlalchemy_repository import SQLAlchemyRepository
from ..entities import CourseEntity, EventEntity, GroupEntity, LocalEntity, NotificationEntity, \
    OptionEntity, PermissionEntity, ResourceEntity, RoleEntity, StudentEntity, TagEntity, \
    TeacherEntity, UserEntity, VoteEntity


class CourseRepository(SQLAlchemyRepository):
    def entity(self):
        return CourseEntity


class EventRepository(SQLAlchemyRepository):
    def entity(self):
        return EventEntity


class GroupRepository(SQLAlchemyRepository):
    def entity(self):
        return GroupEntity


class LocalRepository(SQLAlchemyRepository):
    def entity(self):
        return LocalEntity


class NotificationRepository(SQLAlchemyRepository):
    def entity(self):
        return NotificationEntity


class OptionRepository(SQLAlchemyRepository):
    def entity(self):
        return OptionEntity


class PermissionRepository(SQLAlchemyRepository):
    def entity(self):
        return PermissionEntity


class ResourceRepository(SQLAlchemyRepository):
    def entity(self):
        return ResourceEntity


class RoleRepository(SQLAlchemyRepository):
    def entity(self):
        return RoleEntity


class StudentRepository(SQLAlchemyRepository):
    def entity(self):
        return StudentEntity


class TagRepository(SQLAlchemyRepository):
    def entity(self):
        return TagEntity


class TeacherRepository(SQLAlchemyRepository):
    def entity(self):
        return TeacherEntity


class UserRepository(SQLAlchemyRepository):

    def entity(self):
        return UserEntity


class VoteRepository(SQLAlchemyRepository):
    def entity(self):
        return VoteEntity
