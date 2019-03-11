import Resources from './resource';
import Endpoints from '../endpoints/endpoints';
import {encode, decode} from '../utils/base64';

const data_key = 'calendario-matcom-user';

export default {
    user_data: {
        id:-1,
        username:'',
        fullname:'',
        email:'',
        year:'',
        token:'',
        remember:''
    },
    saveMinData() {
        localStorage.setItem(data_key, JSON.stringify({
            id: Number(this.user_data.id),
            token: String(this.user_data.token),
            remember: String(this.user_data.remember)
        }));
    },
    loadMinData() {
        if(localStorage.getItem(data_key) !== null) {
            let data = JSON.parse(localStorage.getItem(data_key));
            this.updateId(data.id);
            this.updateToken(data.token);
            this.updateToken(data.remember);
        }

    },
    removeMinData() {
        localStorage.removeItem(data_key);
    },
    isLogued() {
        return this.user_data.token !== '';
    },
    logOut() {
        this.user_data.id = -1;
        this.user_data.username = '';
        this.user_data.fullname = '';
        this.user_data.email = '';
        this.user_data.year = '';
        this.user_data.token = '';
        this.removeMinData();
    },
    updateToken(token) {
        this.user_data.token = String(token);
    },
    updateId(id) {
        this.user_data.id = Number(id);
    },
    updateRemember(remember) {
        this.user_data.remember = Boolean(remember);
    },
    getAuthJson(username, password) {
        Resources.clearHeaders();
        Resources.set_JSONHeaders(username, password);
        return Resources.get(Endpoints.token_endpoint).then(response => response.json(), response => console.log('Error getting the response.'));
    },
    authenticateUser(username, password, remember) {
        return this.getAuthJson(username, password)
            .then(json => {
                if (json.token !== null && json.id !== null) {
                    this.updateToken(json.token);
                    this.updateId(json.id);
                    this.updateRemember(remember);
                    this.saveMinData();
                    return true;
                }
                console.log(json.error + ':' + json.message);
                return false;
            });
    },
    getUserData() {
        Resources.clearHeaders();
        Resources.set_JSONHeaders(this.user_data.token, '');
        this.loadMinData();
        return Resources.get(Endpoints.users_data + this.user_data.id.toString() + '/').then(
            response => response.json(), response => console.log('Error getting the response.'))
            .then(json => {
                if(json.email !== null && json.username !== null) {
                    this.user_data.email = json.email;
                    this.user_data.username = json.username;
                    return {
                      username: json.username,
                      email: json.email,
                      fullname: 'No in DB',
                    };
                }
            });
    },
    getUsersData() {
        Resources.clearHeaders();
        Resources.set_JSONHeaders(this.user_data.token, '');
        return Resources.get(Endpoints.users_data).then(response => response.json(), response => console.log('Error getting the response.'))
            .then( json => {
                if (json !== null) {
                    return json;
                }
                console.log('Error getting JSON.');
            });
    }
}