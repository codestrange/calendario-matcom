import Vue from 'vue';
import App from './App.vue';
import store from './store';
import router from './router';
import './assets/vendor/jquery/jquery.min';
import './assets/vendor/bootstrap/js/bootstrap.bundle.min';
import './assets/vendor/jquery-easing/jquery.easing.min';
import './assets/js/sb-admin-2.min';

Vue.config.productionTip = false;

new Vue({
    store,
    router,
    render: h => h(App),
}).$mount('#app');
