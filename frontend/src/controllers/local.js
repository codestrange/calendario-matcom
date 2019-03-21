import Petitions from './petitions';
import Endpoints from '../endpoints/endpoints';

const data_key = 'calendario-matcom-local';

export default {
    data: {},
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
    getData(token, id) {
        Petitions.clearHeaders();
        Petitions.set_JSONHeaders(token, '');
        return Petitions.get(Endpoints.locals + '/' + id).
            then(response => response.json(), response => console.log('Error getting the response.')).
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
