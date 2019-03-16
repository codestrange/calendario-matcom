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
                                <input type="checkbox" aria-label="Checkbox for following text input">
                                <span class="ml-2" id="basic-">{{it}}</span>
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
                                <input type="checkbox" aria-label="Checkbox for following text input">
                                <span class="ml-2" id="basi1-addon3">{{it}}</span>
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
                                <input type="checkbox" aria-label="Checkbox for following text input">
                                <span class="ml-2" id="basi3-addon3">{{it}}</span>
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
                        <div class="input-group m-2 " v-for="it in types" :key="it.id">
                            <div class="input-group-text bg-white">
                                <input type="checkbox" aria-label="Checkbox for following text input">
                                <span class="ml-2" id="basi5-addon3">{{it}}</span>
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
                                <input type="checkbox" aria-label="Checkbox for following text input">
                                <span class="ml-2" id="basi7-addon3">{{it}}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <full-calendar :events="events"></full-calendar>
    </div>
</template>

<script>
    import { FullCalendar } from 'vue-full-calendar';
    import 'fullcalendar/dist/fullcalendar.css';

    export default {
        name: "Home",
        data(){
            return {
                courses: ['DAA','Compilacion','BD2','IS'],
                resources: ['Proyector1','Proyector2'],
                locals: ['Aula1','Lab1'],
                types: ['Cp','Conf','JC'],
                groups: ['C312','C311','C411'],
                events: [
                {
                    title  : 'event1',
                    start  : '2019-03-16',
                },
                {
                    title  : 'dasd',
                    start  : '2019-03-16',
                    end    : '2019-03-17',
                },
                {
                    title  : 'event3',
                    start  : '2019-03-16T12:30:00',
                    allDay : false,
                },
            ]
            }
        }, components: {
            FullCalendar
        }
    }
</script>
