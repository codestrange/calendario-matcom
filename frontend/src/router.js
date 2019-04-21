import Vue from 'vue';
import Router from 'vue-router';
import Course from './components/Course';
import Courses from './components/Courses';
import Event from './components/Event';
import Events from './components/Events';
import Group from './components/Group';
import Groups from './components/Groups';
import Home from './components/Home';
import Local from './components/Local';
import Locals from './components/Locals';
import Login from './views/Login';
import Nav from './views/Nav';
import NotFound from './views/NotFound';
import Profile from './components/Profile';
import Register from './views/Register';
import Resource from './components/Resource';
import Resources from './components/Resources';
import Notifications from './components/Notifications';
import Store from './store';
import Tag from './components/Tag';
import Tags from './components/Tags';
import User from './components/User';
import Users from './components/Users';
import Editor from './components/Editor';
import Panel from './components/Panel';
import Forbidden from './views/Forbidden';
import Permission from './utils/permission';


Vue.use(Router);

const checkforAuth = (to, from, next) => {
    if (to.matched.some(route => route.meta.requiresAuth)) {
        Store.state.profile.loadMinData();
        if (Store.state.profile.isLogued() === false) {
            next({name: 'loginPage'});
        }
    }
};

const checkRoles = (to, from, next) => {
    if (to.matched.some(route => route.meta.requireRoles)) {
        Store.state.profile.loadMinData();
        let haveAccess = true;
        to.meta.requireRoles.forEach((role) => {
            haveAccess = haveAccess & Store.state.profile.hasRole(role);
        });
        if (haveAccess === 0) {
            next({name: 'forbiddenPage'})
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
                    path: '/events/:eventId',
                    name: 'eventPage',
                    component: Event,
                    meta: {
                        requiresAuth: true
                    }
                },
                {
                    path: '/events',
                    name: 'eventsPage',
                    component: Events,
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
                    path: '/locals/:localId',
                    name: 'localPage',
                    component: Local,
                    meta: {
                        requiresAuth: true
                    }
                },
                {
                    path: '/locals',
                    name: 'localsPage',
                    component: Locals,
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
                    path: '/resources/:resourceId',
                    name: 'resourcePage',
                    component: Resource,
                    meta: {
                        requiresAuth: true
                    }
                },
                {
                    path: '/resources',
                    name: 'resourcesPage',
                    component: Resources,
                    meta: {
                        requiresAuth: true
                    }
                },
                {
                    path: '/tags/:tagId',
                    name: 'tagPage',
                    component: Tag,
                    meta: {
                        requiresAuth: true
                    }
                },
                {
                    path: '/tags',
                    name: 'tagsPage',
                    component: Tags,
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
                    path: '/notifications',
                    name: 'notificationsPage',
                    component: Notifications,
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
                    path: '/editor/:groupId',
                    name: 'editorPage',
                    component: Editor,
                    meta: {
                        requiresAuth: true,
                        requireRoles: [
                            Permission.VIEW_PANEL,
                            Permission.CREATE_EVENT
                        ]
                    }
                },
                {
                    path: '/panel',
                    name: 'panelPage',
                    component: Panel,
                    meta: {
                        requiresAuth: true,
                        requireRoles: [
                            Permission.VIEW_PANEL
                        ]
                    }
                }
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
            path: '/forbidden',
            name: 'forbiddenPage',
            component: Forbidden
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
    checkRoles(to, from, next);
    next();
});

router.afterEach((to, from) => {
   Store.state.routes.updateLast(from.name);
});

export default router;
