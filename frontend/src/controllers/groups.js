import Petitions from './petitions';
import Endpoints from '../endpoints/endpoints';

const data_groups_key = 'calendario-matcom-groups';
const data_group_key = 'calendario-matcom-group';

export default {
    data: {
        group: {},
        groups: []
    },
    saveMinData() {
        localStorage.setItem(data_group_key, JSON.stringify(this.data.group));
        localStorage.setItem(data_groups_key, JSON.stringify(this.data.groups));
    },
    loadMinData() {
        let stored_group = localStorage.getItem(data_group_key);
        if (stored_group !== null) {
            this.data.group = JSON.parse(stored_group);
        }
        let stored_groups = localStorage.getItem(data_groups_key);
        if (stored_groups !== null) {
            this.data.groups = JSON.parse(stored_groups);
        }
    },
    removeMinData() {
        localStorage.removeItem(data_group_key);
        localStorage.removeItem(data_groups_key);
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
    },
    getGroupData(token, id) {
        Petitions.clearHeaders();
        Petitions.set_JSONHeaders(token, '');
        return Petitions.get(Endpoints.groups_data + '/' + id).then(response => response.json(), response => console.log('Error getting the response.')).then(
            json => {
                if (json !== null && !json.hasOwnProperty('error')) {
                    this.data.group = json;
                    this.saveMinData();
                    return true;
                }
                return false;
            });
    }
}
