import { defineStore } from 'pinia';
import { fetchWrapper } from '@/helpers/fetch-wrapper';

export const usePaginationStore = defineStore({
    id: 'pagination',
    state: () => ({
        page: 1,
        perPage: 10,
        total: 0,
        data: [],
        url: ''
    }),
    actions: {
        async fetchData() {
            let url = `${this.url}page=${this.page}&per_page=${this.perPage}`;
            const response = await fetchWrapper.get(url);
            this.data = response.data;
            this.total = response.total;
        },

        async backPage () {
            if (this.page !== 1) {
                this.page -= 1;
                this.fetchData();
            }
        },
        async nextPage () {
            if (this.page !== this.totalPages()) {
                this.page += 1;
                this.fetchData();
            }
        },

        async goToPage (numPage) {
            this.page = numPage;
            this.fetchData();
        },

        async changePerPage (newPerPage) {
            this.perPage = newPerPage;
            this.goToPage(1);
        },

        totalPages () {
            return Math.ceil(this.total / this.perPage);
        },

        reset(){
            this.page = 1;
            this.perPage = 10;
            this.total = 0;
            this.data = [];
            this.url = '';
        },

        // SETTERS
        setPage (numPage) {this.page = numPage;},

        setPerPage (numPerPage) {this.perPage = numPerPage;},

        setTotal (total) {this.total = total;},

        setData (data) {this.data = data;},

        setUrl (url) {this.url = url;},
    }
});