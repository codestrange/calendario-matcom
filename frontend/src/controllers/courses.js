import Petitions from './petitions';
import Endpoints from '../endpoints/endpoints';

const data_key = 'calendario-matcom-courses';

export default {
    data: {
        courses: []
    },
    saveMinData() {
        localStorage.setItem(data_key, JSON.stringify(this.data.courses));
    },
    loadMinData() {
        let stored = localStorage.getItem(data_key);
        if (stored !== null) {
            this.data.courses = JSON.parse(stored);
        }
    },
    removeMinData() {
        localStorage.removeItem(data_key);
    },
    getCourcesData(token) {
        Petitions.clearHeaders();
        Petitions.set_JSONHeaders(token, '');
        return Petitions.get(Endpoints.courses_data).then(response => response.json(), response => console.log('Error getting the response.')).then(
        json => {
            if (json !== null && !json.hasOwnProperty('error')) {
                this.data.courses = json;
                this.saveMinData();
                return true;
            }
            return false;
        });
    }
}
