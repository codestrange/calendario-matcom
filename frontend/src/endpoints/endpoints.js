const baseUrl = 'http://localhost:5000/api/';

export default {
    baseUrl: baseUrl,
    courses: baseUrl + 'courses',
    groups: baseUrl + 'groups',
    events: baseUrl + 'events',
    query: baseUrl + 'events/query',
    locals: baseUrl + 'locals',
    permissions: baseUrl + 'permissions',
    profile: baseUrl + 'profile',
    register: baseUrl + 'register',
    roles: baseUrl + 'roles',
    resources: baseUrl + 'resources',
    tags: baseUrl + 'tags',
    token: baseUrl + 'token',
    users: baseUrl + 'users',
    intervals: baseUrl + 'intervals',
    free_locals: baseUrl + 'locals/free',
    free_resources: baseUrl + 'resources/free',
}