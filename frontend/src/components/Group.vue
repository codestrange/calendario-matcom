<template>
    <div id="group">
        <div class="row">
            <div class="col-12">
                <div class="card mb-4 w-100 border-bottom-primary">
                    <div class="card-header py-3 bg-white">
                        <h5 class="m-0 font-weight-bold text-primary">Grupo: {{ group.name }}</h5>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-6">
                <div class="card mb-1 border-bottom-primary">
                    <div class="card-header bg-white">
                        <h6 class="m-0 font-weight-bold text-primary">Eventos del Grupo</h6>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <button v-if="group.events.length === 0" type="button" class="list-group-item list-group-item-action" disabled>El grupo no tiene ningún evento asignado</button>
                            <router-link v-for="event in group.events" :key="event.id" :to="{name: 'eventPage', params: {eventId: event.id}}" class="list-group-item list-group-item-action">{{ event.title }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-6">
                <div class="card mb-1 border-bottom-primary">
                    <div class="card-header bg-white">
                        <h6 class="m-0 font-weight-bold text-primary">Usuarios del Grupo</h6>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <button v-if="group.users.length === 0" type="button" class="list-group-item list-group-item-action" disabled>El grupo no tiene ningún usuario asignado</button>
                            <router-link v-for="user in group.users" :key="user.id" :to="{name: 'userPage', params: {userId: user.id}}" class="list-group-item list-group-item-action">{{ user.username }}</router-link>
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
                group : {
                    id: -1,
                    name: '',
                    events: [],
                    users: []
                }
            };
        },
        methods: {
            loadData() {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state.group.getData(token, this.group.id).then(result => {
                    this.group = this.$store.state.group.data;
                });
            }
        },
        created() {
            this.group.id = parseInt(this.$route.params.groupId);
            if(isNaN(this.group.id)) {
                this.$router.push({name:'notFoundPage'});
            }
            this.loadData();
        }
    }
</script>
