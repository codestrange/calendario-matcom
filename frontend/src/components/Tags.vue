<template>
    <div id="group">
        <div class="row">
            <div class="col-12">
                <div class="card mb-2 w-100 border-bottom-primary">
                    <div class="card-header py-3 bg-white">
                        <div class="row mb-3">
                            <div class="col">
                                <h5 class="m-0 font-weight-bold text-primary">Tipos</h5>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col">
                                <div class="input-group">
                                    <input type="text" v-model="text" class="form-control bg-light border-0 small" placeholder="Inserte palabra para buscar..." aria-label="Search" aria-describedby="basic-addon2">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body p-0">
                        <div class="list-group">
                            <router-link v-for="tag in filteredList" :key="tag.id" :to="{name: 'tagPage', params: {tagId: tag.id}}" class="list-group-item list-group-item-action">{{ tag.text }}</router-link>
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
                tags : [],
                text: ''
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
        },
        computed: {
            filteredList() {
                return this.tags.filter(tag => {
                    return tag.text.toString().toLowerCase().includes(this.text.toLowerCase())
                })
            }
        }
    }
</script>
