<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <RouterLink class="nav-brand pe-5" to="/">
          <img
            src="../../assets/logo-completo.png"
            alt="CIDEPINT"
            class="img-fluid logo d-none d-md-inline"
          />
          <img
            src="../../assets/logo.png"
            alt="CIDEPINT"
            class="img-fluid logo d-md-none d-inline"
          />
        </RouterLink>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
          <ul class="navbar-nav">
            <li class="nav-item">
              <RouterLink class="nav-link" to="/services">Servicios</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/requests">Solicitudes</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/stats">Estadísticas</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/register">Registrarse</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/test">API test</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/login">Log In</RouterLink>
            </li>
            <li class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle"
                href="#"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                Cuenta
              </a>
              <ul class="dropdown-menu dropdown-menu-end">
                <li><RouterLink class="dropdown-item" to="/profile">Ver perfil</RouterLink></li>
                <li><hr class="dropdown-divider" /></li>
                <li><a class="dropdown-item" href="#">Cerrar sesión</a></li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
  <RouterView />
</template>

<style scoped>
.logo {
  height: 4em;
  padding: 0.5em;
}
header {
  width: 100vw;
  position: sticky;
  z-index: 999;
  top: 0;
  left: 0;
}
</style>
