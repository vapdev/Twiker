<template>
    <div class="flex flex-col w-full dark:bg-dark border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0 max-[600px]:mb-14" id="twikkerprofileapp">
        <div id="profile" class="flex flex-col p-6 border-solid border-b-2 border-gray-100 dark:border-gray-700">
            <div class="bg-opacity-40">
                <div class="flex w-full justify-between">
                    <div class="flex">
                        <article>
                            <Avatar :avatar_url="user.avatar" />
                        </article> 
                        <div class="font-bold text-lg">{{ user.username }}</div>
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
        <Tweek v-for="tweek in tweeks" :key="tweek.id" :tweek="tweek" @callGetTweeks="getProfileTweeks"/>
        <LoadingSpinner v-if="isLoading" :size="8" class="mt-5" />
    </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router';
import Tweek from '../components/Tweek.vue';
import Avatar from '../components/Avatar.vue';
import LoadingSpinner from '../components/LoadingSpinner.vue'

const isLoading = ref(true);

const cookie_user_id = document.cookie.split('; ')
            .find(row => row.startsWith('user_id='))
            ?.split('=')[1];

const cookie_username = document.cookie.split('; ')
.find(row => row.startsWith('username='))
?.split('=')[1];


const route = useRoute();

const tweeks = ref([]);
const user = ref('');
const followed_by = ref('');
const following = ref('');
const follow = ref(false)
let lastTweekId = null; // initialize last tweet ID to null

async function logged_user_follows_user(){
    await axios.get(`/api/user1_follows_user2/${cookie_username}/${route.params.username}`,)
    .then(response => {
        if(response.data['follows'] == true){
            follow.value = true
        }else{
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

async function getProfileTweeks(refresh = false){
    isLoading.value = true
    try{
        if (refresh) {
            currentPage = 1;
            lastTweekId = null; // reset last tweet ID to null
        }
        let url = `api/get_profile_tweeks/${user.value.id}/?page=${currentPage}`
        if (lastTweekId) {
            url += `&last_tweek_id=${lastTweekId}`; // add last tweet ID to URL if it exists
        }
        const response = await axios.get(url);
        hasNext = false;
        if (response.data.next) {
            hasNext = true;
        }
        if (lastTweekId) {
            tweeks.value = tweeks.value.concat(response.data.results); // add new tweets to end of existing tweets
        } else {
            tweeks.value = response.data.results; // replace existing tweets with new tweets if no last tweet ID
        }
        if (response.data.results.length > 0) {
            lastTweekId = response.data.results[response.data.results.length - 1].id; // set last tweet ID to ID of last tweet in response
        }
    } catch (error) {
        console.log(error)
    }
    isLoading.value = false;
}

const threshold = 100; // threshold value in pixels
let isGettingTweeks = false;
let currentPage = 1;
let hasNext = false;

function handleScroll() {
  const scrollPosition = window.scrollY;
  const windowSize = window.innerHeight;
  const documentHeight = document.documentElement.scrollHeight;
  const visibleBottom = scrollPosition + windowSize;

  if (visibleBottom >= (documentHeight - threshold) && hasNext && !isGettingTweeks) {
    currentPage += 1;
    isGettingTweeks = true;
    getProfileTweeks().then(() => {
      isGettingTweeks = false;
    });
  }
}

onMounted(async () => {
	await getUser();
	logged_user_follows_user();
	getProfileTweeks();
  window.addEventListener('scroll', handleScroll);
});
</script>