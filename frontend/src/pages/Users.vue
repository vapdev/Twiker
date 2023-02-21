<template>
    <div class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0 max-[600px]:mb-14">
        <div class="min-[600px]:sticky p-3 bg-white dark:bg-dark top-0 w-full h-fit min-[600px]:opacity-90 text-2xl border-b-2 border-gray-100 dark:border-gray-700 ">
            <div class="flex justify-between">
                <span class="opacity-100 font-semibold">Todos Usuários</span>
                <p>Usuários: {{ users.length }}</p>
            </div>
        </div>
        <router-link 
        :to="`/profile/${user.username}`" 
        v-for="user in users"
        class="flex flex-row h-fit w-full p-2 pt-3 pl-3 border-solid border-b-2 hover:bg-gray-100 dark:hover:bg-gray-700 border-gray-100 dark:border-gray-700">
            <Avatar class="mr-3" />
            <div class="flex flex-col">
                <div class="flex">
                    <div class="font-bold">{{ user.username }}</div>
                </div>
                <div class="flex">
                    <a>Seguidores: {{ user.followed_by }}</a>
                </div>
                <div class="flex">
                    <a>Seguindo: {{ user.following }}</a>
                </div>
            </div>
        </router-link>
        <LoadingSpinner v-if="isLoading" :size="8" class="mt-5" />
    </div>
</template>


<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import Avatar from '../components/Avatar.vue'
import LoadingSpinner from '../components/LoadingSpinner.vue'

const users = ref([]);
const isLoading = ref(true);

async function getUsers(){
    isLoading.value = true;
    await axios.get(`/api/users/`) 
    .then(response => {
        users.value = response.data;
    }).catch(error => {
        console.log('error' + error)
    })
    isLoading.value = false;
}
onMounted(() => {
    getUsers();
})

</script>