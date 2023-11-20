<script>
import ServiceCard from '../cards/ServiceCard.vue'
export default {
  name: 'ServicesList',
  props: {
    services: Array,
  },
  components: {
    ServiceCard
  }
}
</script>

<template>
  <h4 v-if="services.length === 0" class="text-center">No hay servicios disponibles para mostrar</h4>
  <h4 v-else class="text-center">Servicios</h4>
  <div v-for="service in services" :key="service.id">
    <ServiceCard :service="service" />
  </div>
</template>
