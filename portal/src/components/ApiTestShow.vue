<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'
const API_URL = import.meta.env.VITE_API_URL


export default {
  setup() {
    const posts = ref([])
    console.log('la variable', API_URL+'/institutions')
    onMounted(() => {
      axios
        .get(API_URL+'/institutions')
        .then((response) => {
          console.log('response', response.data.data)
          posts.value = response.data.data
        })
    })

    return {
      posts
    }
  }
}
</script>

<template>
  <div v-for="post in posts" :key="post.id">
    <h2>{{ post.name }} {{ post.address }}</h2>
    <p>{{ post.email }}</p>
  </div>
</template>
