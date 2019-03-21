<template>
    <div id="group">
        <div class="row">
            <div class="col-12">
                <div class="card mb-2 w-100 border-bottom-primary">
                    <div class="card-header py-3 bg-white">
                        <h5 class="m-0 font-weight-bold text-primary">Locales</h5>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <router-link v-for="local in locals" :key="local.id" :to="{name: 'localPage', params: {localId: local.id}}" class="list-group-item list-group-item-action">{{ local.name }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Locals",
        data() {
            return {
                locals : []
            };
        },
        methods: {
            loadData() {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state.locals.getData(token).then(result => {
                    this.locals = this.$store.state.locals.data;
                });
            }
        },
        created() {
            this.loadData();
        }
    }
</script>
