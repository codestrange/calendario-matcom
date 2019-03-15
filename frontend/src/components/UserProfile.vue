<template>
    <div id="user-profile" class="row align-items-center justify-content-center">
        <div class="col-lg-3 offset-lg-1">
            <img class="img-profile ml-3 rounded-circle mb-3" :src="user_img">
            <button class="btn btn-danger btn-user btn-block">Confirmar Cambios</button>
            <hr>
            <div class="form-group">
                <textarea type="text" class="form-control form-control-user" id="username" v-model="username"></textarea>
            </div>
        </div>
        <div class="col-lg-8">
            <div class="p-5">
                <div class="text-center">
                    <h1 class="h2 text-gray-900 mb-4">Perfil</h1>
                </div>
                <form class="user">
                    <div class="form-group">
                        <input type="text" class="form-control form-control-user" id="username" v-model="username">
                    </div>
                    <div class="form-group">
                        <input type="text" class="form-control form-control-user" id="firstName" v-model="name">
                    </div>
                    <div class="form-group">
                        <input type="text" class="form-control form-control-user" id="lastName" v-model="lastname">
                    </div>
                    <div class="form-group">
                        <input type="email" class="form-control form-control-user" id="email" v-model="email">
                    </div>
                    <div class="form-group row">
                        <div class="col-sm-6 mb-3 mb-sm-0">
                            <input type="password" class="form-control form-control-user" id="inputNewPassword" placeholder="Nueva Contraseña" v-model="new_password1">
                        </div>
                        <div class="col-sm-6">
                            <input type="password" class="form-control form-control-user" id="repeatNewPassword" placeholder="Repita la Contraseña" v-model="new_password2">
                        </div>
                    </div>
                    <button class="btn btn-danger btn-user btn-block">Confirmar Cambios</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "UserProfile",
        data() {
            return {
                username: '',
                name: 'John',
                lastname: 'Johnson',
                email: '',
                user_img: './img/default_user_image.jpeg',
                new_password1: '',
                new_password2: '',
                password: ''
            };
        },
        created() {
            this.$store.state.user.getUserData().then(() => {
                this.username = this.$store.state.user.user_data.username;
                this.email = this.$store.state.user.user_data.email;
            });
        }
    }
</script>

