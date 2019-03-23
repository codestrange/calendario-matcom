<template>
    <div id="group">
        <div class="row">
            <div class="col-12">
                <div class="card mb-4 w-100 border-bottom-primary">
                    <div class="card-header py-3 bg-white">
                        <h5 class="m-0 font-weight-bold text-primary">Usuario: {{ user.username }}</h5>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-12">
                <div class="card mb-1 border-bottom-primary">
                    <div class="card-header bg-white">
                        <h6 class="m-0 font-weight-bold text-primary">Grupos del usuario</h6>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <button v-if="user.groups.length === 0" type="button" class="list-group-item list-group-item-action" disabled>El usuario no tiene ningún grupo asignado</button>
                            <router-link v-for="group in user.groups" :key="group.id" :to="{name: 'groupPage', params: {groupId: group.id}}" class="list-group-item list-group-item-action">{{ group.name }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Group",
        data() {
            return {
                user : {
                    id: -1,
                    username: '',
                    groups: []
                }
            };
        },
        methods: {
            loadData() {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state.user.getData(token, this.user.id).then(result => {
                    if (result === true) {
                        this.user = this.$store.state.user.data;
                    }
                    else {
                        this.$router.push({name:'notFoundPage'});
                    }
                });
            }
        },
        created() {
            this.user.id = parseInt(this.$route.params.userId);
            if(isNaN(this.user.id)) {
                this.$router.push({name:'notFoundPage'});
            }
            this.loadData();
        }
    }
</script>
