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
                fake_intervals: []
            }
        },
        methods: {
            eventSelected(event, jsEvent, view) {
                console.log(event);
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
                    finals.push(used);
                });
                return finals;
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
