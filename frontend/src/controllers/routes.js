export default {
    lasturl: '',
    getLast() {
        return String(this.lasturl);
    },
    updateLast(last) {
        this.lasturl = String(last);
    }
}