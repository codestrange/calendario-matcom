import Petitions from './petitions';
import Endpoints from '../endpoints/endpoints';

const data_key = 'calendario-matcom-query'

export default {
    query_data: {},
    saveMinData() {
        localStorage.setItem(data_key, JSON.stringify(this.query_data));
    },
    loadMinData() {
        let stored = localStorage.getItem(data_key);
        if (stored !== null) {
            this.query_data = JSON.parse(stored);
        }
    },
    removeMinData() {
        localStorage.removeItem(data_key);
    },
    makeQuery(token, courses, groups, locals, tags, resources, users, start, end) {
        Petitions.clearHeaders();
        Petitions.set_JSONHeaders(token, '');
        let body = {
            courses: courses,
            locals: locals,
            tags: tags,
            resources: resources,
            groups: groups,
            users: users
        };
        if (start !== null) {
            body.start = new Date(start);
        }
        if (end !== null) {
            body.end = new Date(end);
        }
        return Petitions.post( Endpoints.query_events, body).then(response => response.json(), response => console.log('Error getting the response!', response)).then(json => {
            if (json !== null && !json.hasOwnProperty('error')) {
                this.query_data = json;
                this.saveMinData();
                return true;
            }
            return false;
        });
    }
}
