<template>
    <div id="app">
        <router-view></router-view>
    </div>
</template>

<script>
    export default {
        name: 'app',
        data() {
            return {
            };
        },
        methods: {
            
        },
        mounted() {
            // let jqueryjs = document.createElement('script');
            // jqueryjs.setAttribute('src', './assets/vendor/jquery/jquery.min');
            // document.body.appendChild(jqueryjs);
            // let bootstrapjs = document.createElement('script');
            // bootstrapjs.setAttribute('src', './assets/vendor/bootstrap/js/bootstrap.bundle.min');
            // document.body.appendChild(bootstrapjs);
            // let jqueryeasing = document.createElement('script');
            // jqueryeasing.setAttribute('src', './assets/vendor/jquery-easing/jquery.easing.min');
            // document.body.appendChild(jqueryeasing);
            // let sbadminjs = document.createElement('script');
            // sbadminjs.setAttribute('src', './assets/js/sb-admin-2.min');
            // document.body.appendChild(sbadminjs);
        }
    }
</script>

<style>
    @import "assets/css/sb-admin-2.min.css";
    @import "assets/vendor/fontawesome-free/css/all.min.css";
</style>
