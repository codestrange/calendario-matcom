import Vue from 'vue';
import Vuex from 'vuex';
import UserController from './controllers/user';
import RoutesController from './controllers/routes';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        user: UserController,
        routes: RoutesController
    },
    mutations: {},
    actions: {}
})
