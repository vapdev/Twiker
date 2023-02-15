<template>
    <div class="flex flex-col w-full dark:bg-slate-900 border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0" id="twikkerprofileapp">
        <div id="profile" class="flex flex-col p-4 border-solid border-b-2 border-gray-100 dark:border-gray-700">
            <div class="bg-opacity-40">
                <div class="flex w-full justify-between">
                    <div class="flex">
                        <article>
                            <figure>
                                <div class="h-14 w-14 rounded-full border-2 border-white bg-gray-300"></div>
                            </figure>
                        </article> 
                        <h1>{{ user.username }}</h1>
                    </div>
                    <div class="flex">
                        <a class="cursor-pointer mr-4">Followers: {{ followed_by }}</a>
                        <a class="cursor-pointer">Follows: {{ following }}</a>
                    </div>
                </div>
                <div class="flex justify-end">
                    <div class="flex flex-col ml-4" v-if="user.id != cookie_user_id" :key="follow">
                        <router-link :to="`/conversation/${user.id}`" class="cursor-pointer" >Send message</router-link>
                        <span v-if="follow" class="cursor-pointer" @click="unfollowUser()">Unfollow</span>
                        <span v-if="!follow" class="cursor-pointer" @click="followUser()">Follow</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router';

const cookie_user_id = document.cookie.split('; ')
            .find(row => row.startsWith('user_id='))
            ?.split('=')[1];

const cookie_username = document.cookie.split('; ')
.find(row => row.startsWith('username='))
?.split('=')[1];


const route = useRoute();

const user = ref('');
const followed_by = ref('');
const following = ref('');
const follow = ref(false)

async function logged_user_follows_user(){
    await axios.get(`/api/user1_follows_user2/${cookie_username}/${route.params.username}`,)
    .then(response => {
        if(response.data['follows'] == true){
            console.log("USER FOLLOWS PROFILE USER")
            follow.value = true
        }else{
            console.log("USER DOES NOT FOLLOW PROFILE USER")
            follow.value = false
        }
    })
    .catch(error => {
        console.log('error' + error)
    })
}
async function getUser(){
    await axios.get(`/api/user_data/${route.params.username}`,) 
    .then(response => {
        user.value = response.data
        followed_by.value = response.data.followed_by
        following.value = response.data.following
    }).catch(error => {
        console.log('error' + error)
    })
}
async function followUser(){
    await axios.post(`/api/follow/${route.params.username}`,)
    .then(response => {
        getUser()
    }) 
    .catch(error => {
        console.log('error' + error)
    })
    logged_user_follows_user()
}
async function unfollowUser(){
    await axios.post(`/api/unfollow/${route.params.username}`,) 
    .then(response => {
        getUser()
    })
    .catch(error => {
        console.log('error' + error)
    })
    logged_user_follows_user()
}

onMounted(() => {
    getUser();
    logged_user_follows_user();
})

</script>