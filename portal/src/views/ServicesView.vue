<script>
import SearchItem from '../components/navigation/SearchItem.vue'
import ServicesList from '../components/api/ServicesList.vue'
import { ref } from 'vue';

export default {
  name: 'ServicesView',
  components: {
    SearchItem,
    ServicesList
  },

  setup() {
    const searchResults = ref([]);
    const updateSearchResults = (results) => {
      searchResults.value = results;
    };
    
    return {
      searchResults,
      updateSearchResults,
    };
  },
};

</script>

<template>
  <main class="container">
    <h4 class="text-center">Servicios</h4>
    <SearchItem @search-results="updateSearchResults"/>
    <ServicesList :services="searchResults"/>
  </main>
</template>
