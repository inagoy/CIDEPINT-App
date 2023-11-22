<script>
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()

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
  },
  methods: {
    redirectPage() {
      if (authStore.user) {
        this.$router.push({ name: 'serviceRequest', params: { id: this.serviceID } })
      } else {
        this.$router.push({ name: 'login' })
      }
    }
  }
}
</script>

<template>
  <button class="btn btn-success me-2 mt-1" :disabled="!serviceEnabled" @click="redirectPage">
    Solicitar servicio
  </button>
</template>
