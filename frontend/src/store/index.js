import { createStore } from 'vuex';

export default createStore({
    state: {
        token: '',
        isAuthenticated: false,
        username: '',
        user_id: '',
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
        removeToken(state) {
            state.token = ''
            state.isAuthenticated = false
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