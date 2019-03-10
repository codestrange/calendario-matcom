<template>
    <html>
        <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <meta name="description" content="Calendario-Matcom">
            <meta name="author" content="CodeStrange">
            <title>Calendario Matcom</title>
        </head>
        <body class="bg-gradient-primary">
            <router-view></router-view>
        </body>
    </html>
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
