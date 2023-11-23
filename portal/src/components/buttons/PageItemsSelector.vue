<template>
  <div id="pageItemsSelector" class="d-flex justify-content-start align-items-start gap-3 p-2">
      <label for="selectServicePerPage" class="form-label"><b>Elementos por página: </b></label>
      <select id="selectServicePerPage" class="form-select" v-model="perPage" :aria-selected="perPage">
        <option value="5">5</option>
        <option value="10">10</option>
        <option value="15">15</option>
        <option value="20">20</option>
      </select>
  </div>
</template>


<script setup>
import { usePaginationStore } from '@/stores/pagination';
import { ref, watch } from 'vue';

const pagination = usePaginationStore()
const perPage = ref(pagination.perPage);

watch(perPage, () => {
  pagination.changePerPage(perPage.value);
});

</script>

<style scoped>
.form-select {
  width: auto;
  border-color: black;
}
#pageItemsSelector{
  margin-bottom: 10px;
}
</style>