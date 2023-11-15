import { defineStore } from 'pinia';
import { fetchWrapper } from '@/helpers/fetch-wrapper';

const API_URL = import.meta.env.VITE_API_URL

export const useProfileStore = defineStore({
    id: 'profile',
    state: () => ({
        profile: null
    }),
    actions: {
        async getProfile() {
            console.log("HOLAA")
            const res = await fetchWrapper.get(`${API_URL}/me/profile`);
            this.profile = res.data;
        },
    }
});