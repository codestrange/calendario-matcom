<template>
    <div id="login">

        <div class="container">

            <!-- Outer Row -->
            <div class="row justify-content-center">

                <div class="col-xl-10 col-lg-12 col-md-9">

                    <div class="card o-hidden border-0 shadow-lg my-5">
                        <div class="card-body p-0">
                            <!-- Nested Row within Card Body -->
                            <div class="row">
                                <div class="col-lg-6 d-none d-lg-block bg-login-image"></div>
                                <div class="col-lg-6">
                                    <div class="p-5">
                                        <div class="text-center">
                                            <h1 class="h5 text-gray-900 mb-4">Bienvenido a <strong>Calendario MatCom</strong></h1>
                                        </div>
                                        <form class="user">
                                            <div class="form-group">
                                                <input type="email" class="form-control form-control-user" id="exampleInputEmail" aria-describedby="emailHelp" placeholder="Introduzca su correo electrónico">
                                            </div>
                                            <div class="form-group">
                                                <input type="password" class="form-control form-control-user" id="exampleInputPassword" placeholder="Introduzca su contraseña">
                                            </div>
                                            <div class="form-group">
                                                <div class="custom-control custom-checkbox small">
                                                    <input type="checkbox" class="custom-control-input" id="customCheck">
                                                    <label class="custom-control-label" for="customCheck">Recuerdame</label>
                                                </div>
                                            </div>
                                            <a href="index.html" class="btn btn-primary btn-user btn-block">
                                                Iniciar Sesión
                                            </a>
                                        </form>
                                        <hr>
                                        <div class="text-center">
                                            <a class="small" href="forgot-password.html">Recuperar Contraseña</a>
                                        </div>
                                        <div class="text-center">
                                            <a class="small" href="register.html">Registrarse</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>

            </div>

            <!-- Footer -->
            <footer class="sticky-footer">
                <div class="container my-auto">
                    <div class="copyright text-center my-auto text-white">
                        <span>Facultad de Matemática y Computación de la Universidad de La Habana &copy; 2019</span>
                    </div>
                </div>
            </footer>
            <!-- End of Footer -->

        </div>

    </div>
</template>

<script>
    export default {
        name: "Login",
    }
</script>

<style scoped>

</style>