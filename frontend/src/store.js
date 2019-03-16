import Vue from 'vue';
import Vuex from 'vuex';
import UserController from './controllers/user';
import RoutesController from './controllers/routes';
import ResourcesController from './controllers/resources';
import TagsController from './controllers/tags';
import LocalsController from './controllers/locals';
import GroupsController from './controllers/groups';
import CoursesController from './controllers/courses';
import QueryController from './controllers/query';

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        user: UserController,
        routes: RoutesController,
        resources: ResourcesController,
        tags: TagsController,
        locals: LocalsController,
        groups: GroupsController,
        courses: CoursesController,
        query: QueryController
    },
    mutations: {},
    actions: {}
});

export default store;
