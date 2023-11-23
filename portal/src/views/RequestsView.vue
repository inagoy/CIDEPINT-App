<script setup>
import RequestList from '@/components/api/RequestList.vue'
import PaginationItem from '@/components/navigation/PaginationItem.vue'
import { usePaginationStore } from '@/stores/pagination';

const pagination = usePaginationStore();

</script>

<template>
  <main class="container">
    <h4 class="text-center">Solicitudes</h4>
    <div style="margin-bottom: 10px;">
      <RequestList />
      <PaginationItem v-if="pagination.data && pagination.data.length > 0"/>
    </div>
  </main>
</template>
