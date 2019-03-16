import Petitions from './petitions';
import Endpoints from '../endpoints/endpoints';

const data_key = 'calendario-matcom-resources';

export default {
    data: {
        resources: []
    },
    saveMinData() {
        localStorage.setItem(data_key, JSON.stringify(this.data.resources));
    },
    loadMinData() {
        let stored = localStorage.getItem(data_key);
        if (stored !== null) {
            this.data.resources = JSON.parse(stored);
        }
    },
    removeMinData() {
        localStorage.removeItem(data_key);
    },
    getCourcesData(token) {
        Resources.clearHeaders();
        Resources.set_JSONHeaders(token, '');
        return Petitions.get(Endpoints.resources_data).then(response => response.json(), response => console.log('Error getting the response.')).then(
            json => {
                if (json !== null && !json.hasOwnProperty('error')) {
                    this.data.resources = json;
                    this.saveMinData();
                    return true;
                }
                return false;
            });
    }
}
