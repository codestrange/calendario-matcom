<template>
    <div id="group">
        <div class="row">
            <div class="col-12">
                <div class="card mb-2 w-100 border-bottom-primary">
                    <div class="card-header py-3 bg-white">
                        <h5 class="m-0 font-weight-bold text-primary">Recursos</h5>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <router-link v-for="resource in resources" :key="resource.id" :to="{name: 'resourcePage', params: {resourceId: resource.id}}" class="list-group-item list-group-item-action">{{ resource.name }}</router-link>
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
                resources : []
            };
        },
        methods: {
            loadData() {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state.resources.getData(token).then(result => {
                    this.resources = this.$store.state.resources.data;
                });
            }
        },
        created() {
            this.loadData();
        }
    }
</script>
