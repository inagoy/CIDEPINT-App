<script setup>
import SearchItem from '@/components/navigation/SearchItem.vue'
import ServicesList from '@/components/api/ServicesList.vue'
import PaginationItem from '@/components/navigation/PaginationItem.vue'
import { usePaginationStore } from '@/stores/pagination';

const pagination = usePaginationStore();

</script>

<template>
  <main class="container">
    <h4 class="text-center">Servicios</h4>
    <SearchItem/>
    <div style="margin-bottom: 10px;">
      <ServicesList/>
      <PaginationItem v-if="pagination.data && pagination.data.length > 0"/>
    </div>
  </main>
</template> 
