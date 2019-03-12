<template>
    <div id="home">
        <div id="wrapper">
            <!-- Sidebar -->
            <ul class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion" id="accordionSidebar">
                <!-- Sidebar - Brand -->
                <a class="sidebar-brand d-flex align-items-center justify-content-center" href="index.html">
                    <div class="sidebar-brand-icon rotate-n-15">
                        <i class="fas fa-table"></i>
                    </div>
                    <!--<div class="sidebar-brand-text mx-3"></div>-->
                </a>
                <!-- Divider -->
                <hr class="sidebar-divider my-0">
                <!-- Nav Item - Inicio -->
                <li class="nav-item">
                    <a class="nav-link" href="blank.html">
                        <i class="fas fa-fw fa-home"></i>
                        <span>Inicio</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="blank.html">
                        <i class="fas fa-fw fa-table"></i>
                        <span>Mi Calendario</span></a>
                </li>
                <!-- Divider -->
                <hr class="sidebar-divider">
                <!-- Heading -->
                <!--<div class="sidebar-heading">-->
                <!--Addons-->
                <!--</div>-->
                <!-- Nav Item - Pages Collapse Menu -->
                <li class="nav-item">
                    <a class="nav-link" href="#" data-toggle="collapse" data-target="#collapsePages" aria-expanded="true"
                       aria-controls="collapsePages">
                        <i class="fas fa-fw fa-folder"></i>
                        <span>Enlaces Externos</span>
                    </a>
                    <div id="collapsePages" class="collapse" aria-labelledby="headingPages"
                         data-parent="#accordionSidebar">
                        <div class="bg-white py-2 collapse-inner rounded">
                            <h6 class="collapse-header">Sitios Matcom:</h6>
                            <a class="collapse-item" href="http://foros.matcom.uh.cu">Foros Matcom</a>
                            <a class="collapse-item" href="http://correo.estudiantes.matcom.uh.cu">Correo</a>
                            <div class="collapse-divider"></div>
                            <h6 class="collapse-header">Sitios UH:</h6>
                            <a class="collapse-item" href="http://www.uh.cu">UH</a>
                        </div>
                    </div>
                </li>
                <!-- Divider -->
                <hr class="sidebar-divider d-none d-md-block">
                <!-- Sidebar Toggler (Sidebar) -->
                <div class="text-center d-none d-md-inline">
                    <button class="rounded-circle border-0" id="sidebarToggle"></button>
                </div>
            </ul>
            <!-- End of Sidebar -->
            <div id="content-wrapper" class="d-flex flex-column">
                <!-- Main Content -->
                <div id="content">
                    <!-- Topbar -->
                    <nav class="navbar navbar-expand navbar-light bg-white topbar mb-4 static-top shadow">
                        <!-- Sidebar Toggle (Topbar) -->
                        <button id="sidebarToggleTop" class="btn btn-link d-md-none rounded-circle mr-3">
                            <i class="fa fa-bars"></i>
                        </button>
                        <h1 class="h2 mb-0 text-dark">
                            Calendario Matcom
                        </h1>
                        <!-- Topbar Navbar -->
                        <ul class="navbar-nav ml-auto">
                            <!-- Nav Item - Alerts -->
                            <li class="nav-item dropdown no-arrow mx-1">
                                <a class="nav-link dropdown-toggle" href="#" id="alertsDropdown" role="button"
                                   data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                    <i class="fas fa-bell fa-fw"></i>
                                    <!-- Counter - Alerts -->
                                    <span class="badge badge-danger badge-counter">2</span>
                                </a>
                                <!-- Dropdown - Alerts -->
                                <div class="dropdown-list dropdown-menu dropdown-menu-right shadow animated--grow-in"
                                     aria-labelledby="alertsDropdown">
                                    <h6 class="dropdown-header">
                                        Notificaciones
                                    </h6>
                                    <a class="dropdown-item d-flex align-items-center" href="#">
                                        <div class="mr-3">
                                            <div class="icon-circle bg-primary">
                                                <i class="fas fa-file-alt text-white"></i>
                                            </div>
                                        </div>
                                        <div>
                                            <div class="small text-gray-500">12 de diciembre del 2019</div>
                                            <span class="font-weight-bold">Un nuevo reporte esta listo para ser descargado</span>
                                        </div>
                                    </a>
                                    <a class="dropdown-item d-flex align-items-center" href="#">
                                        <div class="mr-3">
                                            <div class="icon-circle bg-success">
                                                <i class="fas fa-donate text-white"></i>
                                            </div>
                                        </div>
                                        <div>
                                            <div class="small text-gray-500">7 de diciembre del 2019</div>
                                            290.29 dolares han sido depositados en su cuenta.
                                        </div>
                                    </a>
                                    <a class="dropdown-item text-center small text-gray-500" href="#">Ver todas las notificaciones</a>
                                </div>
                            </li>
                            <div class="topbar-divider d-none d-sm-block"></div>
                            <!-- Nav Item - User Information -->
                            <li class="nav-item dropdown no-arrow">
                                <a class="nav-link dropdown-toggle" href="#" id="userDropdown" role="button"
                                   data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                    <span class="mr-2 d-none d-lg-inline text-gray-600 small">Usuario</span>
                                    <img class="img-profile rounded-circle" src="img/uh_front.jpg">
                                </a>
                                <!-- Dropdown - User Information -->
                                <div class="dropdown-menu dropdown-menu-right shadow animated--grow-in"
                                     aria-labelledby="userDropdown">
                                    <a class="dropdown-item" href="#">
                                        <i class="fas fa-user fa-sm fa-fw mr-2 text-gray-400"></i>
                                        Perfil
                                    </a>
                                    <a class="dropdown-item" href="#">
                                        <i class="fas fa-cogs fa-sm fa-fw mr-2 text-gray-400"></i>
                                        Configuración
                                    </a>
                                    <div class="dropdown-divider"></div>
                                    <a class="dropdown-item" href="#" data-toggle="modal" data-target="#logoutModal">
                                        <i class="fas fa-sign-out-alt fa-sm fa-fw mr-2 text-gray-400"></i>
                                        Cerrar Sesión
                                    </a>
                                </div>
                            </li>
                        </ul>
                    </nav>
                    <!-- End of Topbar -->
                    <!-- Begin Page Content -->
                    <div class="container-fluid">
                        <!-- Page Heading -->
                        <h1 class="h3 mb-4 text-gray-800">Página en Blanco</h1>
                    </div>
                    <!-- /.container-fluid -->
                </div>
                <!-- End of Main Content -->
                <!-- Footer -->
                <footer class="sticky-footer bg-white">
                    <div class="container my-auto">
                        <div class="copyright text-center my-auto">
                            <span>Facultad de Matemática y Computación de la Universidad de La Habana &copy; 2019</span>
                        </div>
                    </div>
                </footer>
                <!-- End of Footer -->
            </div>
            <!-- End of Content Wrapper -->
        </div>
        <!-- Scroll to Top Button-->
        <a class="scroll-to-top rounded" href="#page-top">
            <i class="fas fa-angle-up"></i>
        </a>
        <!-- Logout Modal-->
        <div class="modal fade" id="logoutModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
             aria-hidden="true">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">¿Está seguro que desea cerrar sesión?</h5>
                        <button class="close" type="button" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">x</span>
                        </button>
                    </div>
                    <div class="modal-footer">
                        <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancelar</button>
                        <button class="btn btn-primary" data-dismiss="modal" @click="logoutUser">Cerrar Sesión</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Home",
        data() {
            return {
                loginOut: false
            };
        },
        methods: {
            logoutUser() {
                this.$store.state.user.logOut();
                this.$router.push({ name: 'loginPage' });
            }
        }
    }
</script>
