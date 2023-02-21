import { defineStore } from 'pinia';
import axios from 'axios';
import { useRouter } from 'vue-router';

export const useUserStore = defineStore('UserStore', {
    state: () => {
      return {
        router: useRouter(),
        token: '',
        isAuthenticated: false,
        username: '',
        user_id: '',
      }
    },
    getters: {
        Authenticated: (state) => state.isAuthenticated,
    },
    actions: {
        initializeStore() {
            const cookieValue = document.cookie.split('; ')
            .find(row => row.startsWith('token='))
            ?.split('=')[1];
        
            if (cookieValue) {
                this.token = cookieValue;
                this.isAuthenticated = true;
            } else {
                this.token = '';
                this.isAuthenticated = false;
            }
        },
        setToken(token) {
            this.token = token
            this.isAuthenticated = true
        },
        async removeToken() {
            try {
                await axios.post('/api/v1/auth/logout/');
                document.cookie = 'token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
                this.$reset();
                this.router.replace({ name: 'Login' });
            } catch (error) {
                console.error(error);
            }
        },
        setUsername(username) {
            this.username = username
        },
        setUserId(user_id) {
            this.user_id = user_id
        }
    },
  })