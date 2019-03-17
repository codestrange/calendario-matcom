import Petitions from './petitions';
import Endpoints from '../endpoints/endpoints';

export default {
    data: {
        event: {}
    },
    getEventData(token, id) {
        Petitions.clearHeaders();
        Petitions.set_JSONHeaders(token, '');
        return Petitions.get(Endpoints.event_info + id).then(response => response.json(), response => console.log('Error getting the response.'))
            .then(json => {
                if (json !== null && !json.hasOwnProperty('error')) {
                    this.data.event = json;
                    return true;
                }
                return false;
            });
    }
}