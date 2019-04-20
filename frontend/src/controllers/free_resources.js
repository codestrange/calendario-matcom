import Petitions from './petitions';
import Endpoints from '../endpoints/endpoints';

const data_key = 'calendario-matcom-free-resources';

export default {
    data: [],
    saveMinData() {
        localStorage.setItem(data_key, JSON.stringify(this.data));
    },
    loadMinData() {
        let stored = localStorage.getItem(data_key);
        if (stored !== null) {
            this.data = JSON.parse(stored);
        }
    },
    removeMinData() {
        localStorage.removeItem(data_key);
    },
    getData(token, start, end) {
        Petitions.clearHeaders();
        Petitions.set_JSONHeaders(token, '');
        let body = {
            start: start,
            end: end
        };
        return Petitions.post(Endpoints.free_resources, body).
        then(response => response.json(), response => console.log('Error getting the response!', response)).
        then(json => {
            if (json !== null && !json.hasOwnProperty('error')) {
                this.data = json;
                this.saveMinData();
                return true;
            }
            return false;
        });
    }
}
