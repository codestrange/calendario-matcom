import {encode} from "../utils/base64";

export default {
    headers: {},
    get(url) {
        return fetch(url,{
            method:'get',
            headers: this.headers
        });
    },
    post(url, headers, body) {
        console.log('Not implemented exception!!!');
    },
    put(url, headers, body) {
        console.log('Not implemented exception!!!');
    },
    delete(url, headers) {
        console.log('Not implemented exception!!!');
    },
    set_JSONHeaders(username, password) {
        let headers =
        [
            {
                key: 'Content-Type',
                value: 'application/json'
            },
            {
                key: 'Accept',
                value: 'application/json'
            }
        ];
        if (username !== null && password !== null) {
            headers.push({
                key: 'Authorization',
                value: 'Basic ' + encode(username + ':' + password)
            });
        }
        this.setHeaders(headers);
    },
    setHeaders(headers) {
        headers.forEach(header => {
            this.headers[header.key] = header.value;
        });
    },
    clearHeaders() {
        this.headers = {};
    }
}