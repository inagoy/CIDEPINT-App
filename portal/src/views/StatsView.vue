<script setup>



import ChartRequests from '../components/charts/ChartRequests.vue'
import ChartRequestsType from '../components/charts/ChartRequestsType.vue';
import ChartInstitutionsResponse from '../components/charts/ChartInstitutionsResponse.vue';
import { useChartsStore } from '@/stores/charts';

const charts = useChartsStore()

</script>

<template>
  <main class="container">
    <h4 class="text-center">Estadísticas</h4>
    <div class="btn-group btn-group-toggle mx-auto" data-toggle="buttons">
    <button  @click="charts.chartOne()" :class= "{ active: charts.actualChart === 1 }" class="btn btn-outline-secondary">
      Servicios más solicitados
    </button >
    <button  @click="charts.chartTwo()" :class= "{ active: charts.actualChart === 2 }" class="btn btn-outline-secondary">
      Solicitudes por tipo de Servicio
    </button >
    <button  @click="charts.chartThree()" :class= "{ active: charts.actualChart === 3 }" class="btn btn-outline-secondary">
      Instituciones más rápidas
    </button >
  </div>
    <div class="box">
      <div class="content">
        <ChartRequests v-if="charts.actualChart === 1"></ChartRequests>
        <ChartRequestsType v-if="charts.actualChart === 2"></ChartRequestsType>
        <ChartInstitutionsResponse v-if="charts.actualChart === 3"></ChartInstitutionsResponse>
      </div>
    </div>
  </main>
  
  
</template>

<style>
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
