<template>
    <div id="group">
        <div class="row">
            <div class="col-12">
                <div class="card mb-2 w-100 border-bottom-primary">
                    <div class="card-header py-3 bg-white">
                        <h5 class="m-0 font-weight-bold text-primary">Evento: {{ event.title }}</h5>
                    </div>
                </div>
                <div class="card mb-2 w-100 border-bottom-grey">
                    <div class="card-header py-2 bg-white">
                        {{ render_date(event.start, event.end) }}
                    </div>
                </div>
                <div v-if="event.description" class="card mb-2 w-100 border-bottom-grey">
                    <div class="card-header py-2 bg-white">
                        <span class="font-weight-bold text-primary">Descripción:</span> {{ event.description }}
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-6">
                <div class="card mb-1 bg-white border-bottom-primary">
                    <a href="#collapseCardEventsGroups" class="d-block card-header py-3" data-toggle="collapse" role="button" aria-expanded="false" aria-controls="collapseCardEventsGroups">
                        <h6 class="m-0 font-weight-bold text-primary">Grupos del Evento</h6>
                    </a>
                    <div class="collapse hide" id="collapseCardEventsGroups" style="">
                        <div class="card-body p-2">
                            <div class="row">
                                <div class="col-9">
                                    <input type="text w-100" v-model="event_groups" class="form-control bg-light border-0 small" placeholder="Buscar ..." aria-label="Search" aria-describedby="basic-addon2">
                                </div>
                                <div class="col-3">
                                    <button class="btn ml-2" @click.prevent="setVal(5)">
                                        <i class="fas fa-sort-alpha-down"></i>
                                    </button>
                                    <button class="btn ml-2" @click.prevent="unsetVal(5)">
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
                            <button v-if="event.groups.length === 0" type="button" class="list-group-item list-group-item-action" disabled>El evento no tiene ningún grupo asignado</button>
                            <button v-else-if="filterList(event.groups, event_groups, 'name', gropus_val).length === 0" type="button" class="list-group-item list-group-item-action" disabled>No hay resultados para mostrar</button>
                            <router-link v-for="group in filterList(event.groups, event_groups, 'name', gropus_val)" :key="group.id" :to="{name: 'groupPage', params: {groupId: group.id}}" class="list-group-item list-group-item-action">{{ group.name }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-6">
                <div class="card mb-1 bg-white border-bottom-primary">
                    <a href="#collapseCardEventsRooms" class="d-block card-header py-3" data-toggle="collapse" role="button" aria-expanded="false" aria-controls="collapseCardEventsRooms">
                        <h6 class="m-0 font-weight-bold text-primary">Locales del Evento</h6>
                    </a>
                    <div class="collapse hide" id="collapseCardEventsRooms" style="">
                        <div class="card-body p-2">
                            <div class="row">
                                <div class="col-9">
                                    <input type="text w-100" v-model="event_rooms" class="form-control bg-light border-0 small" placeholder="Buscar ..." aria-label="Search" aria-describedby="basic-addon2">
                                </div>
                                <div class="col-3">
                                    <button class="btn ml-2" @click.prevent="setVal(4)">
                                        <i class="fas fa-sort-alpha-down"></i>
                                    </button>
                                    <button class="btn ml-2" @click.prevent="unsetVal(4)">
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
                            <button v-if="event.locals.length === 0" type="button" class="list-group-item list-group-item-action" disabled>El evento no tiene ningún local asignado</button>
                            <button v-else-if="filterList(event.locals, event_rooms, 'name', rooms_val).length === 0" type="button" class="list-group-item list-group-item-action" disabled>No hay resultados para mostrar</button>
                            <router-link v-for="local in filterList(event.locals, event_rooms, 'name', rooms_val)" :key="local.id" :to="{name: 'localPage', params: {localId: local.id}}" class="list-group-item list-group-item-action">{{ local.name }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row mt-2">
            <div class="col-4">
                <div class="card mb-1 bg-white border-bottom-primary">
                    <a href="#collapseCardEventsCources" class="d-block card-header py-3" data-toggle="collapse" role="button" aria-expanded="false" aria-controls="collapseCardEventsCources">
                        <h6 class="m-0 font-weight-bold text-primary">Asignaturas del Evento</h6>
                    </a>
                    <div class="collapse hide" id="collapseCardEventsCources" style="">
                        <div class="card-body p-2">
                            <div class="row justify-content-center">
                                <form class="form-inline">
                                    <input type="text" v-model="event_cources" class="form-control bg-light border-0 small" placeholder="Buscar ..." aria-label="Search" aria-describedby="basic-addon2">
                                    <button class="btn ml-2" @click.prevent="setVal(3)">
                                        <i class="fas fa-sort-alpha-down"></i>
                                    </button>
                                    <button class="btn ml-2" @click.prevent="unsetVal(3)">
                                        <i class="fas fa-sort-alpha-up"></i>
                                    </button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <button v-if="event.courses.length === 0" type="button" class="list-group-item list-group-item-action" disabled>El evento no tiene ningún asignatura asignado</button>
                            <button v-else-if="filterList(event.courses, event_cources, 'name', cources_val).length === 0" type="button" class="list-group-item list-group-item-action" disabled>No hay resultados para mostrar</button>
                            <router-link v-for="course in filterList(event.courses, event_cources, 'name', cources_val)" :key="course.id" :to="{name: 'coursePage', params: {courseId: course.id}}" class="list-group-item list-group-item-action">{{ course.name }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-4">
                <div class="card mb-1 bg-white border-bottom-primary">
                    <a href="#collapseCardEventsResources" class="d-block card-header py-3" data-toggle="collapse" role="button" aria-expanded="false" aria-controls="collapseCardEventsResources">
                        <h6 class="m-0 font-weight-bold text-primary">Recursos del Evento</h6>
                    </a>
                    <div class="collapse hide" id="collapseCardEventsResources" style="">
                        <div class="card-body p-2">
                            <div class="row justify-content-center">
                                <form class="form-inline">
                                    <input type="text" v-model="event_resources" class="form-control bg-light border-0 small" placeholder="Buscar ..." aria-label="Search" aria-describedby="basic-addon2">
                                    <button class="btn ml-2" @click.prevent="setVal(1)">
                                        <i class="fas fa-sort-alpha-down"></i>
                                    </button>
                                    <button class="btn ml-2" @click.prevent="unsetVal(1)">
                                        <i class="fas fa-sort-alpha-up"></i>
                                    </button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <button v-if="event.resources.length === 0" type="button" class="list-group-item list-group-item-action" disabled>El evento no tiene ningún recurso asignado</button>
                            <button v-else-if="filterList(event.resources, event_resources, 'name', resources_val).length === 0" type="button" class="list-group-item list-group-item-action" disabled>No hay resultados para mostrar</button>
                            <router-link v-for="resource in filterList(event.resources, event_resources, 'name', resources_val)" :key="resource.id" :to="{name: 'resourcePage', params: {resourceId: resource.id}}" class="list-group-item list-group-item-action">{{ resource.name }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-4">
                <div class="card mb-1 bg-white border-bottom-primary">
                    <a href="#collapseCardEventsTypes" class="d-block card-header py-3" data-toggle="collapse" role="button" aria-expanded="false" aria-controls="collapseCardEventsTypes">
                        <h6 class="m-0 font-weight-bold text-primary">Tipos del Evento</h6>
                    </a>
                    <div class="collapse hide" id="collapseCardEventsTypes" style="">
                        <div class="card-body p-2">
                            <div class="row justify-content-center">
                                <form class="form-inline">
                                    <input type="text" v-model="event_types" class="form-control bg-light border-0 small" placeholder="Buscar ..." aria-label="Search" aria-describedby="basic-addon2">
                                    <button class="btn ml-2" @click.prevent="setVal(2)">
                                        <i class="fas fa-sort-alpha-down"></i>
                                    </button>
                                    <button class="btn ml-2" @click.prevent="unsetVal(2)">
                                        <i class="fas fa-sort-alpha-up"></i>
                                    </button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <button v-if="event.tags.length === 0" type="button" class="list-group-item list-group-item-action" disabled>El evento no tiene ningún tipo asignado</button>
                            <button v-else-if="filterList(event.tags, event_types, 'text', types_val).length === 0" type="button" class="list-group-item list-group-item-action" disabled>No hay resultados para mostrar</button>
                            <router-link v-for="tag in filterList(event.tags, event_types, 'text', types_val)" :key="tag.id" :to="{name: 'tagPage', params: {tagId: tag.id}}" class="list-group-item list-group-item-action">{{ tag.text }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import { renderPresentation } from '../utils/render_date';

    export default {
        name: "Group",
        data() {
            return {
                event : {
                    id: -1,
                    title: '',
                    courses: [],
                    groups: [],
                    locals: [],
                    resources: [],
                    tags: []
                },
                event_resources: '',
                event_types: '',
                event_cources: '',
                event_rooms: '',
                event_groups: '',
                resources_val: 1,
                types_val: 1,
                cources_val: 1,
                rooms_val: 1,
                gropus_val: 1

            };
        },
        methods: {
            loadData() {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state.event.getData(token, this.event.id).then(result => {
                    this.event = this.$store.state.event.data;
                });
            },
            render_date(start, end) {
                return renderPresentation(start, end);
            },
            filterList(list, box, prop, val){
                let tmp = list.sort(this.comparer(prop , val))
                return list.filter(elem => {
                    return elem[prop].toString().toLowerCase().includes(box.toLowerCase());
                });
            },
            setVal(number){
                if (number == 1){
                    this.resources_val = 1;
                }
                else if (number == 2){
                    this.types_val = 1;
                }
                else if (number == 3){
                    this.cources_val = 1;
                }
                else if (number == 4){
                    this.rooms_val = 1;
                }
                else{
                    this.gropus_val = 1;
                }
            },
            unsetVal(number){
                if (number == 1){
                    this.resources_val = -1;
                }
                else if (number == 2){
                    this.types_val = -1;
                }
                else if (number == 3){
                    this.cources_val = -1;
                }
                else if (number == 4){
                    this.rooms_val = -1;
                }
                else{
                    this.gropus_val = -1;
                }
            },
            comparer(prop, val){
                return function (a,b) {
                    if (a[prop] > b[prop]) {
                        return 1 * val;
                    } else if (a[prop] < b[prop]) {
                        return -1 * val;
                    } else {
                        return 0;
                    }
                }
            }
        },
        created() {
            this.event.id = parseInt(this.$route.params.eventId);
            if(isNaN(this.event.id)) {
                this.$router.push({name:'notFoundPage'});
            }
            this.loadData();
        }
    }
</script>
