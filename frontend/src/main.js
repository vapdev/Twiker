import { createApp } from 'vue'
import { createPinia } from 'pinia'
import './style.css'
import App from './App.vue'
import router from './router'
import axios from 'axios'
const app = createApp(App);
const pinia = createPinia()
axios.defaults.baseURL = import.meta.env.VITE_API_BASE_URL
app.use(pinia)
.use(router)
.mount('#app');
