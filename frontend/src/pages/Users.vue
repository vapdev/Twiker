<template>
    <div class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0">
        <div class="p-3 bg-white dark:bg-dark top-0 w-full h-fit text-2xl border-solid border-b-2 border-gray-100 dark:border-gray-700">
            <div class="flex justify-between">
                <h1 class="title">All Users</h1>
                <p>Total users: {{ users.length }}</p>
            </div>
        </div>
        <div v-for="user in users" class="flex flex-row h-fit w-full p-2 pt-3 pl-3 border-solid border-b-2 hover:bg-gray-100 dark:hover:bg-gray-700 border-gray-100 dark:border-gray-700">
            <Avatar />
            <div class="flex flex-col">
                <div class="flex">
                    <h1>
                        <router-link :to="`/profile/${user.username}`">{{ user.username }}</router-link>
                    </h1>
                </div>
                <div class="flex">
                    <a>Seguidores: {{ user.followed_by }}</a>
                </div>
                <div class="flex">
                    <a>Seguindo: {{ user.following }}</a>
                </div>
            </div>
        </div>
    </div>
</template>


<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import Avatar from '../components/Avatar.vue'

const users = ref([]);

function getUsers(){
    axios.get(`/api/users/`) 
    .then(response => {
        users.value = response.data;
    }).catch(error => {
        console.log('error' + error)
    })
}
onMounted(() => {
    getUsers();
})

</script>