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
            };
        },
        methods: {
            beforeUnload() {
                this.$store.state.user.loadMinData();
                if (this.$store.state.user.isLogued() === true && this.$store.state.user.user_data.remember === true) {
                    this.$store.state.user.saveMinData();
                }
                else {
                    this.$store.state.user.removeMinData();
                }
            }
        },
        created() {
            document.addEventListener('beforeunload', this.beforeUnload);
        }
    }
</script>

<style>
</style>
