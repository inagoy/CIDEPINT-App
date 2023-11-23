<script>
import { ref, watch, onBeforeMount } from 'vue'
import RequestCard from '@/components/cards/RequestCard.vue'
import PageItemsSelector from '@/components/buttons/PageItemsSelector.vue'
import { usePaginationStore } from '@/stores/pagination';

const pagination = usePaginationStore();

const API_URL = import.meta.env.VITE_API_URL

export default {
  setup() {
    const posts = ref([])
    const sortBy = ref('status') // Default value for sorting
    const sortOrder = ref('desc') // Default value for ordering

    onBeforeMount(() => {
      pagination.reset();
      fetchData();
    })

    const fetchData = async () => {
     let URL  = `${API_URL}/me/requests?sort=${sortBy.value}&order=${sortOrder.value}&`
      pagination.setUrl(URL);
      pagination.fetchData();
    }

    // Watch for changes in sortBy or sortOrder and fetch data accordingly
    watch([sortBy, sortOrder], async () => {
      await fetchData()
    })

    return {
      posts,
      sortBy,
      sortOrder,
      pagination
    }
  },
  components: { 
    RequestCard,
    PageItemsSelector
  }
}
</script>

<template>
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
  <div id="requestList">
    <h4 v-if="!pagination.data" class="text-center mt-4 mb-2">Cargando...</h4>
    <h4 v-else-if="pagination.data.length === 0" class="text-center mt-4 mb-2">No hay solicitudes disponibles para mostrar</h4>
    <template v-else>
      <PageItemsSelector/>
      <div v-for="post in pagination.data" :key="post.id" class="mb-3">
        <RequestCard :request="post" />
      </div>
    </template>
  </div>
</template>

<style scoped>
#requestList {
  margin-top: 20px;

}
</style>