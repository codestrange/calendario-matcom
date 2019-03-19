<template>
    <div id="group">
        <p>
            Esto muestra la informacion del grupo {{id}}.
        </p>
    </div>
</template>

<script>
    export default {
        name: "GroupInfo",
        data() {
            return {
                id: -1
            };
        },
        created() {
            this.id = parseInt(this.$route.params.groupId);
            if(isNaN(this.id)) {
                this.$router.push({name:'notFoundPage'});
            }
            // Now should check if can retrive the group info
        }
    }
</script>
