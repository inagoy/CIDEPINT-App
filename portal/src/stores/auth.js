import { defineStore } from 'pinia';
import { fetchWrapper } from '@/helpers/fetch-wrapper';
import router from '@/router';

const API_URL = import.meta.env.VITE_API_URL

export const useAuthStore = defineStore({
    id: 'auth',
    state: () => ({
        user: JSON.parse(localStorage.getItem('user')),
    }),
    actions: {
        async login(email, password) {
            const user = await fetchWrapper.post(`${API_URL}/auth`, {
                "user": email, "password": password 
            });

            this.user = user;

            localStorage.setItem('user', JSON.stringify(user));

            router.push('/');
        },
        logout() {
            this.user = null;
            localStorage.removeItem('user');
            router.push('/');
        }
    }
});