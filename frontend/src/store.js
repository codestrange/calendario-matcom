import Vue from 'vue';
import Vuex from 'vuex';
import CourseController from './controllers/course';
import CoursesController from './controllers/courses';
import EventController from './controllers/event';
import EventsController from './controllers/events';
import GroupController from './controllers/group';
import GroupsController from './controllers/groups';
import LocalController from './controllers/local';
import LocalsController from './controllers/locals';
import ProfileController from './controllers/profile';
import QueryController from './controllers/query';
import ResourceController from './controllers/resource';
import ResourcesController from './controllers/resources';
import RoutesController from './controllers/routes';
import TagController from './controllers/tag';
import TagsController from './controllers/tags';
import UserController from './controllers/user';
import UsersController from './controllers/users';
import IntervalsController from './controllers/intervals';

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        course: CourseController,
        courses: CoursesController,
        event: EventController,
        events: EventsController,
        group: GroupController,
        groups: GroupsController,
        local: LocalController,
        locals: LocalsController,
        profile: ProfileController,
        query: QueryController,
        resource: ResourceController,
        resources: ResourcesController,
        routes: RoutesController,
        tag: TagController,
        tags: TagsController,
        user: UserController,
        users: UsersController,
        intervals: IntervalsController
    },
    mutations: {},
    actions: {}
});

export default store;
