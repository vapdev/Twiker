<template>
    <div class="flex min-w-full max-[600px]:mb-14">
        <div id="feedapp"
            class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0">
            <div
                class="min-[600px]:sticky p-3 bg-white dark:bg-dark top-0 min-[600px]:opacity-90 w-full h-fit text-2xl">
                <a href="">
                    <span class="opacity-100 font-semibold">Página inicial</span>
                </a>
            </div>
            <div class="flex h-30 w-full pt-3 pl-3 border-solid border-b-2 border-gray-100 dark:border-gray-700">
                <Avatar />
                <div class="flex flex-col w-full pl-1">
                    <form v-on:submit.prevent="submitTweek()">
                        <div class="flex w-full py-5">
                            <textarea placeholder="What you tweeking bro..."
                                class="text-xl resize-none h-fit w-full outline-none bg-white dark:bg-dark"
                                type="text" v-model="body"></textarea>
                        </div>
                        <div v-if="selectedImageUrl"  class="w-64 h-64">
                            <img :src="selectedImageUrl" />
                        </div>
                        <div class="flex border-solid border-t-2 border-gray-100 dark:border-gray-700 w-full">
                            <div class="flex my-2 w-full">
                                <div class="flex justify-between w-full">
                                    <div @click="selectImage" class="flex">
                                        <button class=""><i class="p-1 fa-regular fa-image"></i></button>
                                    </div>
                                    <div class="flex">
                                        <button id="submit-tweek" type="submit"
                                            class="bg-green-400 rounded-full text-white font-bold mx-3 px-5 py-2">Submit</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
            <Tweek v-for="tweek in tweeks" :key="tweek.id" :tweek="tweek" @callGetTweeks="getTweeks"/>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import Tweek from '../components/Tweek.vue';
import { ref, onMounted } from 'vue';
import Avatar from '../components/Avatar.vue';

document.body.addEventListener('keydown', function(e) {
  if(!(e.keyCode == 13 && (e.metaKey || e.ctrlKey))) return;
        let target = e.target;
        let submit_button = document.querySelector('#submit-tweek');
        if(target.form) {
            submit_button.click();
      }
  });


const tweeks = ref([]);
const body = ref('');
const selectedImageUrl = ref('');
const image = ref(null);
let currentPage = 1;
let tweeker = 'tweeker_username';
let created_at = 'Now';
let avatar = 'tweeker_avatar';
let retweeked_tweeks =  [];
let hasNext = false;

function selectImage(){
    let input = document.createElement('input');
    input.type = 'file';
    input.accept = 'image/*';
    input.onchange = e => {
        image.value = e.target.files[0];
        selectedImageUrl.value = URL.createObjectURL(image.value);
    }
    input.click();
    // const formData = new FormData();
    // formData.append('file', file);
    // await axios.post('/api/upload_image/', formData)
    // .then(response => {
    // imageUrl.value = response.data['image_url']
    // })
    // .catch(error => {
        // console.log('error' + error)
    // })
}
function submitTweek(tweek_id=null){
    if (body.value.length > 0 || tweek_id != null){
        let tweek = new FormData();
        tweek.append('body', body.value);
        tweek.append('tweeker', tweeker);
        tweek.append('created_at', created_at);
        tweek.append('avatar', avatar);
        tweek.append('retweek_id', tweek_id);
        tweek.append('image', image.value);
        // Send to backend
        axios.post('/api/add_tweek/', tweek)
        .catch((error) => {
            console.log(error)
        })
        currentPage = 1;
        getTweeks()
    }
    body.value = '';
    selectedImageUrl.value = '';
}

async function getTweeks(){
    await axios.get(`/api/get_tweeks/?page=${currentPage}`) 
    .then(response => {
        hasNext = false
        if (response.data.next) {
            hasNext = true
        }
        tweeks.value = response.data.results
    }).catch(error => {
        console.log('error' + error)
    })
}

onMounted(() => {
    getTweeks()
    window.onscroll = () => {
        let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documtweeksentElement.offsetHeight

        if (bottomOfWindow && hasNext) {
            currentPage += 1
            getTweeks()
        }
    }
})
</script>

<style>



</style>