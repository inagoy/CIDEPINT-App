<script setup>
import { ref } from 'vue'
import ChartRequests from '../components/charts/ChartRequests.vue'
import ChartRequestsType from '../components/charts/ChartRequestsType.vue';

const selected = ref(0)

</script>

<template>
  <main class="container">
    <div class="box">
      <div class="content">
        <ChartRequests v-if="selected === 0"></ChartRequests>
        <ChartRequestsType v-if="selected === 1"></ChartRequestsType>
      </div>
    </div>
  </main>
  <div class="btn-group btn-group-toggle mx-auto" data-toggle="buttons">
    <label class="btn btn-outline-secondary">
      <input @click="selected = 0" type="radio" name="options" id="option1" autocomplete="off" checked> Servicios más solicitados
    </label>
    <label class="btn btn-outline-secondary">
      <input @click="selected = 1" type="radio" name="options" id="option2" autocomplete="off"> Solicitudes por tipo de servicio
    </label>
    <label class="btn btn-outline-secondary">
      <input @click="selected = 2" type="radio" name="options" id="option3" autocomplete="off"> Instituciones más rápidas
    </label>
  </div>
  
</template>

<style>
.container {
  display: flex;
  justify-content: space-between;
}

.box {
  height: 100%; /* Make all boxes the same height */
  display: flex;
  align-items: center;
  box-sizing: border-box;
  flex: 1; /* Distribute available space equally among boxes */
}

.content {
  width: 100%;
}
</style>
