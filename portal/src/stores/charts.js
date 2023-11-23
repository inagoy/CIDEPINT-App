import { defineStore } from 'pinia';

export const useChartsStore = defineStore({
    id: 'charts',
    state: () => ({
        actualChart: 1
    }),

    actions: {
        chartOne() {this.actualChart = 1},
        chartTwo() {this.actualChart = 2},
        chartThree() {this.actualChart = 3},
    }
});