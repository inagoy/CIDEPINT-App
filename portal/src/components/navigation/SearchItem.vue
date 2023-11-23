<script>
import { ref, computed, onMounted } from "vue";
import { fetchWrapper } from "@/helpers/fetch-wrapper";
import { usePaginationStore } from '@/stores/pagination';

const API_URL = import.meta.env.VITE_API_URL;
const pagination = usePaginationStore()

export default {
  name: "SearchItem",
  setup() {
    const servicesTypes = ref([]);

    const inputSearch = ref("");
    const type = ref(null);

    const fetchServicesTypes =  async () => {
      const response = await fetchWrapper.get(API_URL + "/services-types");
      servicesTypes.value = response.data;
    };

    const clearSearch = () => {
      inputSearch.value = "";
      type.value = null;
      search();
    };

    const search =  async () => {
      let URL = API_URL + "/services/search?q=" + inputSearch.value + "&";
      if (type.value) {
        URL += "type=" + type.value + "&";
      }
      pagination.setUrl(URL);
      pagination.fetchData();
    };

    onMounted(() => {
      fetchServicesTypes();
      search();
    });

    const validateInput = () => {
      if (!inputSearch.value || !inputSearch.value.trim()) {
        return false;
      }
      return true;
    };

    const isButtonEnabled = computed(() => {
      return validateInput();
    });

    return {
      servicesTypes,
      search,
      clearSearch,
      validateInput,
      isButtonEnabled,
      inputSearch,
      type,
    };
  },
};
</script>

<template>
  <div class="card text-center">
    <h6 class="card-header"> Buscar por título, descripción, institución o palabras claves:</h6>
    <div class="card-body">
      <form class="d-flex pr-md-3" role="search" @submit.prevent="search">
        <input
          class="form-control me-2"
          type="search"
          placeholder="Buscar servicio"
          aria-label="Search"
          id="searchInput"
          v-model="inputSearch"
          :style="{ borderColor: validateInput() ? '' : '#D63030' }"
          required
        />
        <select id="selectServiceType" class="form-select me-2" v-model="type">
          <option selected value="">Seleccionar tipo</option>
          <option v-for="serviceType in servicesTypes" :value="serviceType">
            {{ serviceType }}
          </option>
        </select>

        <button class="btn btn-outline-success"  :disabled="!isButtonEnabled" type="submit">Buscar</button>
        <button class="btn btn-outline-secondary" type="button" @click="clearSearch">Limpiar</button>
      </form>
    </div>
  </div>
</template>

<style scoped>
button {
  margin-left: 5px;
  margin-right: 5px;
}
</style>