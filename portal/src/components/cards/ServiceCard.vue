<script>
import { RouterLink, RouterView } from 'vue-router'
import ServiceRequestButton from '../buttons/ServiceRequestButton.vue'
export default {
  props: {
    service: {
      type: Object
    }
  },
  components: {
    ServiceRequestButton
  }
}
</script>

<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title">
        {{ service.name }} <span class="badge bg-secondary"> {{ service.service_type }}</span>
      </h5>
      <h6 class="card-subtitle mb-2 text-body-secondary">
        <u>Institución:</u> {{ service.laboratory }}
      </h6>
      <p class="card-text">
        <u>Descripción:</u> {{ service.description }}
      </p>
      <p class="card-text">
        <u>Palabras claves para la búsqueda:</u> {{ service.keywords }}
      </p>
      <div class="">
        <RouterLink
          :to="{ name: 'service', params: { id: service.id } }"
          class="btn btn-primary me-2 mt-1"
          :disabled="!service.enabled"
          >Ver servicio</RouterLink
        >
        <RouterView />
        <ServiceRequestButton :serviceID="service.id" :serviceEnabled="service.enabled" />
      </div>
    </div>
  </div>
</template>
