<script>
import { ref, onMounted, watch } from 'vue'
import { fetchWrapper } from '@/helpers/fetch-wrapper'

import RequestCard from '../cards/RequestCard.vue'
const API_URL = import.meta.env.VITE_API_URL

export default {
  setup() {
    const posts = ref([])
    const sortBy = ref('status') // Default value for sorting
    const sortOrder = ref('desc') // Default value for ordering

    onMounted(async () => {
      await fetchData()
    })

    const fetchData = async () => {
      const request = await fetchWrapper.get(
        `${API_URL}/me/requests?sort=${sortBy.value}&order=${sortOrder.value}`
      )
      posts.value = request.data
      console.log('posts: ', posts)
    }

    // Watch for changes in sortBy or sortOrder and fetch data accordingly
    watch([sortBy, sortOrder], async () => {
      await fetchData()
    })

    return {
      posts,
      sortBy,
      sortOrder
    }
  },
  components: { RequestCard }
}
</script>

<template>
  <h4 class="text-center">Solicitudes</h4>
  <div class="d-grid gap-2 d-md-flex justify-content-md-end align-items-center">
    <h6 class="mb-0"><b> Ordenar por: </b></h6>
    <select v-model="sortBy" class="form-select w-md-25" aria-label="Default select example">
      <option value="status">Estado</option>
      <option value="title">Título</option>
      <option value="service_id">Servicio</option>
      <option value="inserted_at">Fecha de creación</option>
    </select>
    <select v-model="sortOrder" class="form-select w-md-25" aria-label="Default select example">
      <option value="desc">Descendiente</option>
      <option value="asc">Ascendiente</option>
    </select>
  </div>
  <div v-for="post in posts" :key="post.id">
    <RequestCard :request="post" />
  </div>
</template>
