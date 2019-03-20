<template>
    <div id="home">
        <div class="row">
            <div class="col">
                <div class="dropdown mb-0">
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
                <div class="dropdown mb-0">
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
                <div class="dropdown mb-0">
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
                <div class="dropdown mb-0">
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
                <div class="dropdown mb-0">
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
                <button class="btn btn-block btn-outline-dark" @click="makeQuery">
                    Filtrar
                </button>
            </div>
        </div>
        <div class="row">
            <div class="card-body mt-0" @click.stop style="width: 200px">
                <div class="row ml-5">
                    <div class="col-1">
                        <h1 class="h5 text-dark mt-1">Desde:</h1>
                    </div>
                    <div class="col-5">
                        <datetime  type="datetime" :phrases="phrases" v-model="datetimeStart" ></datetime>
                    </div>
                    <div class="col-1">
                        <h1 class="h5 text-dark mt-1 ">Hasta:</h1>
                    </div>
                    <div class="col-5">
                        <datetime type="datetime" :phrases="phrases" v-model="datetimeEnd"></datetime>
                    </div>
                </div>
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
    import 'fullcalendar/dist/fullcalendar.css';
    import 'fullcalendar/dist/locale/es';
    import { Datetime } from 'vue-datetime';
    import 'vue-datetime/dist/vue-datetime.css';
    import { Settings } from 'luxon';

    Settings.defaultLocale = 'es';

    export default {
        name: "Home",
        components: {
            Datetime,
            EventShower,
            FullCalendar
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
                datetimeStart: '',
                datetimeEnd: '',
                phrases: {ok: 'Aceptar',cancel: 'Cancelar'},
                eventSelected: {}
            }
        },
        methods: {
            loadAll () {
                this.loadFrom('courses');
                this.loadFrom('groups');
                this.loadFrom('locals');
                this.loadFrom('resources');
                this.loadFrom('tags');
            },
            loadFrom(arg) {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state[arg].getData(token).then(result => {
                    this[arg] = this.$store.state[arg].data;
                });
            },
            getMarkedData(to) {
                return (item => {
                    if (item.hasOwnProperty('isMarked') && item.isMarked) {
                        to.push(item.id);
                    }
                });
            },
            makeQuery() {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                let toSendTags = [];
                let toSendCourses = [];
                let toSendGroups = [];
                let toSendLocals = [];
                let toSendResources = [];
                let toSendStartDate = null;
                let toSendEndDate = null;
                this.courses.forEach(this.getMarkedData(toSendCourses));
                this.tags.forEach(this.getMarkedData(toSendTags));
                this.groups.forEach(this.getMarkedData(toSendGroups));
                this.locals.forEach(this.getMarkedData(toSendLocals));
                this.resources.forEach(this.getMarkedData(toSendResources));
                if (this.datetimeStart !== '') {
                    toSendStartDate = this.datetimeStart;
                }
                if (this.datetimeEnd !== '') {
                    toSendEndDate = this.datetimeEnd;
                }
                this.$store.state.query.makeQuery(token, toSendCourses, toSendGroups, toSendLocals, toSendTags, toSendResources, [], toSendStartDate, toSendEndDate)
                    .then(result => {
                        if (result === true) {
                            this.events = this.$store.state.query.data;
                            this.events.forEach(event => {
                                event.color = '#428bca';
                                event.textColor = '#ffffff';
                            });
                        }
                        this.loadAll();
                    });
            },
            eventSelect(event, jsEvent, view) {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state.event.getData(token, event.id).then(result => {
                    if (result === true) {
                        this.eventSelected = this.$store.state.event.data;
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
