<template>
    <div id="group">
        <div class="row">
            <div class="col-12">
                <div class="card w-100 border-bottom-primary mb-1">
                    <div class="card-header py-2 bg-white">
                        <div class="row align-items-center">
                            <div class="col">
                                <h5 class="m-0 font-weight-bold text-primary">Asignaturas</h5>
                            </div>
                            <div class="col">
                                <form class="form-inline justify-content-end">
                                    <input type="text" v-model="text" class="form-control bg-light border-0 small" placeholder="Buscar ..." aria-label="Search" aria-describedby="basic-addon2">
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
                            <button v-if="filterList(courses, text, 'name').length === 0" type="button" class="list-group-item list-group-item-action" disabled>No hay resultados para mostrar</button>
                            <router-link v-for="course in filterList(courses, text, 'name')" :key="course.id" :to="{name: 'coursePage', params: {courseId: course.id}}" class="list-group-item list-group-item-action">{{ course.name }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Courses",
        data() {
            return {
                courses : [],
                text: ''
            };
        },
        methods: {
            loadData() {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state.courses.getData(token).then(result => {
                    this.courses = this.$store.state.courses.data;
                });
            },
            filterList(list, box, prop){
                return list.filter(elem => {
                    return elem[prop].toString().toLowerCase().includes(box.toLowerCase())
                })
            }
        },
        created() {
            this.loadData();
        }
    }
</script>
