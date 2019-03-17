<template>
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="eventSelectedModalLabel">{{ eventSelected.title }}</h5>
                <button class="close" type="button" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">x</span>
                </button>
            </div>
            <div class="modal-body">
                <div class="mb-1" v-if="eventSelected.description !== ''"><strong>Descripción:</strong> {{ eventSelected.description }}</div>
                <div class="mb-1"><strong>Horario:</strong> {{ render_date(eventSelected.start, eventSelected.end) }}</div>
                <div class="mb-1" v-if="eventSelected.hasOwnProperty('courses') && eventSelected.courses.length !== 0"><strong>Asignaturas:</strong>
                    <span v-for="(course, index) in eventSelected.courses" :key="course.id">
                                {{ course.name }}<span v-if="index !== eventSelected.courses.length - 1">, </span>
                            </span>
                </div>
                <div class="mb-1" v-if="eventSelected.hasOwnProperty('groups') && eventSelected.groups.length !== 0"><strong>Grupos:</strong>
                    <span v-for="(group, index) in eventSelected.groups" :key="group.id">
                                {{ group.name }}<span v-if="index !== eventSelected.groups.length - 1">, </span>
                            </span>
                </div>
                <div class="mb-1" v-if="eventSelected.hasOwnProperty('locals') && eventSelected.locals.length !== 0"><strong>Locales:</strong>
                    <span v-for="(local, index) in eventSelected.locals" :key="local.id">
                                {{ local.name }}<span v-if="index !== eventSelected.locals.length - 1">, </span>
                            </span>
                </div>
                <div class="mb-1" v-if="eventSelected.hasOwnProperty('resources') && eventSelected.resources.length !== 0"><strong>Recursos:</strong>
                    <span v-for="(resource, index) in eventSelected.resources" :key="resource.id">
                                {{ resource.name }}<span v-if="index !== eventSelected.resources.length - 1">, </span>
                            </span>
                </div>
                <div class="mb-1" v-if="eventSelected.hasOwnProperty('tags') && eventSelected.tags.length !== 0"><strong>Tipos:</strong>
                    <span v-for="(tag, index) in eventSelected.tags" :key="tag.id">
                                {{ tag.text }}<span v-if="index !== eventSelected.tags.length - 1">, </span>
                            </span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import { renderPresentation } from '../utils/render_date';

    export default {
        name: "EventInfoShower",
        props: {
            eventSelected: {}
        },
        methods: {
            render_date(start, end) {
                return renderPresentation(start, end);
            }
        }
    }
</script>

<style scoped>

</style>