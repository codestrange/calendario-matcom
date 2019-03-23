<template>
    <div id="group">
        <div class="row">
            <div class="col-12">
                <div class="card mb-2 w-100 border-bottom-primary">
                    <div class="card-header py-2 bg-white">
                        <div class="row align-items-center">
                            <div class="col-2">
                                <h5 class="m-0 font-weight-bold text-primary">Asignaturas</h5>
                            </div>
                            <div class="col-9">
                                <input type="text" v-model="text" class="form-control bg-light border-0 small" placeholder="Buscar ..." aria-label="Search" aria-describedby="basic-addon2">
                            </div>
                            <div class="col-1">
                                <div class="row justify-content-end">
                                    <button class="btn btn-primary btn-sm btn-circle ml-3">
                                        <i class="fas fa-sort-alpha-down"></i>
                                    </button>
                                    <button class="btn btn-primary btn-sm btn-circle ml-3">
                                        <i class="fas fa-sort-alpha-up"></i>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <router-link v-for="course in filteredList" :key="course.id" :to="{name: 'coursePage', params: {courseId: course.id}}" class="list-group-item list-group-item-action">{{ course.name }}</router-link>
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
            }
        },
        created() {
            this.loadData();
        },
        computed: {
            filteredList() {
                return this.courses.filter(course => {
                    return course.name.toString().toLowerCase().includes(this.text.toLowerCase())
                })
            }
        }
    }
</script>
