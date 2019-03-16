import Petitions from './petitions';
import Endpoints from '../endpoints/endpoints';

const data_key = 'calendario-matcom-locals';

export default {
    data: {
        locals: []
    },
    saveMinData() {
        localStorage.setItem(data_key, JSON.stringify(this.data.locals));
    },
    loadMinData() {
        let stored = localStorage.getItem(data_key);
        if (stored !== null) {
            this.data.locals = JSON.parse(stored);
        }
    },
    removeMinData() {
        localStorage.removeItem(data_key);
    },
    getLocalsData(token) {
        Resources.clearHeaders();
        Resources.set_JSONHeaders(token, '');
        return Petitions.get(Endpoints.locals_data).then(response => response.json(), response => console.log('Error getting the response.')).then(
            json => {
                if (json !== null && !json.hasOwnProperty('error')) {
                    this.data.locals = json;
                    this.saveMinData();
                    return true;
                }
                return false;
            });
    }
}
