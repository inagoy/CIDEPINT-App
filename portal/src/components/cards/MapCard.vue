<script>
import { onMounted, ref, watch } from 'vue'

export default {
  name: 'Map',
  props: {
    institution: {
      type: Object
    }
  },
  setup(props) {
    let map, marker

    watch(
      () => props.institution,
      (newVal, oldVal) => {
        if (newVal) {
          // Props are available
          map = L.map('map').setView([-34.9223, -57.9546], 12)
          L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
          }).addTo(map)
          marker = L.marker([-34.9223, -57.9546]).addTo(map)
          marker
            .bindPopup('<b>Dirección: </b>' + props.institution.address + '<br/> <b>Contacto: </b>' + props.institution.email)
            .openPopup()
        } else {
          // Props are not available
          console.log('esperando prop!!!!')
        }
      }
    )
  }
}
</script>

<template>
  <div class="my-4">
    <h6 class="fw-bold">Cómo llegar</h6>
    <div id="map"></div>
  </div>
</template>

<style scoped>
#map {
  height: 220px;
  width: 25vw;
}
@media screen and (max-width: 768px) {
  #map {
    width: 90vw;
  }
  
}
</style>
