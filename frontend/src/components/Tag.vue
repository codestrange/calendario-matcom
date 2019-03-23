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
                <div class="card mb-1 bg-white border-bottom-primary">
                    <a href="#collapseCardTypesEvents" class="d-block card-header py-3" data-toggle="collapse" role="button" aria-expanded="false" aria-controls="collapseCardTypesEvents">
                        <h6 class="m-0 font-weight-bold text-primary">Eventos del Tipo</h6>
                    </a>
                    <div class="collapse hide" id="collapseCardTypesEvents" style="">
                        <div class="card-body p-2">
                            <div class="row justify-content-center">
                                <div class="col-10">
                                    <input type="text" v-model="type_events" class="form-control bg-light border-0 small" placeholder="Buscar ..." aria-label="Search" aria-describedby="basic-addon2">
                                </div>
                                <div class="col-lg-2">
                                    <button class="btn ml-4">
                                        <i class="fas fa-sort-alpha-down"></i>
                                    </button>
                                    <button class="btn ml-4">
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
                            <button v-if="tag.events.length === 0" type="button" class="list-group-item list-group-item-action" disabled>El tipo no tiene ningún evento asignado</button>
                            <button v-else-if="filterList(tag.events, type_events, 'title').length === 0" type="button" class="list-group-item list-group-item-action" disabled>No hay resultados para mostrar</button>
                            <router-link v-for="event in filterList(tag.events, type_events, 'title')" :key="event.id" :to="{name: 'eventPage', params: {eventId: event.id}}" class="list-group-item list-group-item-action">{{ event.title }}</router-link>
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
                },
                type_events: ''
            };
        },
        methods: {
            loadData() {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state.tag.getData(token, this.tag.id).then(result => {
                    this.tag = this.$store.state.tag.data;
                });
            },
            filterList(list, box, prop){
                return list.filter(elem => {
                    return elem[prop].toString().toLowerCase().includes(box.toLowerCase());
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
