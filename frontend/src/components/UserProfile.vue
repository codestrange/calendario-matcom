<template>
    <div id="user-profile" class="row">
        <div class="col-lg-5">
            <img class="img-profile rounded-circle" :src="user_img">
        </div>
        <div class="col-lg-7">
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
                <hr>
                <div class="text-center">
                    <a class="small" href="forgot-password.html">Forgot Password?</a>
                </div>
                <div class="text-center">
                    <a class="small" href="login.html">Already have an account? Login!</a>
                </div>
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

