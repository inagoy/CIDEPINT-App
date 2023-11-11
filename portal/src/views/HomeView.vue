<script setup>
import SearchItem from '../components/navigation/SearchItem.vue'
</script>

<template>
  <main class="container">
    <div class="card text-start p-4">
      <h3>Bienvenido al sitio de CIDEPINT</h3>
      <p class="card-text">
        Acá un texto el en que te digo que hacemos y cosas bonitas de ese estilo mira que lindo todo. 
      </p>
      <p class="card-text">
        En este sitio vas a poder
      </p>
      <ul class="list px-6">
        <li class="list-item">Ver todos los servicios que prestan nuestras institucones</li>
        <li class="list-item">Buscar un servicio específico</li>
        <li class="list-item">Solicitar servicios</li>
      </ul>
      <p class="card-text">
        Contactate con nosotros:
      </p>
      <p class="card-text">
        Aca el contacto
      </p>
    </div>

    <SearchItem />
  </main>
</template>
