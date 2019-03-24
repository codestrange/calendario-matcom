<template>
    <div id="group">
        <div class="row">
            <div class="col-12">
                <div class="card mb-4 w-100 border-bottom-primary">
                    <div class="card-header py-3 bg-white">
                        <h5 class="m-0 font-weight-bold text-primary">Usuario: {{ user.username }}</h5>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-12">
                <div class="card mb-1 bg-white border-bottom-primary">
                    <a href="#collapseCardUsersGroups" class="d-block card-header py-3" data-toggle="collapse" role="button" aria-expanded="false" aria-controls="collapseCardUsersGroups">
                        <h6 class="m-0 font-weight-bold text-primary">Grupos del Usuario</h6>
                    </a>
                    <div class="collapse hide" id="collapseCardUsersGroups" style="">
                        <div class="card-body p-2">
                            <div class="row justify-content-center">
                                <div class="col-10">
                                    <input type="text" v-model="user_groups" class="form-control bg-light border-0 small" placeholder="Buscar ..." aria-label="Search" aria-describedby="basic-addon2">
                                </div>
                                <div class="col-lg-2">
                                    <button class="btn ml-4" @click.prevent="setVal()">
                                        <i class="fas fa-sort-alpha-down"></i>
                                    </button>
                                    <button class="btn ml-4" @click.prevent="unsetVal()">
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
                            <button v-if="user.groups.length === 0" type="button" class="list-group-item list-group-item-action" disabled>El usuario no tiene ningún grupo asignado</button>
                            <button v-else-if="filterList(user.groups, user_groups, 'name').length === 0" type="button" class="list-group-item list-group-item-action" disabled>No hay resultados para mostrar</button>
                            <router-link v-for="group in filterList(user.groups, user_groups, 'name')" :key="group.id" :to="{name: 'groupPage', params: {groupId: group.id}}" class="list-group-item list-group-item-action">{{ group.name }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Group",
        data() {
            return {
                user : {
                    id: -1,
                    username: '',
                    groups: []
                },
                user_groups: '',
                val: 1
            };
        },
        methods: {
            loadData() {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state.user.getData(token, this.user.id).then(result => {
                    this.user = this.$store.state.user.data;
                });
            },
            filterList(list, box, prop){
                let tmp = list.sort(this.comparer(prop, this.val));
                return tmp.filter(elem => {
                    return elem[prop].toString().toLowerCase().includes(box.toLowerCase());
                });
            },
            setVal(){
                this.val = 1;
            },
            unsetVal(){
                this.val = -1;
            },
            comparer(prop, val){
                return function (a,b) {
                    if (a[prop] > b[prop]) {
                        return 1 * val;
                    } else if (a[prop] < b[prop]) {
                        return -1 * val;
                    } else {
                        return 0;
                    }
                }
            }
        },
        created() {
            this.user.id = parseInt(this.$route.params.userId);
            if(isNaN(this.user.id)) {
                this.$router.push({name:'notFoundPage'});
            }
            this.loadData();
        }
    }
</script>
