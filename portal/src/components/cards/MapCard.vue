<script>
import { onMounted } from 'vue'

export default {
  name: 'Map',
  props: {
    location: {
      type: String
    }
  },
  setup() {
    let map, marker
    onMounted(() => {
      map = L.map('map').setView([-34.9223, -57.9546], 12)
      L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
      }).addTo(map)
      marker = L.marker([-34.9223, -57.9546]).addTo(map);
      marker.bindPopup("<b>Dirección:</b> aaaaa <br/> <b>Contacto:</b> aaaaa").openPopup();
    })
  }
}
</script>

<template>
  <div class=" my-4">
    <h6 class="fw-bold"> Cómo llegar </h6>
    <div id="map"></div>
  </div>
</template>

<style scoped>
#map {
  height: 220px;
}
</style>
