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
    setHeaders(headers) {
        headers.forEach(header => {
            this.headers[header.key] = header.value;
        });
    },
    clearHeaders() {
        this.headers = {};
    }
}