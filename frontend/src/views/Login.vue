<template>
    <div class="flex h-screen w-screen bg-slate-900">
    <div class="w-2/4 m-auto text-center">
        <i class="text-4xl m-auto fa-solid fa-ankh"></i>
        <h1 class="text-4xl font-bold text-blue-300">Twikker</h1>
        <p class="text-xs text-gray-300">"Quem já tem ciência age na inteligência, tudo te leva a crer, vitória é ter paciência"</p>
    </div>
    <div class="w-2/4 dark w-50 flex items-center justify-center border-l-2 border-gray-500 text-gray-400">
        <form @submit.prevent="submitForm" class="text-lg">
            <p class="text-base">Usuário:</p>
            <div class="flex flex-col">
                <input class="rounded-md mb-1 text-base " type="text" name="username" v-model="username">
                <input class="rounded-md mb-2 text-base " type="password" name="password" v-model="password"> 
            </div>
            <div class="flex justify-between">
                <button type="submit" class="hover:scale-105 text-bold hover:text-gray-200 text-sm ml-1">Log In</button>
                <router-link to='/signup' class="hover:scale-105 text-bold hover:text-gray-200 text-sm mr-1" href="{% url 'signup' %} ">Sign Up</router-link>
            </div>
        </form>
    </div>
</div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useUserStore } from '../store/UserStore.js'

const userStore = useUserStore()
const router = useRouter();
const route = useRoute();


const username = ref('');
const password = ref('');

const expiryDate = new Date();
expiryDate.setTime(expiryDate.getTime() + (3 * 24 * 60 * 60 * 1000));


function submitForm(e){
    const formData = {
        username: username.value,
        password: password.value,
    }

    axios
        .post('api/v1/token/login', formData)
        .then(response => {
            const token = response.data.auth_token
            userStore.setToken(token)
            axios.defaults.headers.common['Authorization'] = `Token ${token}`
            document.cookie = `token=${token}; expires=${expiryDate.toUTCString()}; path=/`;
            if (userStore.isAuthenticated){
                router.push('/')
            }
        })
        .catch(error => {
            console.log('error' + error)
        })
}

onMounted(() => {
    if (route.name == 'Logout'){
        userStore.removeToken()
    }
})
</script>
