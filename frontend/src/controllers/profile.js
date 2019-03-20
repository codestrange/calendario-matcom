import Petitions from './petitions';
import Endpoints from '../endpoints/endpoints';

const data_key = 'calendario-matcom-profile';

export default {
    data: {
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
            token: String(this.data.token),
            remember: String(this.data.remember)
        }));
    },
    loadMinData() {
        if(localStorage.getItem(data_key) !== null) {
            let temp_data = JSON.parse(localStorage.getItem(data_key));
            this.data.token = String(temp_data.token);
            this.data.remember = Boolean(temp_data.remember);
        }
    },
    removeMinData() {
        localStorage.removeItem(data_key);
    },
    isLogued() {
        return this.data.token !== '';
    },
    logOut() {
        this.data.id = -1;
        this.data.username = '';
        this.data.fullname = '';
        this.data.email = '';
        this.data.year = '';
        this.data.token = '';
        this.removeMinData();
    },
    getAuthJson(username, password) {
        Petitions.clearHeaders();
        Petitions.set_JSONHeaders(username, password);
        return Petitions.get(Endpoints.token).then(response => response.json(), response => console.log('Error getting the response.'));
    },
    authenticate(username, password, remember) {
        return this.getAuthJson(username, password)
            .then(json => {
                if (json.hasOwnProperty('token')) {
                    this.data.token = String(json.token);
                    this.data.remember = Boolean(json.remember);
                    this.saveMinData();
                    return true;
                }
                console.log(json.error + ':' + json.message);
                return false;
            });
    },
    getData() {
        this.loadMinData();
        Petitions.clearHeaders();
        Petitions.set_JSONHeaders(this.data.token, '');
        return Petitions.get(Endpoints.profile).then(
            response => response.json(), response => console.log('Error getting the response.'))
            .then(json => {
                if(json.hasOwnProperty('email') && json.hasOwnProperty('username') && json.hasOwnProperty('id')) {
                    this.data.email = json.email;
                    this.data.username = json.username;
                    this.data.id = json.id;
                }
            });
    },
    register(username, email, password) {
        Petitions.clearHeaders();
        Petitions.set_JSONHeaders();
        return Petitions.post(Endpoints.register, {
            username: username,
            email: email,
            password: password
        }).then(response => response.json(), response => console.log('Error getting the response.'));
    }
}