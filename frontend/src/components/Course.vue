<template>
    <div id="group">
        <div class="row">
            <div class="col-12">
                <div class="card mb-4 w-100 border-bottom-primary">
                    <div class="card-header py-3 bg-white">
                        <h5 class="m-0 font-weight-bold text-primary">Asignatura: {{ course.name }}</h5>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-6">
                <div class="card mb-1 border-bottom-primary">
                    <div class="card-header bg-white">
                        <h6 class="m-0 font-weight-bold text-primary">Eventos de la Asignatura</h6>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <button v-if="course.events.length === 0" type="button" class="list-group-item list-group-item-action" disabled>La asignatura no tiene ningún evento asignado</button>
                            <router-link v-for="event in course.events" :key="event.id" :to="{name: 'eventPage', params: {eventId: event.id}}" class="list-group-item list-group-item-action">{{ event.title }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-6">
                <div class="card mb-1 border-bottom-primary">
                    <div class="card-header bg-white">
                        <h6 class="m-0 font-weight-bold text-primary">Profesores de la Asignatura</h6>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <button v-if="course.teachers.length === 0" type="button" class="list-group-item list-group-item-action" disabled>La asignatura no tiene ningún profesor asignado</button>
                            <router-link v-for="teacher in course.teachers" :key="teacher.id" :to="{name: 'userPage', params: {userId: teacher.id}}" class="list-group-item list-group-item-action">{{ teacher.username }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Course",
        data() {
            return {
                course : {
                    id: -1,
                    name: '',
                    events: [],
                    teachers: []
                }
            };
        },
        methods: {
            loadData() {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state.course.getData(token, this.course.id).then(result => {
                    if (result === true) {
                        this.course = this.$store.state.course.data;
                    }
                    else {
                        this.$router.push({name:'notFoundPage'});
                    }
                });
            }
        },
        created() {
            this.course.id = parseInt(this.$route.params.courseId);
            if(isNaN(this.course.id)) {
                this.$router.push({name:'notFoundPage'});
            }
            this.loadData();
        }
    }
</script>
