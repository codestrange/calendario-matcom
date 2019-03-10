import Vue from 'vue';
import Vuex from 'vuex';
import UserController from './controllers/user';
import RoutesController from './controllers/routes';

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        user: UserController,
        routes: RoutesController
    },
    mutations: {},
    actions: {}
});

export default store;
