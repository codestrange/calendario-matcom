import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home';
import Login from './views/Login';
import Store from './store';

Vue.use(Router);

const checkforAuth = (to, from, next) => {
    if (to.matched.some(route => route.meta.requiresAuth)) {
        Store.state.user.loadMinData();
        if (Store.state.user.isLogued() === false) {
            next({name: 'loginPage'});
        }
    }
};

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
            beforeEnter(to, from, next) {
                Store.state.user.loadMinData();
                if (Store.state.user.isLogued() === true) {
                    next({ name: Store.state.routes.getLast() });
                }
                next();
            }
        }
        //Hollow Page
        // {
        //     path: '*',
        //     component:
        // }
    ]
});

router.beforeEach((to, from, next) => {
    checkforAuth(to, from, next);
    next();
});

router.afterEach((to, from) => {
   Store.state.routes.updateLast(from.name);
});

export default router;
