from .sqlalchemy_repository import SQLAlchemyRepository
from ...entities.course_entity import CourseEntity


class CourseRepository(SQLAlchemyRepository):
    def entity(self):
        return CourseEntity
