<template>
    <div id="class_editor">
        <div class="row">
            <div class="col-4"></div>
            <div class="col-4">
                <div class="row justify-content-center">
                    <span class="h5 text-primary mr-0">Editando Horario del Grupo {{this.selectedGroupData.name}}</span>
                </div>
            </div>
            <div class="col-4">
                <div class="row justify-content-end">
                    <form class="form-inline">
                        <button class="btn ml-3" @click.prevent="prev">
                            <i class="fas fa-arrow-left"></i>
                        </button>
                        <button class="btn ml-3" @click.prevent="next">
                            <i class="fas fa-arrow-right"></i>
                        </button>
                    </form>
                </div>
            </div>
        </div>
        <div id="eventSelectedModal" class="modal fade" tabindex="-1" role="dialog"
             aria-labelledby="eventSelectedModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-lg" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <span class="h3 text-dark mb-0">Agregue los Datos del Evento</span>
                        <button class="close mb-0" type="button" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">x</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <div class="form-group mb-3 text-dark">
                            <label for="labelInputTitle">Título:</label>
                            <input type="text" class="form-control" id="labelInputTitle" v-model="selectedEvent.title">
                        </div>
                        <div class="form-group mb-3 text-dark">
                            <label for="labelInputDescription">Descripción:</label>
                            <textarea class="form-control" id="labelInputDescription" v-model="selectedEvent.description"></textarea>
                        </div>
                        <div class="row">
                            <div class="col-3">
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
                            <div class="col-3">
                                <div class="dropdown mb-0">
                                    <button class="btn btn-light dropdown-toggle" type="button" id="locales_drop_down" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
                                        Locales
                                    </button>
                                    <div class="dropdown-menu animated--fade-in " aria-labelledby="dropdownMenuButton" x-placement="bottom-start" style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 38px, 0px);">
                                        <div class="input-group m-2 " v-for="it in free_locals" :key="it.id">
                                            <div class="input-group-text bg-white">
                                                <input type="checkbox" aria-label="Checkbox for following text input" v-model="it.isMarked">
                                                <span class="ml-2" id="basi3-addon3">{{it.name}}</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-3">
                                <div class="dropdown mb-0">
                                    <button class="btn btn-light dropdown-toggle" type="button" id="resources_drop_down" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
                                        Recursos
                                    </button>
                                    <div class="dropdown-menu animated--fade-in " aria-labelledby="dropdownMenuButton" x-placement="bottom-start" style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 38px, 0px);">
                                        <div class="input-group m-2 " v-for="it in free_resources" :key="it.id">
                                            <div class="input-group-text bg-white">
                                                <input type="checkbox" aria-label="Checkbox for following text input" v-model="it.isMarked">
                                                <span class="ml-2" id="basi1-addon3">{{it.name}}</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-3">
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
                        </div>
                        <div class="row justify-content-center mt-2">
                            <button class="btn btn-primary text-white" @click="confirmCreation" data-dismiss="modal">
                                Confirmar
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <full-calendar ref="calendar" :events="events" :config="config" @event-selected="eventSelected"></full-calendar>
    </div>
</template>

