<script setup>
import { useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'
import axios from 'axios'
import ServiceInfoCard from '../components/cards/ServiceInfoCard.vue'
import InstitutionInfo from '../components/cards/InstitutionInfo.vue'
import Map from '../components/cards/MapCard.vue'
import ServiceRequestButton from '../components/buttons/ServiceRequestButton.vue'

const API_URL = import.meta.env.VITE_API_URL
const route = useRoute()
const id = route.params.id
const serviceData = ref([])
const institutionData = ref([])

onMounted(() => {
  axios
    .get(API_URL + '/services/' + id)
    .then((response) => {
      serviceData.value = response.data
      console.log(API_URL + '/services/' + id)
      console.log(serviceData.value)
    })
    .then(() => {
      axios.get(API_URL + '/institutions/' + serviceData.value.laboratory).then((response) => {
        institutionData.value = response.data
        console.log(API_URL + '/institutions/' + serviceData.value.laboratory)
        console.log('coordenadas', institutionData.value.coordinates)
      })
    })
})
</script>

<template>
  <main class="container">
    <div
      class="d-flex flex-column-reverse flex-md-row align-items-center justify-content-center gap-3"
    >
      <div class="w-100">
        <ServiceInfoCard :service="serviceData" />
        <InstitutionInfo :institution="institutionData" />
      </div>
      <div class="flex-shrink-1 px-4 d-flex flex-column justify-content-start h-100">
        <p class="fst-italic">Debe iniciar sesión para poder solicitar un servicio</p>
        <ServiceRequestButton :serviceID="id" :serviceEnabled="serviceData.enabled" />
        <Map v-if="institutionData.coordinates !== null" :institution="institutionData" />
      </div>
    </div>
  </main>
</template>
