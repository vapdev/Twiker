import { createStore } from 'vuex';
import axios from 'axios';
export default createStore({
    state: {
        token: '',
        isAuthenticated: false,
        username: '',
        user_id: '',
    },
    getters: {
        isAuthenticated: state => state.isAuthenticated
    },
    mutations: {
        initializeStore(state) {
            if (localStorage.getItem('token')) {
                state.token = localStorage.getItem('token')
                state.isAuthenticated = true
            } else {
                state.token = ''
                state.isAuthenticated = false
            }
        },
        setToken(state, token) {
            state.token = token
            state.isAuthenticated = true
        },
        async removeToken(state) {
            try {
                await axios.post('/api/v1/auth/logout/');
                localStorage.removeItem('token');
                state.token = ''
                state.isAuthenticated = false
                this.$router.push({ name: 'Login' });
            } catch (error) {
                console.error(error);
            }
        },
        setUsername(state, username) {
            state.username = username
        },
        setUserId(state, user_id) {
            state.user_id = user_id
        }
    },
    actions: {
        
    },
    modules: {
    }
})