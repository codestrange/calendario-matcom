<template>
    <div id="home">
        <div class="row">
            <div class="col">
                <div class="dropdown mb-4">
                    <button class="btn btn-light dropdown-toggle" type="button" id="asignaturas_drop_down" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true" @click="loadCourses">
                        Asignaturas
                    </button>
                    <div class="dropdown-menu animated--fade-in " aria-labelledby="dropdownMenuButton" x-placement="bottom-start" style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 38px, 0px);">
                        <div class="input-group m-2 " v-for="it in courses" :key="it.id">
                            <div class="input-group-text bg-white">
                                <input type="checkbox" aria-label="Checkbox for following text input" @click="markItem(it)">
                                <span class="ml-2" id="basic-">{{it.name}}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="dropdown mb-4 ">
                    <button class="btn btn-light dropdown-toggle" type="button" id="resources_drop_down" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true" @click="loadResources">
                        Recursos
                    </button>
                    <div class="dropdown-menu animated--fade-in " aria-labelledby="dropdownMenuButton" x-placement="bottom-start" style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 38px, 0px);">
                        <div class="input-group m-2 " v-for="it in resources" :key="it.id">
                            <div class="input-group-text bg-white">
                                <input type="checkbox" aria-label="Checkbox for following text input">
                                <span class="ml-2" id="basi1-addon3">{{it.name}}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="dropdown mb-4 ">
                    <button class="btn btn-light dropdown-toggle" type="button" id="locales_drop_down" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true" @click="loadLocals">
                        Locales
                    </button>
                    <div class="dropdown-menu animated--fade-in " aria-labelledby="dropdownMenuButton" x-placement="bottom-start" style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 38px, 0px);">
                        <div class="input-group m-2 " v-for="it in locals" :key="it.id">
                            <div class="input-group-text bg-white">
                                <input type="checkbox" aria-label="Checkbox for following text input">
                                <span class="ml-2" id="basi3-addon3">{{it.name}}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="dropdown mb-4 ">
                    <button class="btn btn-light dropdown-toggle" type="button" id="tipos_drop_down" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true" @click="loadTags">
                        Tipos
                    </button>
                    <div class="dropdown-menu animated--fade-in " aria-labelledby="dropdownMenuButton" x-placement="bottom-start" style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 38px, 0px);">
                        <div class="input-group m-2 " v-for="it in tags" :key="it.id">
                            <div class="input-group-text bg-white">
                                <input type="checkbox" aria-label="Checkbox for following text input">
                                <span class="ml-2" id="basi5-addon3">{{it.text}}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="dropdown mb-4 ">
                    <button class="btn btn-light dropdown-toggle" type="button" id="grupos_drop_down" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true" @click="loadGroups">
                        Grupos
                    </button>
                    <div class="dropdown-menu animated--fade-in " aria-labelledby="dropdownMenuButton" x-placement="bottom-start" style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 38px, 0px);">
                        <div class="input-group m-2 " v-for="it in groups" :key="it.id">
                            <div class="input-group-text bg-white">
                                <input type="checkbox" aria-label="Checkbox for following text input">
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
        <full-calendar :events="events" :config="config"></full-calendar>
    </div>
</template>

<script>
    import { FullCalendar } from 'vue-full-calendar';
    import 'fullcalendar/dist/locale/es.js';

    export default {
        name: "Home",
        components: {
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
                    header: {
                        left: 'prev,next today',
                        center: 'title',
                        right: 'month,agendaWeek,agendaDay,list'
                    }
                }
            }
        },
        methods: {
            loadCourses () {
                this.$store.state.user.loadMinData();
                let token = this.$store.state.user.getToken();
                this.$store.state.courses.loadMinData();
                if (this.$store.state.courses.data.courses.length !== 0) {
                    this.courses = this.$store.state.courses.data.courses;
                }
                else {
                    this.$store.state.courses.getCourcesData(token).then(result => {
                        this.courses = this.$store.state.courses.data.courses;
                    });
                }
            },
            loadResources () {
                this.$store.state.user.loadMinData();
                let token = this.$store.state.user.getToken();
                this.$store.state.resources.loadMinData();
                if (this.$store.state.resources.data.resources.length !== 0) {
                    this.resources = this.$store.state.resources.data.resources;
                }
                else {
                    this.$store.state.resources.getResourcesData(token).then(result => {
                        this.resources = this.$store.state.resources.data.resources;
                    });
                }
            },
            loadLocals () {
                this.$store.state.user.loadMinData();
                let token = this.$store.state.user.getToken();
                this.$store.state.locals.loadMinData();
                if (this.$store.state.locals.data.locals.length !== 0) {
                    this.locals = this.$store.state.locals.data.locals;
                }
                else {
                    this.$store.state.locals.getLocalsData(token).then(result => {
                        this.locals = this.$store.state.locals.data.locals;
                    });
                }
            },
            loadTags () {
                this.$store.state.user.loadMinData();
                let token = this.$store.state.user.getToken();
                this.$store.state.tags.loadMinData();
                if (this.$store.state.tags.data.tags.length !== 0) {
                    this.tags = this.$store.state.tags.data.tags;
                }
                else {
                    this.$store.state.tags.getTagsData(token).then(result => {
                        this.tags = this.$store.state.tags.data.tags;
                    });
                }
            },
            loadGroups () {
                this.$store.state.user.loadMinData();
                let token = this.$store.state.user.getToken();
                this.$store.state.groups.loadMinData();
                if (this.$store.state.groups.data.groups.length !== 0) {
                    this.groups = this.$store.state.groups.data.groups;
                }
                else {
                    this.$store.state.groups.getGroupsData(token).then(result => {
                        this.groups = this.$store.state.groups.data.groups;
                    });
                }
            },
            markItem(item) {
                if (item.hasOwnProperty('isMarked')) {
                    item.isMarked = !item.isMarked;
                }
                else {
                    item.isMarked = true;
                }
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
                        toSendCourses.push({
                            id: course.id
                        });
                    }
                });
                this.tags.forEach(tag => {
                    if (tag.hasOwnProperty('isMarked') && tag.isMarked) {
                        toSendTags.push({
                            id: tag.id
                        });
                    }
                });
                this.groups.forEach(group => {
                    if (group.hasOwnProperty('isMarked') && group.isMarked) {
                        toSendGroups.push({
                            id: group.id
                        });
                    }
                });
                this.locals.forEach(local => {
                    if (local.hasOwnProperty('isMarked') && local.isMarked) {
                        toSendLocals.push({
                            id: local.id
                        });
                    }
                });
                this.resources.forEach(resource => {
                    if (resource.hasOwnProperty('isMarked') && resource.isMarked) {
                        toSendResources.push({
                            id: resource.id
                        });
                    }
                });
                this.$store.state.query.makeQuery(token, toSendCourses, toSendGroups, toSendLocals, toSendTags, toSendResources, [])
                    .then( result => {
                        if (result === true) {
                            this.events = this.$store.state.query.query_data;
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
@import '~fullcalendar/dist/fullcalendar.css';
</style>