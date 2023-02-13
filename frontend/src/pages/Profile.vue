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
                    <div class="flex flex-col ml-4" v-if="user.id != store.state.user_id">
                        <router-link :to="`/conversation/${user.id}`" class="cursor-pointer" >Send message</router-link>
                        <span class="cursor-pointer" @click="unfollowUser()">Unfollow</span>
                        <span class="cursor-pointer" @click="followUser()">Follow</span>
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
import { useStore } from 'vuex'

const route = useRoute();

const store = useStore();

const user = ref('');
const followed_by = ref('');
const following = ref('');

async function logged_user_follows_user(){
    await axios.get(`/api/user1_follows_user2/${store.state.username}/${route.params.username}`,)
    .then(response => {
        if(response.data['follows'] == true){
            console.log("USER FOLLOWS PROFILE USER")
            followed_by.value = true
        }else{
            console.log("USER DOES NOT FOLLOW PROFILE USER")
            followed_by.value = false
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
}
async function unfollowUser(){
    await axios.post(`/api/unfollow/${route.params.username}`,) 
    .then(response => {
        getUser()
    })
    .catch(error => {
        console.log('error' + error)
    })
}

onMounted(() => {
    getUser();
    logged_user_follows_user();
})

</script>