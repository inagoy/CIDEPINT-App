import { defineStore } from 'pinia';
import { fetchWrapper } from '@/helpers/fetch-wrapper';
import { googleTokenLogin } from "vue3-google-login"
import router from '@/router';

const API_URL = import.meta.env.VITE_API_URL

export const useAuthStore = defineStore({
    id: 'auth',
    state: () => ({
        user: JSON.parse(localStorage.getItem('user')),
    }),
    actions: {
        async login(email, password) {
            const auth = await fetchWrapper.post(`${API_URL}/auth`, {
                "user": email, "password": password 
            });
            this.user = auth;
            
            localStorage.setItem('user', JSON.stringify(this.user));
            this.userProfile()
            router.push('/');

        },
        
        async loginWithGoogle(response) {
            const auth = await fetchWrapper.post(`${API_URL}/auth-google`, response);
            this.user = auth;
            localStorage.setItem('user', JSON.stringify(this.user));
            this.userProfile()
            router.push('/');
        },

        async userProfile(){
            const profile = await fetchWrapper.get(`${API_URL}/me/profile`);
            this.user.profile = profile.data;
            localStorage.setItem('user', JSON.stringify(this.user)); 
        },
        logout() {
            router.push('/');
            this.user = null;
            localStorage.removeItem('user');
        }
    }
});