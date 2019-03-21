<template>
    <div id="group">
        <div class="row">
            <div class="col-12">
                <div class="card mb-2 w-100 border-bottom-primary">
                    <div class="card-header py-3 bg-white">
                        <h5 class="m-0 font-weight-bold text-primary">Evento: {{ event.title }}</h5>
                    </div>
                </div>
                <div class="card mb-2 w-100 border-bottom-grey">
                    <div class="card-header py-2 bg-white">
                        {{ render_date(event.start, event.end) }}
                    </div>
                </div>
                
            </div>
        </div>
        <div class="row">
            <div class="col-6">
                <div class="card mb-1 border-bottom-primary">
                    <div class="card-header bg-white">
                        <h6 class="m-0 font-weight-bold text-primary">Grupos del Evento</h6>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <button v-if="event.groups.length === 0" type="button" class="list-group-item list-group-item-action" disabled>El evento no tiene ningún grupo asignado</button>
                            <router-link v-for="group in event.groups" :key="group.id" :to="{name: 'groupPage', params: {groupId: group.id}}" class="list-group-item list-group-item-action">{{ group.name }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-6">
                <div class="card mb-1 border-bottom-primary">
                    <div class="card-header bg-white">
                        <h6 class="m-0 font-weight-bold text-primary">Locales del Evento</h6>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <button v-if="event.locals.length === 0" type="button" class="list-group-item list-group-item-action" disabled>El evento no tiene ningún local asignado</button>
                            <router-link v-for="local in event.locals" :key="local.id" :to="{name: 'localPage', params: {localId: local.id}}" class="list-group-item list-group-item-action">{{ local.name }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row mt-2">
            <div class="col-4">
                <div class="card mb-1 border-bottom-primary">
                    <div class="card-header bg-white">
                        <h6 class="m-0 font-weight-bold text-primary">Asignaturas del Evento</h6>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <button v-if="event.courses.length === 0" type="button" class="list-group-item list-group-item-action" disabled>El evento no tiene ningún asignatura asignado</button>
                            <router-link v-for="course in event.courses" :key="course.id" :to="{name: 'coursePage', params: {courseId: course.id}}" class="list-group-item list-group-item-action">{{ course.name }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-4">
                <div class="card mb-1 border-bottom-primary">
                    <div class="card-header bg-white">
                        <h6 class="m-0 font-weight-bold text-primary">Recursos del Evento</h6>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <button v-if="event.resources.length === 0" type="button" class="list-group-item list-group-item-action" disabled>El evento no tiene ningún recurso asignado</button>
                            <router-link v-for="resource in event.resources" :key="resource.id" :to="{name: 'resourcePage', params: {resourceId: resource.id}}" class="list-group-item list-group-item-action">{{ resource.name }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-4">
                <div class="card mb-1 border-bottom-primary">
                    <div class="card-header bg-white">
                        <h6 class="m-0 font-weight-bold text-primary">Tipos del Evento</h6>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <button v-if="event.tags.length === 0" type="button" class="list-group-item list-group-item-action" disabled>El evento no tiene ningún tipo asignado</button>
                            <router-link v-for="tag in event.tags" :key="tag.id" :to="{name: 'tagPage', params: {tagId: tag.id}}" class="list-group-item list-group-item-action">{{ tag.text }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import { renderPresentation } from '../utils/render_date';

    export default {
        name: "Group",
        data() {
            return {
                event : {
                    id: -1,
                    title: '',
                    courses: [],
                    groups: [],
                    locals: [],
                    resources: [],
                    tags: []
                }
            };
        },
        methods: {
            loadEvent() {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state.event.getData(token, this.event.id).then(result => {
                    this.event = this.$store.state.event.data;
                });
            },
            render_date(start, end) {
                return renderPresentation(start, end);
            }
        },
        created() {
            this.event.id = parseInt(this.$route.params.eventId);
            if(isNaN(this.event.id)) {
                this.$router.push({name:'notFoundPage'});
            }
            this.loadEvent();
        }
    }
</script>
