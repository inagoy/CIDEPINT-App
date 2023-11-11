<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import ServiceCard from '../cards/ServiceCard.vue'
const API_URL = import.meta.env.VITE_API_URL

export default {
  setup() {
    const posts = ref([])
    console.log('la variable', API_URL + '/services/search?q=')
    onMounted(() => {
      axios.get(API_URL + '/services/search?q=').then((response) => {
        console.log('response', response.data.data)
        posts.value = response.data.data
      })
    })
    return {
      posts
    }
  },
  components: { ServiceCard }
}
</script>

<template>
  <h4 class="text-center">Todos los servicios</h4>
  <div v-for="post in posts" :key="post.id">
    <ServiceCard :service="post" />
  </div>
</template>
