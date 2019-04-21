import Petitions from './petitions';
import Endpoints from '../endpoints/endpoints';

const data_key = 'calendario-matcom-notifications';

export default {
    data: [],
    saveMinData() {
        localStorage.setItem(data_key, JSON.stringify(this.data));
    },
    updates: [],
    update() {
        this.updates.forEach(item => {
            item.method();
        });
    },
    addUpdate(id, method) {
        let mark = false;
        this.updates.forEach(item => {
            if (id === item.id) {
                item.method = method;
                mark = true;
            }
        });
        if (!mark) {
            this.updates.push({
                'id': id,
                'method': method
            });
        }
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
    getData(token) {
        Petitions.clearHeaders();
        Petitions.set_JSONHeaders(token, '');
        return Petitions.get(Endpoints.notifications).
            then(response => response.json(), response => console.log('Error getting the response.')).
            then(json => {
                if (json !== null && !json.hasOwnProperty('error')) {
                    this.data = json;
                    this.saveMinData();
                    return true;
                }
                return false;
            });
    },
    setSeened(token, id) {
        Petitions.clearHeaders();
        Petitions.set_JSONHeaders(token, '');
        return Petitions.post(Endpoints.notifications + '/seen/' + id, null).
            then(response => response.json(), response => console.log('Error getting the response.')).
            then(json => {
                if (json !== null && !json.hasOwnProperty('error')) {
                    return true;
                }
                return false;
            });
    }
}
