<template>
    <div id="group">
        <div class="row">
            <div class="col-12">
                <div class="card mb-4 w-100 border-bottom-primary">
                    <div class="card-header py-3 bg-white">
                        <h5 class="m-0 font-weight-bold text-primary">Tipo: {{ tag.text }}</h5>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-12">
                <div class="card mb-1 border-bottom-primary">
                    <div class="card-header bg-white">
                        <h6 class="m-0 font-weight-bold text-primary">Eventos del Tipo</h6>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <button v-if="tag.events.length === 0" type="button" class="list-group-item list-group-item-action" disabled>El tipo no tiene ningún evento asignado</button>
                            <router-link v-for="event in tag.events" :key="event.id" :to="{name: 'eventPage', params: {eventId: event.id}}" class="list-group-item list-group-item-action">{{ event.title }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Tag",
        data() {
            return {
                tag : {
                    id: -1,
                    text: '',
                    events: []
                }
            };
        },
        methods: {
            loadData() {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state.tag.getData(token, this.tag.id).then(result => {
                    if (result === true) {
                        this.tag = this.$store.state.tag.data;
                    }
                    else {
                        this.$router.push({name:'notFoundPage'});
                    }
                });
            }
        },
        created() {
            this.tag.id = parseInt(this.$route.params.tagId);
            if(isNaN(this.tag.id)) {
                this.$router.push({name:'notFoundPage'});
            }
            this.loadData();
        }
    }
</script>
