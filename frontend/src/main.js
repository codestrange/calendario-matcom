import Vue from 'vue';
import App from './App.vue';
import store from './store';
import router from './router';
import '../public/vendor/jquery/jquery.min';
import '../public/vendor/bootstrap/js/bootstrap.bundle.min';
import '../public/vendor/jquery-easing/jquery.easing.min';
import '../public/js/sb-admin-2.min';
import '../public/vendor/fontawesome-free/css/all.min.css';
import '../public/css/sb-admin-2.min.css';

Vue.config.productionTip = false;

new Vue({
    store,
    router,
    render: h => h(App),
}).$mount('#app');
