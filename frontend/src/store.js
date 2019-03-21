import Vue from 'vue';
import Vuex from 'vuex';
import UserController from './controllers/user';
import UsersController from './controllers/users';
import ProfileController from './controllers/profile';
import RoutesController from './controllers/routes';
import ResourcesController from './controllers/resources';
import TagsController from './controllers/tags';
import LocalsController from './controllers/locals';
import GroupController from './controllers/group';
import GroupsController from './controllers/groups';
import CourseController from './controllers/course';
import CoursesController from './controllers/courses';
import QueryController from './controllers/query';
import EventController from './controllers/event';

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        profile: ProfileController,
        user: UserController,
        users: UsersController,
        routes: RoutesController,
        resources: ResourcesController,
        tags: TagsController,
        locals: LocalsController,
        group: GroupController,
        groups: GroupsController,
        course: CourseController,
        courses: CoursesController,
        query: QueryController,
        event: EventController
    },
    mutations: {},
    actions: {}
});

export default store;
