<template>
    <div id="group">
        <div class="row">
            <div class="col-12">
                <div class="card mb-2 w-100 border-bottom-primary">
                    <div class="card-header py-3 bg-white">
                        <h5 class="m-0 font-weight-bold text-primary">Usuarios</h5>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <router-link v-for="user in users" :key="user.id" :to="{name: 'userPage', params: {userId: user.id}}" class="list-group-item list-group-item-action">{{ user.username }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Users",
        data() {
            return {
                users : []
            };
        },
        methods: {
            loadGroups() {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state.users.getData(token).then(result => {
                    this.users = this.$store.state.users.data;
                });
            }
        },
        created() {
            this.loadGroups();
        }
    }
</script>
