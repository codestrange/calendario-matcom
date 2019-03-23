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
                datetimeStart: '',
                datetimeEnd: '',
                phrases: {ok: 'Aceptar',cancel: 'Cancelar'}
            }
        },
        methods: {
            eventSelected(event, jsEvent, view) {
            },
            next() {
                this.$refs.calendar.fireMethod('next');
            },
            prev() {
                this.$refs.calendar.fireMethod('prev');
            }
        },
        created() {
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
