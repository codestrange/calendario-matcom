<template>
    <div id="group">
        <div class="row">
            <div class="col-12">
                <div class="card w-100 border-bottom-primary mb-1">
                    <div class="card-header py-2 bg-white">
                        <div class="row align-items-center">
                            <div class="col">
                                <h5 class="m-0 font-weight-bold text-primary">Recursos</h5>
                            </div>
                            <div class="col">
                                <form class="form-inline justify-content-end">
                                    <input type="text" v-model="text" class="form-control bg-light border-0 small" placeholder="Buscar ..." aria-label="Search" aria-describedby="basic-addon2">
                                    <button class="btn ml-2" @click.prevent="setVal()">
                                        <i class="fas fa-sort-alpha-down"></i>
                                    </button>
                                    <button class="btn ml-2" @click.prevent="unsetVal()">
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
                            <button v-if="filterList(resources, text, 'name').length === 0" type="button" class="list-group-item list-group-item-action" disabled>No hay resultados para mostrar</button>
                            <router-link v-for="resource in filterList(resources, text, 'name')" :key="resource.id" :to="{name: 'resourcePage', params: {resourceId: resource.id}}" class="list-group-item list-group-item-action">{{ resource.name }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Resources",
        data() {
            return {
                resources : [],
                text: '',
                val: 1
            };
        },
        methods: {
            loadData() {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state.resources.getData(token).then(result => {
                    this.resources = this.$store.state.resources.data;
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
            this.loadData();
        },
    }
</script>
