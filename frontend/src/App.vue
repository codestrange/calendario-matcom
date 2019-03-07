<template>
    <div id="app">

        <body class="bg-gradient-primary">

            <router-view></router-view>

        </body>

    </div>
</template>

<script>
    export default {
        name: 'app',
        data() {
            return {
                prop: 'some props'
            };
        },
        mounted() {
            if(localStorage.getItem('uh-travel-user_data') !== null) {
                this.$store.state.user.reloadMinData(JSON.parse(localStorage.getItem('uh-travel-user_data')));
            }
        },
        updated() {
            localStorage.setItem('uh-travel-user_data', this.$store.state.user.getMinData());
        },
        beforeDestroy() {
            console.log(this.prop);
        }
    }
</script>

<style>
</style>
