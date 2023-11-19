<script setup>
import { ref, onMounted } from 'vue'
import { fetchWrapper } from '@/helpers/fetch-wrapper';
import VueApexCharts from 'vue3-apexcharts';


const apexchart = VueApexCharts

const API_URL = import.meta.env.VITE_API_URL

onMounted(async () => {
    const response = await fetchWrapper.get(`${API_URL}/services/requests-by-type`);
    const data = response.data;
    series.value = data.requests;
    chartOptions.value = {
      ...chartOptions.value,
      labels: data.types,

    };
    status.value = "loaded";
})

const status = ref("loading");
const series = ref(null)
const chartOptions = ref({
    chart: {
        type: 'polarArea'
    },
    labels: null,
    fill: {
        opacity: 1
    },
    stroke: {
        width: 1,
        colors: undefined
    },
    yaxis: {
        show: false
    },
    legend: {
        position: 'bottom',

    },
    plotOptions: {
        polarArea: {
            rings: {
                strokeWidth: 2
            },
            spokes: {
                strokeWidth: 0
            },
        }
    },
})


</script>

<template>
    <h2 class="text-center mt-4"> Solicitudes por tipo de servicio </h2>
    <div class="mt-2 mx-auto">
    <h4 v-if="status === 'loading'">loading...</h4>
        <apexchart
            type="polarArea" 
            width="500"
            :options="chartOptions"
            :series="series"
            v-if="series"
        ></apexchart>
    </div>
</template>