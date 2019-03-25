import {encode} from "../utils/base64";

export default {
    headers: {},
    get(url) {
        return fetch(url,{
            method: 'get',
            headers: this.headers
        });
    },
    post(url, body) {
        if(body === null) {
            return fetch(url,{
                method: 'post',
                headers: this.headers
            });
        }
        return fetch(url,{
            method: 'post',
            headers: this.headers,
            body: JSON.stringify(body)
        });
    },
    put(url, body) {
        if(body === null) {
            return fetch(url,{
                method: 'put',
                headers: this.headers
            });
        }
        return fetch(url,{
            method: 'put',
            headers: this.headers,
            body: JSON.stringify(body)
        });
    },
    delete(url, body) {
        if(body === null) {
            return fetch(url,{
                method: 'delete',
                headers: this.headers
            });
        }
        return fetch(url,{
            method: 'delete',
            headers: this.headers,
            body: body
        });
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