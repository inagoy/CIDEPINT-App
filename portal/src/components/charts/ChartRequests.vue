
<script setup>
import { onMounted, ref } from 'vue';
import { fetchWrapper } from '@/helpers/fetch-wrapper';
import VueApexCharts from 'vue3-apexcharts';

const apexchart = VueApexCharts;

const API_URL = import.meta.env.VITE_API_URL

onMounted(async () => {
    const response = await fetchWrapper.get(`${API_URL}/services/top-requested`);
    const data = response.data;
    series.value = data.requests;
    chartOptions.value = {
      ...chartOptions.value,
      labels: data.services,
      plotOptions: {
        radialBar: {
          dataLabels: {
            name: {
              fontSize: '22px',
            },
            value: {
              fontSize: '16px',
            },
            total: {
              show: true,
              label: 'Total de Solicitudes',
              color: '#333',
              formatter: function (w) {
                // By default this function returns the average of all series. The below is just an example to show the use of custom formatter function
                return data.total
              }
            }
          }
        }
      },
    }
    status.value = "loaded";
});
    
const status = ref("loading");
const series = ref(null);
const chartOptions = ref({
  chart: {
    type: 'radialBar',
  },
  labels: null,
})

</script>

<template>
    <div>
      <h4 v-if="status === 'loading'">loading...</h4>
      <apexchart
        height="600"
        type="radialBar"
        :options="chartOptions"
        :series="series"
        v-if="series"
      ></apexchart>
    </div>
  </template>