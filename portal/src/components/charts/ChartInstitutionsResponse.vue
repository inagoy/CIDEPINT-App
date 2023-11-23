<script setup>

import { ref, onMounted } from 'vue'
import { fetchWrapper } from '@/helpers/fetch-wrapper';
import VueApexCharts from 'vue3-apexcharts';


const apexchart = VueApexCharts

const API_URL = import.meta.env.VITE_API_URL

onMounted(async () => {
    
    const response = await fetchWrapper.get(`${API_URL}/institutions/by-response-time`);
    const data = response.data;
    series.value = [{name:'Días Promedio', data:data.averages}];
    chartOptions.value = {
        ...chartOptions.value,
        xaxis: {
            categories: data.institutions,
            title: {
                text: 'Días Promedio',
                style: {
                    fontSize: '15px',
                }
            },
        },
        yaxis: {
            reversed: true,
            labels: {
                maxWidth: 600,
                style: {
                    fontSize: '14px',
                },
            },
        }
    };
    status.value = "loaded";
});

const status = ref("loading");
const series = ref(null)
const chartOptions = ref({
    chart: {
        type: 'bar',
    },
    plotOptions: {
        bar: {
            borderRadius: 2,
            horizontal: true,

        },
    },
    dataLabels: {
        enabled: true,
        formatter: function (value) {
            return value + ' días';
        },
        style: {
            fontSize: '14px',
        },

        
    },
    xaxis: {
        categories: null,  
    },
})
</script>


<template>
    <div>
        <div class="mx-auto" style="max-width: 1000px; height: 70vh">
            <h4 class="text-center" v-if="status === 'loading'">loading...</h4>
            <apexchart type="bar" height="100%" :options="chartOptions" :series="series" v-if="series"></apexchart>
        </div>
    </div>
</template>