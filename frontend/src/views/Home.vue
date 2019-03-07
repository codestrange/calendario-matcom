<template>
    <div id="home">
        This is the Home!
    </div>
</template>

<script>
    export default {
        name: "Home",
        created() {
            alert('created home');
        },
        mounted() {
            // if(localStorage.getItem('uh-travel-user_data') !== null) {
            //     this.$store.state.user.reloadMinData(JSON.parse(localStorage.getItem('uh-travel-user_data')));
            // }
            alert('mounted home');
        },
        updated() {
            alert('updated home');
            // localStorage.setItem('uh-travel-user_data', this.$store.state.user.getMinData());
        },
    }
</script>

<style scoped>

</style>