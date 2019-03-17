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
                <button class="btn btn-outline-dark" @click="makeQuery">
                    Consultar Horario
                </button>
            </div>
        </div>
        <div class="row">
            <div class="col text-center">
                <datetime class="align-items-center" type="datetime" v-model="datetime"></datetime>
            </div>
        </div>
        <div class="row">
            <div class="col text-center">
                <datetime class="align-items-center" type="datetime" v-model="datetime"></datetime>
            </div>
        </div>
        <full-calendar :events="events" :config="config" @event-selected="eventSelected"></full-calendar>
    </div>
</template>

<script>
    import { FullCalendar } from 'vue-full-calendar';
    import 'fullcalendar/dist/fullcalendar.css';
    import 'fullcalendar/dist/locale/es';
    import { Datetime } from 'vue-datetime';
    import 'vue-datetime/dist/vue-datetime.css';

    export default {
        name: "Home",
        components: {
            FullCalendar,
            Datetime
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
                datetime: '2018-05-12T20:19:06.151Z'
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
            loadCourses () {
                this.$store.state.user.loadMinData();
                let token = this.$store.state.user.getToken();
                this.$store.state.courses.getCourcesData(token).then(result => {
                    this.courses = this.$store.state.courses.data.courses;
                });
            },
            loadResources () {
                this.$store.state.user.loadMinData();
                let token = this.$store.state.user.getToken();
                this.$store.state.resources.getResourcesData(token).then(result => {
                    this.resources = this.$store.state.resources.data.resources;
                });
            },
            loadLocals () {
                this.$store.state.user.loadMinData();
                let token = this.$store.state.user.getToken();
                this.$store.state.locals.getLocalsData(token).then(result => {
                    this.locals = this.$store.state.locals.data.locals;
                });
            },
            loadTags () {
                this.$store.state.user.loadMinData();
                let token = this.$store.state.user.getToken();
                this.$store.state.tags.getTagsData(token).then(result => {
                    this.tags = this.$store.state.tags.data.tags;
                });
            },
            loadGroups () {
                this.$store.state.user.loadMinData();
                let token = this.$store.state.user.getToken();
                this.$store.state.groups.getGroupsData(token).then(result => {
                    this.groups = this.$store.state.groups.data.groups;
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
                this.courses.forEach(course => {
                    if (course.hasOwnProperty('isMarked') && course.isMarked) {
                        toSendCourses.push(course.id);
                    }
                });
                this.tags.forEach(tag => {
                    if (tag.hasOwnProperty('isMarked') && tag.isMarked) {
                        toSendTags.push(tag.id);
                    }
                });
                this.groups.forEach(group => {
                    if (group.hasOwnProperty('isMarked') && group.isMarked) {
                        toSendGroups.push(group.id);
                    }
                });
                this.locals.forEach(local => {
                    if (local.hasOwnProperty('isMarked') && local.isMarked) {
                        toSendLocals.push(local.id);
                    }
                });
                this.resources.forEach(resource => {
                    if (resource.hasOwnProperty('isMarked') && resource.isMarked) {
                        toSendResources.push(resource.id);
                    }
                });
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
            eventSelected(event, jsEvent, view) {
                // Hacer request del evento
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
