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
                <div class="card mb-1 bg-white border-bottom-primary">
                    <a href="#collapseCardCoursesEvents" class="d-block card-header py-3" data-toggle="collapse" role="button" aria-expanded="false" aria-controls="collapseCardCoursesEvents">
                        <h6 class="m-0 font-weight-bold text-primary">Eventos de la Asignatura</h6>
                    </a>
                    <div class="collapse hide" id="collapseCardCoursesEvents" style="">
                        <div class="card-body p-2">
                            <div class="row justify-content-center">
                                <form class="form-inline">
                                    <input type="text" v-model="course_events" class="form-control bg-light border-0 small" placeholder="Buscar ..." aria-label="Search" aria-describedby="basic-addon2">
                                    <button class="btn ml-2">
                                        <i class="fas fa-sort-alpha-down"></i>
                                    </button>
                                    <button class="btn ml-2">
                                        <i class="fas fa-sort-alpha-up"></i>
                                    </button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <button v-if="course.events.length === 0" type="button" class="list-group-item list-group-item-action" disabled>La asignatura no tiene ningún evento asignado</button>
                            <button v-else-if="filterList(course.events, course_events, 'title').length === 0" type="button" class="list-group-item list-group-item-action" disabled>No hay resultados para mostrar</button>
                            <router-link v-for="event in filterList(course.events, course_events, 'title')" :key="event.id" :to="{name: 'eventPage', params: {eventId: event.id}}" class="list-group-item list-group-item-action">{{ event.title }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-6">
                <div class="card mb-1 bg-white border-bottom-primary">
                    <a href="#collapseCardCoursesTeachers" class="d-block card-header py-3" data-toggle="collapse" role="button" aria-expanded="false" aria-controls="collapseCardCoursesTeachers">
                        <h6 class="m-0 font-weight-bold text-primary">Profesores de la Asignatura</h6>
                    </a>
                    <div class="collapse hide" id="collapseCardCoursesTeachers" style="">
                        <div class="card-body p-2">
                            <div class="row justify-content-center">
                                <form class="form-inline">
                                    <input type="text" v-model="course_teachers" class="form-control bg-light border-0 small" placeholder="Buscar ..." aria-label="Search" aria-describedby="basic-addon2">
                                    <button class="btn ml-2">
                                        <i class="fas fa-sort-alpha-down"></i>
                                    </button>
                                    <button class="btn ml-2">
                                        <i class="fas fa-sort-alpha-up"></i>
                                    </button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <button v-if="course.teachers.length === 0" type="button" class="list-group-item list-group-item-action" disabled>La asignatura no tiene ningún profesor asignado</button>
                            <button v-else-if="filterList(course.teachers, course_teachers, 'username').length === 0" type="button" class="list-group-item list-group-item-action" disabled>No hay resultados para mostrar</button>
                            <router-link v-for="teacher in filterList(course.teachers, course_teachers, 'username')" :key="teacher.id" :to="{name: 'userPage', params: {userId: teacher.id}}" class="list-group-item list-group-item-action">{{ teacher.username }}</router-link>
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
                },
                course_teachers: '',
                course_events: ''
            };
        },
        methods: {
            loadData() {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state.course.getData(token, this.course.id).then(result => {
                    this.course = this.$store.state.course.data;
                });
            },
            filterList(list, box, prop){
                return list.filter(elem => {
                    return elem[prop].toString().toLowerCase().includes(box.toLowerCase())
                })
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
