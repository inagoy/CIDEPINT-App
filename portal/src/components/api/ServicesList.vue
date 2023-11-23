<script setup>
import ServiceCard from '@/components/cards/ServiceCard.vue'
import PageItemsSelector from '@/components/buttons/PageItemsSelector.vue'
import { usePaginationStore } from '@/stores/pagination';
import { watch, onBeforeMount } from 'vue';

const pagination = usePaginationStore();

onBeforeMount(() => {
  pagination.reset();
})

</script>

<template>
  <div>
    <h4 v-if="!pagination.data" class="text-center mt-4 mb-2">Cargando...</h4>
    <h4 v-else-if="pagination.data.length === 0" class="text-center mt-4 mb-2">No hay servicios disponibles para mostrar</h4>
    <template v-else>
      <PageItemsSelector/>
      <div v-for="service in pagination.data" :key="service.id" class="mb-3">
        <ServiceCard :service="service" />
      </div>
    </template>
  </div>
</template>
