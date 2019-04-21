<template>
    <div id="group">
        <div class="row">
            <div class="col-12">
                <div class="card w-100 border-bottom-primary mb-2">
                    <div class="card-header py-2 bg-white">
                        <div class="row align-items-center">
                            <div class="col">
                                <h5 class="m-0 font-weight-bold text-primary">Notificaciones</h5>
                            </div>
                        </div>
                    </div>
                </div>
                <div v-for="(noti, index) in notifications" :key="noti.id" class="card mb-2" :class="noti.seened ? '' : 'text-white bg-primary'">
                    <div class="card-body">
                        <h5 class="card-title"><strong>{{ noti.title }}</strong></h5>
                        <h6 class="card-subtitle text-muted" v-if="noti.groups.length > 0">{{ noti.groups }}</h6>
                        <p class="card-text">{{ noti.body }}</p>
                        <a href="" class="card-link stretched-link" :class="noti.seened ? 'text-muted' : 'text-white'" @click.prevent="seen(noti.id, index)">Fecha: {{ render_date(noti.date) }}</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import { renderPresentation } from '../utils/render_date';

    export default {
        name: "Notifications",
        data() {
            return {
                notifications: []
            };
        },
        methods: {
            render_date(start) {
                return renderPresentation(start, null);
            },
            seen(id, index) {
                let token = this.$store.state.profile.data.token;
                this.$store.state.notifications.setSeened(token, id).then(status => {
                    if(status)
                        this.notifications[index].seened = true;
                });
                this.$store.state.notifications.update();
            },
            loadData() {
                let token = this.$store.state.profile.data.token;
                this.$store.state.notifications.getData(token).then(() => {
                    this.notifications = this.$store.state.notifications.data;
                });
            }
        },
        created() {
            this.$store.state.profile.getData().then(() => {
                this.username = this.$store.state.profile.data.username;
            });
            this.$store.state.notifications.addUpdate('notifications', this.loadData);
            this.$store.state.notifications.update();
        }
    }
</script>
