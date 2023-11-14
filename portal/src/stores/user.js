import { defineStore } from "pinia";
const API_URL = import.meta.env.VITE_API_URL

export const useUserStore = defineStore("user", {
  state: () => ({
    token: null,
  }),

  actions: {
    async signIn(email, password) {
      const res = await axios.post(API_URL+'/auth', {
        user: email,
        password: password
      });
      const token = await res.data.token
      this.token = token;

    }
  }
});