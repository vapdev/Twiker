import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import store from './store'
console.log('dsaasd'+import.meta.env.VITE_API_BASE_URL)
axios.defaults.baseURL = import.meta.env.VITE_API_BASE_URL
createApp(App).use(store).use(router, axios).mount('#app')
