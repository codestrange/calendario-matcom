<template>
    <div id="group">
        <div class="row">
            <div class="col-12">
                <div class="card mb-4 w-100 border-bottom-primary">
                    <div class="card-header py-3 bg-white">
                        <h5 class="m-0 font-weight-bold text-primary">Recurso: {{ resource.name }}</h5>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-12">
                <div class="card mb-1 border-bottom-primary">
                    <div class="card-header bg-white">
                        <h6 class="m-0 font-weight-bold text-primary">Eventos del Recurso</h6>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <button v-if="resource.events.length === 0" type="button" class="list-group-item list-group-item-action" disabled>El recurso no tiene ningún evento asignado</button>
                            <router-link v-for="event in resource.events" :key="event.id" :to="{name: 'eventPage', params: {eventId: event.id}}" class="list-group-item list-group-item-action">{{ event.title }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Resource",
        data() {
            return {
                resource : {
                    id: -1,
                    name: '',
                    events: []
                }
            };
        },
        methods: {
            loadData() {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state.resource.getData(token, this.resource.id).then(result => {
                    if (result === true) {
                        this.resource = this.$store.state.resource.data;
                    }
                    else {
                        this.$router.push({name:'notFoundPage'});
                    }
                });
            }
        },
        created() {
            this.resource.id = parseInt(this.$route.params.resourceId);
            if(isNaN(this.resource.id)) {
                this.$router.push({name:'notFoundPage'});
            }
            this.loadData();
        }
    }
</script>
