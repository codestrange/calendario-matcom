import Petitions from './petitions';
import Endpoints from '../endpoints/endpoints';

const data_key = 'calendario-matcom-groups';

export default {
    data: {
        groups: []
    },
    saveMinData() {
        localStorage.setItem(data_key, JSON.stringify(this.data.groups));
    },
    loadMinData() {
        let stored = localStorage.getItem(data_key);
        if (stored !== null) {
            this.data.groups = JSON.parse(stored);
        }
    },
    removeMinData() {
        localStorage.removeItem(data_key);
    },
    getGroupsData(token) {
        Petitions.clearHeaders();
        Petitions.set_JSONHeaders(token, '');
        return Petitions.get(Endpoints.groups_data).then(response => response.json(), response => console.log('Error getting the response.')).then(
            json => {
                if (json !== null && !json.hasOwnProperty('error')) {
                    this.data.groups = json;
                    this.saveMinData();
                    return true;
                }
                return false;
            });
    }
}
