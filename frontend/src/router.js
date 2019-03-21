import Vue from 'vue';
import Router from 'vue-router';
import Nav from './views/Nav';
import Login from './views/Login';
import Store from './store';
import Register from './views/Register';
import NotFound from './views/NotFound';
import Home from './components/Home';
import Profile from './components/Profile';
import Course from './components/Course';
import Courses from './components/Courses';
import Group from './components/Group';
import Groups from './components/Groups';
import User from './components/User';
import Users from './components/Users';
import Event from './components/Event';

Vue.use(Router);

const checkforAuth = (to, from, next) => {
    if (to.matched.some(route => route.meta.requiresAuth)) {
        Store.state.profile.loadMinData();
        if (Store.state.profile.isLogued() === false) {
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
            path: '/nav',
            name: 'navPage',
            component: Nav,
            meta: {
                requiresAuth: true
            },
            children: [
                {
                    path: '/home',
                    name: 'homePage',
                    component: Home,
                    meta: {
                        requiresAuth: true
                    }
                },
                {
                    path: '/profile',
                    name: 'profilePage',
                    component: Profile,
                    meta: {
                        requiresAuth: true
                    }
                },
                {
                    path: '/courses/:courseId',
                    name: 'coursePage',
                    component: Course,
                    meta: {
                        requiresAuth: true
                    }
                },
                {
                    path: '/courses',
                    name: 'coursesPage',
                    component: Courses,
                    meta: {
                        requiresAuth: true
                    }
                },
                {
                    path: '/groups/:groupId',
                    name: 'groupPage',
                    component: Group,
                    meta: {
                        requiresAuth: true
                    }
                },
                {
                    path: '/groups',
                    name: 'groupsPage',
                    component: Groups,
                    meta: {
                        requiresAuth: true
                    }
                },
                {
                    path: '/users/:userId',
                    name: 'userPage',
                    component: User,
                    meta: {
                        requiresAuth: true
                    }
                },
                {
                    path: '/users',
                    name: 'usersPage',
                    component: Users,
                    meta: {
                        requiresAuth: true
                    }
                },
                {
                    path: '/events/:eventId',
                    name: 'eventPage',
                    component: Event,
                    meta: {
                        requiresAuth: true
                    }
                },
                // {
                //     path: '/events',
                //     name: 'eventsPage',
                //     component: Users,
                //     meta: {
                //         requiresAuth: true
                //     }
                // }
            ]
        },
        {
            path: '/login',
            name: 'loginPage',
            component: Login,
            beforeEnter(to, from, next) {
                Store.state.profile.loadMinData();
                if (Store.state.profile.isLogued() === true) {
                    next({ name: Store.state.routes.getLast() });
                }
                next();
            }
        },
        {
            path: '/register',
            name: 'registerPage',
            component: Register
        },
        {
            path: '*',
            name: 'notFoundPage',
            component: NotFound
        }
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
