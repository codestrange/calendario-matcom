import Petitions from './petitions';
import Endpoints from '../endpoints/endpoints';

const data_key = 'calendario-matcom-tags';

export default {
    data: {
        tags: []
    },
    saveMinData() {
        localStorage.setItem(data_key, JSON.stringify(this.data.tags));
    },
    loadMinData() {
        let stored = localStorage.getItem(data_key);
        if (stored !== null) {
            this.data.tags = JSON.parse(stored);
        }
    },
    removeMinData() {
        localStorage.removeItem(data_key);
    },
    getTagsData(token) {
        Petitions.clearHeaders();
        Petitions.set_JSONHeaders(token, '');
        return Petitions.get(Endpoints.tags_data).then(response => response.json(), response => console.log('Error getting the response.')).then(
            json => {
                if (json !== null && !json.hasOwnProperty('error')) {
                    this.data.tags = json;
                    this.saveMinData();
                    return true;
                }
                return false;
            });
    }
}
