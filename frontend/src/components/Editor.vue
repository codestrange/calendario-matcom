<template>
    <div id="class_editor">
        <full-calendar :events="events" :config="config" @event-selected="eventSelected"></full-calendar>
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
                    navLinks: true,
                    header: {
                        left: 'prev,next',
                        center: 'title',
                        right: 'agendaWeek,agendaDay'
                    },
                    scrollTime: '08:00:00'
                },
                datetimeStart: '',
                datetimeEnd: '',
                phrases: {ok: 'Aceptar',cancel: 'Cancelar'}
            }
        },
        methods: {
            eventSelected(event, jsEvent, view) {
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
