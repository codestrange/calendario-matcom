<template>
    <div id="user-profile" class="row align-items-center justify-content-center">
        <div class="col-lg-3 offset-lg-1">
            <img class="img-profile ml-3 rounded-circle mb-5" :src="user.user_img">
            <button class="btn btn-primary btn-user btn-block" disabled>Cambiar</button>
        </div>
        <div class="col-lg-8">
            <div class="p-5">
                    <div class="form-group">
                        <input type="text" class="form-control form-control-user" id="username" placeholder="Usuario" v-model="user.username" :disabled="!is_edit">
                    </div>
                    <div class="form-group">
                        <input type="text" class="form-control form-control-user" id="firstName" placeholder="Nombre" v-model="user.firstname" :disabled="!is_edit">
                    </div>
                    <div class="form-group">
                        <input type="text" class="form-control form-control-user" id="lastName" placeholder="Apellidos" v-model="user.lastname" :disabled="!is_edit">
                    </div>
                    <div class="form-group">
                        <input type="email" class="form-control form-control-user" id="email" placeholder="Correo" v-model="user.email" :disabled="!is_edit">
                    </div>
                    <div class="form-group row">
                        <div class="col-sm-6 mb-3 mb-sm-0">
                            <input type="password" class="form-control form-control-user" id="inputNewPassword" placeholder="Contraseña Nueva" v-model="new_password1" :disabled="!is_edit">
                        </div>
                        <div class="col-sm-6">
                            <input type="password" class="form-control form-control-user" id="repeatNewPassword" placeholder="Repita la Contraseña" v-model="new_password2" :disabled="!is_edit">
                        </div>
                    </div>
                <button class="btn btn-primary btn-user btn-block" @click="toogleEdit">{{ text_button }}</button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "UserProfile",
        data() {
            return {
                user : {
                    username: '',
                    firstname: '',
                    lastname: '',
                    email: '',
                    user_img: './img/default_user_image.jpeg',
                    password: ''
                },
                new_password1: '',
                new_password2: '',
                is_edit: false,
                text_button: "Editar"
            };
        },
        methods: {
            toogleEdit: function() {
                if (this.is_edit) {
                    // Hacer request
                }
                this.is_edit = !this.is_edit;
                if (this.is_edit) {
                    this.text_button = "Guardar";
                } else {
                    this.text_button = "Editar";
                }
            }
        },
        created() {
            this.$store.state.profile.getData().then(() => {
                this.user.username = this.$store.state.profile.data.username;
                this.user.email = this.$store.state.profile.data.email;
            });
        }
    }
</script>

