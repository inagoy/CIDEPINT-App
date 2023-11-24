
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
    total.value = series.value.reduce((partialSum, a) => partialSum + a, 0);
    chartOptions.value = {
        ...chartOptions.value,
        labels: data.types,

        dataLabels: {
            enabled: true,
            formatter: function (val, { seriesIndex, dataPointIndex, w }) {
                return data.requests[seriesIndex]
            },
            background: {
                enabled: true,
                foreColor: '#555',
                borderWidth: 0,
                borderRadius: 2,
                padding: 10,
                dropShadow: {
                    enabled: true,
                }
            },
            style: {
                fontSize: '20px',
            },
        }
    };
    
    status.value = "loaded";
})

const status = ref("loading");
const series = ref(null)
const total = ref(null)

const chartOptions = ref({
    chart: {
        type: 'polarArea',

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
        show: false,
    },
    legend: {
        position: 'bottom',
        fontSize: '16px',
        itemMargin: {
          horizontal: 20,
        },
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
    <div>
        <div class="mx-auto" style="max-width: 600px; height: 70vh">
            <h4 class="text-center" v-if="status === 'loading'">Cargando...</h4>
            <p v-if="series" class="text-center "> Total de Solicitudes: {{ total }} </p>
            <apexchart type="polarArea" height="90%" :options="chartOptions" :series="series" v-if="series"></apexchart>
        </div>
    </div>
</template>