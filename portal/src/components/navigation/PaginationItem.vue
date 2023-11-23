<script setup>
import { usePaginationStore } from '@/stores/pagination';

const pagination = usePaginationStore()
</script>

<template v-if="pagination.data">
  <div>
    <nav>
      <ul class="pagination justify-content-center">
        <li class="page-item" :class="{ disabled: pagination.page === 1 }">
          <button class="page-link" @click="pagination.backPage()" :disabled="pagination.page === 1">&lt;&lt;</button>
        </li>
        <li v-for="pageNumber in pagination.totalPages()" :key="pageNumber">
          <div class="page-item" :class="{ active: pageNumber === pagination.page }">
            <button class="page-link" @click="pagination.goToPage(pageNumber)">{{ pageNumber }}</button>
          </div>
        </li>
        <li class="page-item" :class="{ disabled: pagination.page === pagination.totalPages() }">
          <button class="page-link" @click="pagination.nextPage()" :disabled="pagination.page === pagination.totalPages()">&gt;&gt;</button>
        </li>
      </ul>
    </nav>
  </div>
</template>

<style scoped>
.paginated-item {
  margin-bottom: 8px;
}

.pagination-buttons {
  display: flex;
  justify-content: center;
  margin-top: 16px;
}

.pagination-buttons button {
  margin: 0 4px;
  padding: 8px;
  cursor: pointer;
}

.pagination-buttons button:disabled {
  cursor: not-allowed;
  color: #888;
}

.pagination-buttons button.active {
  background-color: #007bff;
  color: #fff;
  border: 1px solid #007bff;
}
</style>
