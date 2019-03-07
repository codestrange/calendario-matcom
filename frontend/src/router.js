import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home';
import Login from './views/Login';
import UserController from './controllers/user';
import RoutesController from './controllers/routes';

Vue.use(Router);

export default new Router({
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
            beforeEnter(to, from, next) {
                if (!UserController.isLogued()) {
                    return next({name: 'loginPage'});
                }
                next();
            }
        },
        {
            path: '/login',
            name: 'loginPage',
            component: Login,
            beforeEnter(to, from, next) {
                RoutesController.updateLast(from.name);
            }
        }
        //Hollow Page
        // {
        //     path: '*',
        //     component:
        // }
    ]
})
