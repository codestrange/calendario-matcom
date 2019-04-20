<template>
    <div id="not_found">
        <div class="container">
            <!-- Outer Row -->
            <div class="row justify-content-center">
                <div class="col-xl-10 col-lg-12 col-md-9">
                    <div class="card o-hidden border-0 shadow-lg my-5">
                        <div class="card-body p-0 mt-3">
                            <!-- Nested Row within Card Body -->
                            <div class="row">
                                <div class="col-lg">
                                    <div class="text-center">
                                        <div class="error mx-auto" data-text="403">403</div>
                                        <p class="lead text-gray-800 mb-5">No tiene los permisos necesarios.</p>
                                        <router-link :to="{ name: 'homePage' }">Ir a inicio</router-link>
                                    </div>
                                </div>
                            </div>
                            <!-- Footer -->
                            <footer class="sticky-footer">
                                <div class="container my-auto">
                                    <div class="copyright text-center my-auto text-dark">
                                        <strong>Facultad de Matemática y Computación de la Universidad de La Habana &copy; 2019</strong>
                                    </div>
                                </div>
                            </footer>
                            <!-- End of Footer -->
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Forbbiden"
    }
</script>
