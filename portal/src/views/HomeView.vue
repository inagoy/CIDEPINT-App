<script>
import SearchItem from '@/components/navigation/SearchItem.vue';
import { ref, onMounted } from 'vue'
import axios from 'axios'
const API_URL = import.meta.env.VITE_API_URL

export default {
  setup() {
    const contact_info = ref(null)
    onMounted(() => {
      axios
        .get(API_URL+'/contact-info')
        .then((response) => {
          contact_info.value = response.data.contact_info
        })
    })
    return {
      contact_info
    }
  },
  components: { SearchItem }
}
</script>

<template>
  <main class="container">
    <SearchItem />
    <div class="card text-start p-4">
      <h3>Bienvenido al sitio de CIDEPINT</h3>
      <p class="card-text">
        ¡Te damos la bienvenida al Portal de CIDEPINT! Aquí, podrás acceder a información relevante sobre el Laboratorio, información Institucional y servicios habilitados.
      </p>
      <p class="card-text">
        En este sitio vas a poder
      </p>
      <ul class="list px-6">
        <li class="list-item">Ver todos los servicios que prestan nuestras instituciones</li>
        <li class="list-item">Buscar un servicio específico</li>
        <li class="list-item">Visualizar la sección de análisis de datos, donde podrás ver:
          <ul class="list">
            <li class="list-item">Cantidad de solicitudes realizadas agrupadas por estado</li>
            <li class="list-item">Ranking de los servicios más solicitados</li>
            <li class="list-item">Top 10 de las instituciones con el mejor tiempo de resolución.</li>
          </ul>
        </li>
        <li class="list-item">Registrarte como usuario para:
          <ul class="list">
            <li class="list-item">Solicitar un servicio</li>
            <li class="list-item">Ver sus solicitudes</li>
            <li class="list-item">Detalles del Pedido</li>
            <li class="list-item">Ver y agregar notas a los pedidos</li>
          </ul>
        </li>
      </ul>
    </div>
    <div class="card text-start p-4">
      <h3>Información de contacto</h3>
      <p class="card-text">
        ¡Nos encantaría escucharte! Contactanos para cualquier consulta o comentario.
      </p>
      <p class="card-text">
        <strong>{{contact_info}}</strong>
      </p>
    </div>
  </main>
</template>
