<script>
export default {
  name: 'ServiceRequestButton',
  props: {
    // estoy pasando el ID del servicio aca, para poder hacer la solicitud
    serviceID: {
      type: Number,
      required: true
    },
    serviceEnabled: {
      type: Boolean,
      required: true,
      default: true
    }
  }
}
// Falta agregar de que no pueda solicitar si esta iniciada la sesion
</script>

<template>
  <button class="btn btn-success me-2 mt-1" :disabled="!serviceEnabled">Solicitar servicio</button>
</template>
