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
            token: String(this.user_data.token),
            remember: String(this.user_data.remember)
        }));
    },
    loadMinData() {
        if(localStorage.getItem(data_key) !== null) {
            let data = JSON.parse(localStorage.getItem(data_key));
            this.updateToken(data.token);
            this.updateRemember(data.remember);
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
                if (json.hasOwnProperty('token')) {
                    this.updateToken(json.token);
                    this.updateRemember(remember);
                    this.saveMinData();
                    return true;
                }
                console.log(json.error + ':' + json.message);
                return false;
            });
    },
    getUserData() {
        this.loadMinData();
        Resources.clearHeaders();
        Resources.set_JSONHeaders(this.user_data.token, '');
        return Resources.get(Endpoints.profile_data).then(
            response => response.json(), response => console.log('Error getting the response.'))
            .then(json => {
                if(json.hasOwnProperty('email') && json.hasOwnProperty('username') && json.hasOwnProperty('id')) {
                    this.user_data.email = json.email;
                    this.user_data.username = json.username;
                    this.user_data.id = json.id;
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
    },
    createUser(username, email, password) {
        Resources.clearHeaders();
        Resources.set_JSONHeaders();
        return Resources.post(Endpoints.create_user, {
            username: username,
            email: email,
            password: password
        }).then(response => response.json(), response => console.log('Error getting the response.'))
            .then( json => {
                if (json !== null && json.hasOwnProperty('error') === false) {
                    console.log(json.message);
                    return true;
                }
                console.log(json.error + ':' + json.message);
                return false;
            });
    }
}