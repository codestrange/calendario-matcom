<template>
    <div id="home">
        <div class="row">
            <div class="col">
                <div class="dropdown mb-4">
                    <button class="btn btn-light dropdown-toggle" type="button" id="asignaturas_drop_down" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
                        Asignaturas
                    </button>
                    <div class="dropdown-menu animated--fade-in " aria-labelledby="dropdownMenuButton" x-placement="bottom-start" style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 38px, 0px);">
                        <div class="input-group m-2 " v-for="it in courses">
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
                        <div class="input-group m-2 " v-for="it in resources">
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
                        <div class="input-group m-2 " v-for="it in locals">
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
                        <div class="input-group m-2 " v-for="it in types">
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
                        <div class="input-group m-2 " v-for="it in groups">
                            <div class="input-group-text bg-white">
                                <input type="checkbox" aria-label="Checkbox for following text input">
                                <span class="ml-2" id="basi7-addon3">{{it}}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Home",
        data(){
            return {
                courses: ['DAA','Compilacion','BD2','IS'],
                resources: ['Proyector1','Proyector2'],
                locals: ['Aula1','Lab1'],
                types: ['Cp','Conf','JC'],
                groups: ['C312','C311','C411']
            }
        }
    }
</script>
