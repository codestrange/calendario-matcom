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
                <div class="card mb-1 bg-white border-bottom-primary">
                    <a href="#collapseCardGroupsEvents" class="d-block card-header py-3" data-toggle="collapse" role="button" aria-expanded="false" aria-controls="collapseCardGroupsEvents">
                        <h6 class="m-0 font-weight-bold text-primary">Eventos del Grupo</h6>
                    </a>
                    <div class="collapse hide" id="collapseCardGroupsEvents" style="">
                        <div class="card-body p-2">
                            <div class="row">
                                <div class="col-9">
                                    <input type="text w-100" v-model="group_events" class="form-control bg-light border-0 small" placeholder="Buscar ..." aria-label="Search" aria-describedby="basic-addon2">
                                </div>
                                <div class="col-3">
                                    <button class="btn ml-2">
                                        <i class="fas fa-sort-alpha-down"></i>
                                    </button>
                                    <button class="btn ml-2">
                                        <i class="fas fa-sort-alpha-up"></i>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <button v-if="group.events.length === 0" type="button" class="list-group-item list-group-item-action" disabled>El grupo no tiene ningún evento asignado</button>
                            <button v-else-if="filterList(group.events, group_events, 'title').length === 0" type="button" class="list-group-item list-group-item-action" disabled>No hay resultados para mostrar</button>
                            <router-link v-for="event in filterList(group.events, group_events, 'title')" :key="event.id" :to="{name: 'eventPage', params: {eventId: event.id}}" class="list-group-item list-group-item-action">{{ event.title }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-6">
                <div class="card mb-1 bg-white border-bottom-primary">
                    <a href="#collapseCardGroupsUsers" class="d-block card-header py-3" data-toggle="collapse" role="button" aria-expanded="false" aria-controls="collapseCardGroupsUsers">
                        <h6 class="m-0 font-weight-bold text-primary">Usuarios del Grupo</h6>
                    </a>
                    <div class="collapse hide" id="collapseCardGroupsUsers" style="">
                        <div class="card-body p-2">
                            <div class="row">
                                <div class="col-9">
                                    <input type="text w-100" v-model="group_users" class="form-control bg-light border-0 small" placeholder="Buscar ..." aria-label="Search" aria-describedby="basic-addon2">
                                </div>
                                <div class="col-3">
                                    <button class="btn ml-2">
                                        <i class="fas fa-sort-alpha-down"></i>
                                    </button>
                                    <button class="btn ml-2">
                                        <i class="fas fa-sort-alpha-up"></i>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <button v-if="group.users.length === 0" type="button" class="list-group-item list-group-item-action" disabled>El grupo no tiene ningún usuario asignado</button>
                            <button v-else-if="filterList(group.users, group_users,'username').length === 0" type="button" class="list-group-item list-group-item-action" disabled>No hay resultados para mostrar</button>
                            <router-link v-for="user in filterList(group.users, group_users,'username')" :key="user.id" :to="{name: 'userPage', params: {userId: user.id}}" class="list-group-item list-group-item-action">{{ user.username }}</router-link>
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
                },
                group_users: '',
                group_events: ''
            };
        },
        methods: {
            loadData() {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state.group.getData(token, this.group.id).then(result => {
                    this.group = this.$store.state.group.data;
                })
            },
            filterList(list, box, prop){
                return list.filter(elem => {
                    return elem[prop].toString().toLowerCase().includes(box.toLowerCase());
                });
            }
        },
        created() {
            this.group.id = parseInt(this.$route.params.groupId);
            if(isNaN(this.group.id)) {
                this.$router.push({name:'notFoundPage'});
            }
            this.loadData();
        },

    }
</script>
