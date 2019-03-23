<template>
    <div id="group">
        <div class="row">
            <div class="col-12">
                <div class="card mb-2 w-100 border-bottom-primary">
                    <div class="card-header py-3 bg-white">
                        <div class="row mb-3">
                            <div class="col">
                                <h5 class="m-0 font-weight-bold text-primary">Grupos</h5>
                            </div>
                        </div>
                        <div class="row">
                            <class class="col">
                                <div class="input-group">
                                    <input type="text" v-model="text" class="form-control bg-light border-0 small" placeholder="Inserte palabra para buscar..." aria-label="Search" aria-describedby="basic-addon2">
                                </div>
                            </class>
                        </div>

                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <router-link v-for="group in filteredList" :key="group.id" :to="{name: 'groupPage', params: {groupId: group.id}}" class="list-group-item list-group-item-action">{{ group.name }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Groups",
        data() {
            return {
                groups : [],
                text: ''
            };
        },
        methods: {
            loadData() {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state.groups.getData(token).then(result => {
                    if (result === true) {
                        this.groups = this.$store.state.groups.data;
                        this.groups = this.groups.sort((a,b) => b.name - a.name );
                    }
                    else {
                        this.$router.push({name:'notFoundPage'});
                    }
                });
            }
        },
        created() {
            this.loadData();
        },
        computed: {
            filteredList() {
                return this.groups.filter(group => {
                    return group.name.toString().toLowerCase().includes(this.text.toLowerCase())
                })
            }
        }
    }
</script>
