<template>
    <div id="group">
        <div class="row">
            <div class="col-12">
                <div class="card mb-2 w-100 border-bottom-primary">
                    <div class="card-header py-3 bg-white">
                        <h5 class="m-0 font-weight-bold text-primary">Tipos</h5>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <router-link v-for="tag in tags" :key="tag.id" :to="{name: 'tagPage', params: {tagId: tag.id}}" class="list-group-item list-group-item-action">{{ tag.text }}</router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Tags",
        data() {
            return {
                tags : []
            };
        },
        methods: {
            loadData() {
                this.$store.state.profile.loadMinData();
                let token = this.$store.state.profile.data.token;
                this.$store.state.tags.getData(token).then(result => {
                    this.tags = this.$store.state.tags.data;
                });
            }
        },
        created() {
            this.loadData();
        }
    }
</script>
