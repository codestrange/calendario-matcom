<template>
    <div id="class_editor">
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
                events: [],
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
            }
        },
        methods: {
            eventSelected(event, jsEvent, view) {
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
                let year = date.getFullYear();
                let month = date.getMonth() + 1;
                if (parseInt(month) < 10) {
                    month = '0' + month;
                }
                let day = date.getDate() + 1;
                if (parseInt(day) < 10) {
                    day = '0' + day;
                }
                console.log(year + '-' + month + '-' + day + 'T00:00:00.000Z');
                return year + '-' + month + '-' + day + 'T00:00:00.000Z';
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
            addFakeEvents(fixed_events) {
                return fixed_events;
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
                            this.events = this.addFakeEvents(this.$store.state.query.data);
                        }
                });
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