<script>
    import { FullCalendar } from 'vue-full-calendar';
    import 'fullcalendar/dist/fullcalendar.css';
    import 'fullcalendar/dist/locale/es';
    import { Settings } from 'luxon';

    Settings.defaultLocale = 'es';

    export default {
        name: "Editor",
        components: {
            FullCalendar
        },
        data () {
            return {
                selectedEvent: {},
                courses: [],
                free_resources: [],
                free_locals: [],
                tags: [],
                events: [],
                selectedGroupData: {},
                config: {
                    schedulerLicenseKey: 'GPL-My-Project-Is-Open-Source',
                    defaultView: 'agendaWeek',
                    locale: 'es',
                    editable: false,
                    selectable: false,
                    navLinks: false,
                    weekNumbers: true,
                    weekNumberTitle: 'S ',
                    hiddenDays: [6, 0],
                    header: {
                        left: '',
                        center: 'title',
                        right: ''
                    },
                    scrollTime: '08:00:00',
                    minTime: '08:00:00',
                    maxTime: '18:30:00',
                    allDaySlot: false
                },
                fake_intervals: []
            }
        },
        methods: {
            loadAll () {
                this.loadFrom('courses');
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
            eventSelected(event, jsEvent, view) {
                let start = event.start;
                let end = event.end;
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state.free_locals.getData(token, start, end).then(result => {
                    if (result === true) {
                        this.free_locals = this.$store.state.free_locals.data;
                        this.$store.state.free_resources.getData(token, start, end).then(result => {
                            if (result === true) {
                                this.free_resources = this.$store.state.free_resources.data;
                                this.selectedEvent = Object.assign({}, event);
                                this.selectedEvent.title = '';
                                this.selectedEvent.description = '';
                                console.log(this.selectedEvent);
                                console.log(event);
                                $('#eventSelectedModal').modal();
                            }
                        });
                    }
                });
            },
            next() {
                this.$refs.calendar.fireMethod('next');
                this.loadEvents();
            },
            prev() {
                this.$refs.calendar.fireMethod('prev');
                this.loadEvents();
            },
            dateToString(date) {
                return date.toISOString();
            },
            startDate() {
                let sdate = this.$refs.calendar.fireMethod('getDate');
                let date = sdate._d;
                return this.dateToString(date);
            },
            endDate() {
                let sdate = this.$refs.calendar.fireMethod('getDate');
                let date = sdate._d;
                date.setDate(date.getDate() + 6);
                return this.dateToString(date);
            },
            addFakeEvents(used_intervals) {
                let finals = [];
                this.fake_intervals.forEach(fake => {
                    let b = true;
                    used_intervals.forEach( used => {
                        b &= this.checkCollition(used, fake);
                    });
                    if (b) {
                        finals.push(fake);
                    }
                });
                used_intervals.forEach(used => {
                    used.isFake = false;
                    finals.push(used);
                });
                return finals;
            },
            updateVisualStyle() {
                this.events.forEach(event => {
                    event.textColor = event.isFake ? '#428bca' : '#ffffff';
                    event.color = event.isFake ? '#f5f5f0' : '#428bca';
                });
            },
            loadEvents() {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                let toSendTags = [];
                let toSendCourses = [];
                let toSendGroups = [ parseInt(this.$route.params.groupId) ];
                let toSendLocals = [];
                let toSendResources = [];
                let toSendUsers = [];
                let toSendStartDate = this.startDate();
                let toSendEndDate = this.endDate();
                this.$store.state.query.makeQuery(token, toSendCourses, toSendGroups, toSendLocals, toSendTags, toSendResources, toSendUsers, toSendStartDate, toSendEndDate)
                    .then(result => {
                        if (result === true) {
                            this.$store.state.intervals.getData(token).then( result => {
                                if (result === true) {
                                    this.fake_intervals = this.buildAllFakeEvents(this.$store.state.intervals.data);
                                    this.events = this.addFakeEvents(this.$store.state.query.data);
                                    this.updateVisualStyle();
                                }
                            });
                        }
                });
            },
            checkCollition (inter1, inter2) {
                let s1 = new Date(inter1.start);
                let e1 = new Date(inter1.end);
                let s2 = new Date(inter2.start);
                let e2 = new Date(inter2.end);
                return (s1.getTime() > e2.getTime() || e1.getTime() < s2.getTime());
            },
            buildAllFakeEvents(intervals) {
                let fakes = [];
                intervals.forEach( interval => {
                    for (let i = 0; i < 5; ++i) {
                        let fakeI = {};
                        fakeI.isFake = true;
                        fakeI.title = interval.name;
                        let s = new Date(this.startDate());
                        s.setDate(s.getDate() + i);
                        s.setHours(s.getHours() + parseInt(interval.start[0]+interval.start[1]));
                        s.setMinutes(s.getMinutes() + parseInt(interval.start[3]+interval.start[4]));
                        s.setSeconds(s.getSeconds() + parseInt(interval.start[6]+interval.start[7]));
                        let e = new Date(this.startDate());
                        e.setDate(e.getDate() + i);
                        e.setHours(e.getHours() + parseInt(interval.end[0]+interval.end[1]));
                        e.setMinutes(e.getMinutes() + parseInt(interval.end[3]+interval.end[4]));
                        e.setSeconds(e.getSeconds() + parseInt(interval.end[6]+interval.end[7]));
                        fakeI.start = s.toISOString();
                        fakeI.end = e.toISOString();
                        fakes.push(fakeI);
                    }
                });
                return fakes;
            },
            confirmCreation() {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                let toSendTitle = this.selectedEvent.title;
                let toSendDesc = this.selectedEvent.description;
                let toSendTags = [];
                let toSendCourses = [];
                let toSendGroups = [ parseInt(this.$route.params.groupId) ];
                let toSendLocals = [];
                let toSendResources = [];
                let toSendStartDate = this.selectedEvent.start.toISOString();
                let toSendEndDate = this.selectedEvent.end.toISOString();
                this.courses.forEach(this.getMarkedData(toSendCourses));
                this.tags.forEach(this.getMarkedData(toSendTags));
                this.free_locals.forEach(this.getMarkedData(toSendLocals));
                this.free_resources.forEach(this.getMarkedData(toSendResources));
                if ( this.selectedEvent.isFake === true ) {
                    this.$store.state.events.createEvent(token, {
                        title: toSendTitle,
                        description: toSendDesc,
                        start: toSendStartDate,
                        end: toSendEndDate,
                        resources: toSendResources,
                        tags: toSendTags,
                        groups: toSendGroups,
                        courses: toSendCourses,
                        locals: toSendLocals
                    }).then(result => {
                        if (result === true) {
                            this.loadEvents();
                        }
                    });
                }
                else {
                    let toSendId = parseInt(this.selectedEvent.id);
                    this.$store.state.events.updateEvent(token, {
                        id: toSendId,
                        title: toSendTitle,
                        description: toSendDesc,
                        start: toSendStartDate,
                        end: toSendEndDate,
                        resources: toSendResources,
                        tags: toSendTags,
                        groups: toSendGroups,
                        courses: toSendCourses,
                        locals: toSendLocals
                    }).then(result => {
                        if (result === true) {
                            this.loadEvents();
                        }
                    });
                }
            }
        },
        created() {
            this.$store.state.profile.loadMinData();
            let token = this.$store.state.profile.data.token;
            let id = this.$route.params.groupId;
            this.$store.state.group.getData(token, id).then(result => {
                if (result === true) {
                    this.next();
                    this.prev();
                    this.selectedGroupData = this.$store.state.group.data;
                    this.loadAll();
                }
                else {
                    this.$router.push({name:'notFoundPage'});
                }
            });
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
