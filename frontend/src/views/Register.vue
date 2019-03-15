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
                                    <input type="text" class="form-control form-control-user" id="InputUsername" placeholder="Introduzca el nombre de usuario" v-model.trim="username">
                                </div>
                                <div class="form-group">
                                    <input type="email" class="form-control form-control-user" id="InputEmail" placeholder="Introduzca la dirección de correo" v-model="email">
                                </div>
                                <div class="form-group row">
                                    <div class="col-sm-6 mb-3 mb-sm-0">
                                        <input type="password" class="form-control form-control-user" id="exampleInputPassword" placeholder="Introduzca la contraseña" v-model="password1">
                                    </div>
                                    <div class="col-sm-6">
                                        <input type="password" class="form-control form-control-user" id="exampleRepeatPassword" placeholder="Repita la Contraseña" v-model="password2">
                                    </div>
                                </div>
                                <a class="btn btn-primary btn-user btn-block text-white" @click="registerUser">
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
                username: '',
                email: '',
                password1: '',
                password2: ''
            };
        },
        methods: {
            registerUser() {
                if (this.password1 === this.password2) {
                    //I should check if email is correctly writed
                    this.$store.state.user.createUser(this.username, this.email, this.password1).then(result => {
                        if (result === true) {
                            this.$router.push({name: 'loginPage'});
                        }
                    });
                }
                else {
                    //Show that the two passwords didnt match
                    alert('Passwords are different.');
                }
            }
        }
    }
</script>
