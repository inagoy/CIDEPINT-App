<script setup>
import { useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'
import axios from 'axios'
import ServiceRequestForm from '../components/ServiceRequestForm.vue'

const API_URL = import.meta.env.VITE_API_URL
const route = useRoute()
const id = route.params.id
const serviceData = ref([])

onMounted(() => {
  window.scrollTo(0, 0)
  axios.get(API_URL + '/services/' + id).then((response) => {
    serviceData.value = response.data
    console.log(API_URL + '/services/' + id)
    console.log(serviceData.value)
  })
})
</script>

<template>
  <main class="container">
    <h2>Solicitud de servicio: {{ serviceData.name }}</h2>
    <ServiceRequestForm :serviceID="id" />
  </main>
</template>
