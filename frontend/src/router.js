import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home';
import Login from './views/Login';
import Store from './store';

Vue.use(Router);

const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        //Redirections
        {
            path: '/',
            redirect: {name: 'homePage'},
        },
        //Redirections
        {
            path: '/home',
            name: 'homePage',
            component: Home,
            meta: {
                requiresAuth: true
            }
        },
        {
            path: '/login',
            name: 'loginPage',
            component: Login,
        }
        //Hollow Page
        // {
        //     path: '*',
        //     component:
        // }
    ],
    beforeEach(to, from, next) {
        if (to.hasOwnProperty('requiresAuth')) {
            if (to.meta.requiresAuth === true) {
                Store.state.user.loadMinData();
                if (Store.state.user.isLogued() === false) {
                    next({name: 'loginPage'});
                }
            }
            next();
        }
    }
});

export default router;
