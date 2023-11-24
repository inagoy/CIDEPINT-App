<script setup>
import { onMounted, ref } from 'vue'
import { fetchWrapper } from '@/helpers/fetch-wrapper'
import VueApexCharts from 'vue3-apexcharts'

const apexchart = VueApexCharts

const API_URL = import.meta.env.VITE_API_URL

onMounted(async () => {
  const response = await fetchWrapper.get(`${API_URL}/services/top-requested`)
  const data = response.data
  series.value = data.percentages
  chartOptions.value = {
    ...chartOptions.value,
    labels: data.services,
    plotOptions: {
      radialBar: {
        dataLabels: {
          name: {
            fontSize: '22px'
          },
          value: {
            fontSize: '16px',
            formatter: function (value) {
              return value + '% de las solicitudes'
            }
          },
          total: {
            show: true,
            label: 'Total de Solicitudes',
            color: '#333',
            formatter: function (w) {
              return data.total
            }
          }
        }
      }
    },
    legend: {
      show: true,
      horizontalAlign: 'center',
      floating: false,
      fontSize: '16px',
      position: 'bottom',
      labels: {
        useSeriesColors: true
      },
      onItemClick: {
        toggleDataSeries: true
      },
      onItemHover: {
        highlightDataSeries: true
      },
      formatter: function (seriesName, opts) {
        return seriesName + ': ' + data.requests[opts.seriesIndex]
      }
    }
  }
  status.value = 'loaded'
})

const status = ref('loading')
const series = ref(null)
const chartOptions = ref({
  chart: {
    type: 'radialBar'
  },
  labels: null
})
</script>

<template>
  <div>
    <div class="mx-auto" style="max-width: 90vw; height: 60vh; max-height: 70vh">
      <h4 class="text-center" v-if="status === 'loading'">Cargando...</h4>
      <apexchart
        height="100%"
        type="radialBar"
        :options="chartOptions"
        :series="series"
        v-if="series"
      ></apexchart>
    </div>
  </div>
</template>
