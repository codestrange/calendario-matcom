<template>
    <div id="home">
        <div class="row">
            <div class="col">
                <div class="dropdown mb-4">
                    <button class="btn btn-light dropdown-toggle" type="button" id="asignaturas_drop_down" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
                        Asignaturas
                    </button>
                    <div class="dropdown-menu animated--fade-in " aria-labelledby="dropdownMenuButton" x-placement="bottom-start" style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 38px, 0px);">
                        <div class="input-group m-2 " v-for="it in courses" :key="it.id">
                            <div class="input-group-text bg-white">
                                <input type="checkbox" aria-label="Checkbox for following text input" v-model="it.isMarked">
                                <span class="ml-2" id="basic-">{{it.name}}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="dropdown mb-4 ">
                    <button class="btn btn-light dropdown-toggle" type="button" id="grupos_drop_down" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
                        Grupos
                    </button>
                    <div class="dropdown-menu animated--fade-in " aria-labelledby="dropdownMenuButton" x-placement="bottom-start" style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 38px, 0px);">
                        <div class="input-group m-2 " v-for="it in groups" :key="it.id">
                            <div class="input-group-text bg-white">
                                <input type="checkbox" aria-label="Checkbox for following text input" v-model="it.isMarked">
                                <span class="ml-2" id="basi7-addon3">{{it.name}}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="dropdown mb-4 ">
                    <button class="btn btn-light dropdown-toggle" type="button" id="locales_drop_down" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
                        Locales
                    </button>
                    <div class="dropdown-menu animated--fade-in " aria-labelledby="dropdownMenuButton" x-placement="bottom-start" style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 38px, 0px);">
                        <div class="input-group m-2 " v-for="it in locals" :key="it.id">
                            <div class="input-group-text bg-white">
                                <input type="checkbox" aria-label="Checkbox for following text input" v-model="it.isMarked">
                                <span class="ml-2" id="basi3-addon3">{{it.name}}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="dropdown mb-4 ">
                    <button class="btn btn-light dropdown-toggle" type="button" id="resources_drop_down" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
                        Recursos
                    </button>
                    <div class="dropdown-menu animated--fade-in " aria-labelledby="dropdownMenuButton" x-placement="bottom-start" style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 38px, 0px);">
                        <div class="input-group m-2 " v-for="it in resources" :key="it.id">
                            <div class="input-group-text bg-white">
                                <input type="checkbox" aria-label="Checkbox for following text input" v-model="it.isMarked">
                                <span class="ml-2" id="basi1-addon3">{{it.name}}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="dropdown mb-4 ">
                    <button class="btn btn-light dropdown-toggle" type="button" id="tipos_drop_down" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
                        Tipos
                    </button>
                    <div class="dropdown-menu animated--fade-in " aria-labelledby="dropdownMenuButton" x-placement="bottom-start" style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 38px, 0px);">
                        <div class="input-group m-2 " v-for="it in tags" :key="it.id">
                            <div class="input-group-text bg-white">
                                <input type="checkbox" aria-label="Checkbox for following text input" v-model="it.isMarked">
                                <span class="ml-2" id="basi5-addon3">{{it.text}}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col">
                <button class="btn btn-outline-dark" @click="makeQuery">
                    Consultar Horario
                </button>
            </div>
        </div>
        <full-calendar :events="events" :config="config" @event-selected="eventSelect"></full-calendar>
        <!-- Event Selected Modal-->
        <div class="modal fade" id="eventSelectedModal" tabindex="-1" role="dialog" aria-labelledby="eventSelectedModalLabel"
             aria-hidden="true">
            <event-shower :event-selected="eventSelected"/>
        </div>
    </div>
</template>

<script>
    import EventShower from '../components/EventInfoShower';
    import { FullCalendar } from 'vue-full-calendar';
    import 'fullcalendar/dist/locale/es';

    export default {
        name: "Home",
        components: {
            FullCalendar,
            EventShower
        },
        data () {
            return {
                courses: [],
                resources: [],
                locals: [],
                tags: [],
                groups: [],
                events: [],
                config: {
                    schedulerLicenseKey: 'GPL-My-Project-Is-Open-Source',
                    defaultView: 'month',
                    locale: 'es',
                    editable: false,
                    selectable: false,
                    navLinks: true,
                    header: {
                        left: 'prev,next today',
                        center: 'title',
                        right: 'month,agendaWeek,agendaDay,listWeek'
                    }
                },
                eventSelected: {}
            }
        },
        methods: {
            loadAll () {
                this.loadGroups();
                this.loadCourses();
                this.loadLocals();
                this.loadTags();
                this.loadResources();
            },
            loadFrom(froms, loader, to) {
                this.$store.state.user.loadMinData();
                let token = this.$store.state.user.getToken();
                this.$store.state[froms][loader](token).then(result => {
                    this[to] = this.$store.state[froms].data[froms];
                });
            },
            loadCourses () {
                this.loadFrom('courses', 'getCourcesData', 'courses');
            },
            loadResources () {
                this.loadFrom('resources', 'getResourcesData', 'resources');
            },
            loadLocals () {
                this.loadFrom('locals', 'getLocalsData', 'locals');
            },
            loadTags () {
                this.loadFrom('tags', 'getTagsData', 'tags');
            },
            loadGroups () {
                this.loadFrom('groups', 'getGroupsData', 'groups');
            },
            getMarkedData(to) {
                return (item => {
                    if (item.hasOwnProperty('isMarked') && item.isMarked) {
                        to.push(item.id);
                    }
                });
            },
            makeQuery() {
                this.$store.state.user.loadMinData();
                let token = this.$store.state.user.getToken();
                let toSendTags = [];
                let toSendCourses = [];
                let toSendGroups = [];
                let toSendLocals = [];
                let toSendResources = [];
                this.courses.forEach(this.getMarkedData(toSendCourses));
                this.tags.forEach(this.getMarkedData(toSendTags));
                this.groups.forEach(this.getMarkedData(toSendGroups));
                this.locals.forEach(this.getMarkedData(toSendLocals));
                this.resources.forEach(this.getMarkedData(toSendResources));
                this.$store.state.query.makeQuery(token, toSendCourses, toSendGroups, toSendLocals, toSendTags, toSendResources, [])
                    .then( result => {
                        if (result === true) {
                            this.events = this.$store.state.query.query_data;
                            this.events.forEach(event => {
                                event.color = '#428bca';
                                event.textColor = '#ffffff';
                            });
                        }
                        this.loadAll();
                    });
            },
            eventSelect(event, jsEvent, view) {
                // Hacer request del evento
                this.$store.state.user.loadMinData();
                let token = this.$store.state.user.getToken();
                this.$store.state.events.getEventData(token, event.id).then(result => {
                    if (result === true) {
                        this.eventSelected = this.$store.state.events.data.event;
                        $('#eventSelectedModal').modal();
                    }
                });
            }
        },
        created() {
            this.makeQuery();
        }
    }
</script>

<style>
@import '~fullcalendar/dist/fullcalendar.min.css';

.fc-event {
    cursor: pointer;
}

.fc-list-item {
    cursor: pointer;
}
</style>
