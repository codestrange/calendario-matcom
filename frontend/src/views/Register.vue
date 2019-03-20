<template>
    <div class="container">
        <div class="card o-hidden border-0 shadow-lg my-5">
            <div class="card-body p-0">
                <!-- Nested Row within Card Body -->
                <div class="row">
                    <div class="col-lg-5 d-none d-lg-block bg-register-image"></div>
                    <div class="col-lg-7">
                        <div class="p-5">
                            <div class="text-center">
                                <h1 class="h4 text-gray-900 mb-4">Crear una Cuenta</h1>
                            </div>
                            <form class="user">
                                <!--<div class="form-group row">-->
                                    <!--<div class="col-sm-6 mb-3 mb-sm-0">-->
                                        <!--<input type="text" class="form-control form-control-user" id="exampleFirstName" placeholder="Nombre">-->
                                    <!--</div>-->
                                    <!--<div class="col-sm-6">-->
                                        <!--<input type="text" class="form-control form-control-user" id="exampleLastName" placeholder="Apellidos">-->
                                    <!--</div>-->
                                <!--</div>-->
                                <div class="form-group">
                                    <input type="text" :class="{'form-control': true, 'form-control-user': true, 'border-danger': error.showError}" id="inputUsername" placeholder="Introduzca el nombre de usuario" v-model.trim="newUserInfo.username">
                                </div>
                                <div class="form-group">
                                    <input type="email" :class="{'form-control': true, 'form-control-user': true, 'border-danger': error.showError}" placeholder="Introduzca la dirección de correo" v-model="newUserInfo.email">
                                </div>
                                <div class="form-group row">
                                    <div class="col-sm-6 mb-3 mb-sm-0">
                                        <input type="password" :class="{'form-control': true, 'form-control-user': true, 'border-danger': error.showError}" placeholder="Introduzca la contraseña" v-model="newUserInfo.password1">
                                    </div>
                                    <div class="col-sm-6">
                                        <input type="password" :class="{'form-control': true, 'form-control-user': true, 'border-danger': error.showError}" placeholder="Repita la Contraseña" v-model="newUserInfo.password2">
                                    </div>
                                </div>
                                <div v-if="error.showError" class="form-group">
                                    <div class="card bg-danger text-white small animated--grow-in">
                                        <div class="card-body">{{error.message}}</div>
                                    </div>
                                </div>
                                <a class="btn btn-primary btn-user btn-block text-white" @click="register">
                                    Registrarse
                                </a>
                            </form>
                            <hr>
                            <!-- <div class="text-center">
                                <a class="small" href="forgot-password.html">Recuperar Contraseña</a>
                            </div> -->
                            <div class="text-center">
                                <router-link :to="{name: 'loginPage'}" class="small text-dark"><strong>¡Ya estoy registrado!</strong></router-link>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Footer -->
                <footer class="sticky-footer">
                    <div class="container">
                        <div class="copyright text-center text-dark">
                            <strong>Facultad de Matemática y Computación de la Universidad de La Habana &copy; 2019</strong>
                        </div>
                    </div>
                </footer>
                <!-- End of Footer -->
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Register",
        data() {
            return {
                newUserInfo: {
                    username: '',
                    email: '',
                    password1: '',
                    password2: ''
                },
                error: {
                    showError: false,
                    message: 'Ha ocurrido un Error.',
                }
            };
        },
        methods: {
            checkEmail() {
                // Check better if possible
                let pos = this.newUserInfo.email.indexOf('@');
                let len = this.newUserInfo.email.length - 1;
                return (pos !== -1 && pos < len && pos !== 0);
            },
            register() {
                if (this.newUserInfo.password1 === this.newUserInfo.password2) {
                    if (this.checkEmail() === false) {
                        this.error.message = 'La dirección de correo es invalida.';
                        this.error.showError = true;
                        setTimeout(() => {
                            this.error.showError = false;
                        }, 2000);
                    }
                    else if (this.newUserInfo.username === '') {
                        this.error.message = 'El nombre de usuario no puede ser vacío.';
                        this.error.showError = true;
                        setTimeout(() => {
                            this.error.showError = false;
                        }, 2000);
                    }
                    else {
                        console.log('Handling the registration.');
                        this.$store.state.profile.register(this.newUserInfo.username, this.newUserInfo.email, this.newUserInfo.password1).
                        then(result => {
                            if (result.hasOwnProperty('error') === false) {
                                this.$router.push({name: 'loginPage'});
                            }
                            else {
                                console.log(result.error + ':' + result.message);
                                this.error.message = result.message;
                                this.error.showError = true;
                                setTimeout(() => {
                                    this.error.showError = false;
                                }, 2000);
                            }
                        });
                    }
                }
                else {
                    this.error.message = 'Las contraseñas no coinciden.';
                    this.error.showError = true;
                    setTimeout(() => {
                        this.error.showError = false;
                    }, 2000);
                }
            }
        }
    }
</script>
