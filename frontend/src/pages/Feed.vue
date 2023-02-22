<template>
    <div class="flex min-w-full max-[600px]:mb-14">
        <div
            class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0">
            <div
                class="min-[600px]:sticky p-3 bg-white dark:bg-dark top-0 w-full h-fit min-[600px]:opacity-90 text-2xl border-b-2 border-gray-100 dark:border-gray-700 ">
                <a href="">
                    <span class="opacity-100 font-semibold">Página inicial</span>
                </a>
            </div>
            <div class="flex h-30 w-full pt-3 pl-3 border-solid border-b-2 border-gray-100 dark:border-gray-700">
                <Avatar :avatar_url="userStore.avatar" />
                <div class="flex flex-col w-full pl-1">
                    <form>
                        <div class="flex w-full py-2">
                            <textarea
                            @input="textAreaAdjust($event.target)"
                            id="textarea"  
                            placeholder="What you tweeking bro..."
                            class="text-xl resize-none overflow-hidden w-full h-8 break-all outline-none pl-1.5 pr-6 bg-white dark:bg-dark"
                            type="text"
                            v-model="body"
                            >
                            </textarea>
                        </div>
                        <div v-if="selectedImageUrl" class="w-64 h-64">
                            <img :src="selectedImageUrl" />
                        </div>
                        <div class="flex border-solid border-t-2 border-gray-100 dark:border-gray-700 w-full">
                            <div class="flex mt-2 w-full">
                                <div class="flex justify-between h-10 w-full">
                                    <div @click.prevent="selectImage()" class="flex">
                                        <button class=""><i class="p-1 fa-regular fa-image"></i></button>
                                    </div>
                                    <div class="flex">
										<LoadingSpinner v-if="isPosting" :size="8" class="py-1.5"/>
                                        <button @click.prevent="submitTweek()" id="submit-tweek" type="submit"
                                            class="bg-green-400 rounded-full text-white font-bold mx-3 px-5 py-2">
                                            Submit
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
            <Tweek v-for="tweek in tweeks" :key="tweek.id" :tweek="tweek" @callGetTweeks="getTweeks" />
            <LoadingSpinner v-if="isLoading" :size="8" class="mt-5" />
        </div>
    </div>
</template>

<script setup>
import axios from 'axios';
import Tweek from '../components/Tweek.vue';
import { ref, onMounted, defineAsyncComponent, computed } from 'vue';
import Avatar from '../components/Avatar.vue';

import { useUserStore } from '../store/UserStore';

const userStore = useUserStore();

function textAreaAdjust(element) {
  element.style.height = "32px";
  element.style.height = (element.scrollHeight)+"px";
}

const LoadingSpinner = defineAsyncComponent(() => import('../components/LoadingSpinner.vue'));

let formSubmitted = false;

document.body.addEventListener('keydown', function (e) {
    if (!(e.keyCode == 13 && (e.metaKey || e.ctrlKey))) return;
    let target = e.target;
    let submit_button = document.querySelector('#submit-tweek');
    if (target.form && !formSubmitted && body.value != '') {
        formSubmitted = true;
        submit_button.click();
    }
});

const tweeks = ref([]);
const body = ref('');
const selectedImageUrl = ref('');
const image = ref(null);
const isLoading = ref(true);
const isPosting = ref(false);
let currentPage = 1;
let tweeker = 'tweeker_username';
let created_at = 'Now';
let avatar = 'tweeker_avatar';
let retweeked_tweeks = [];
let hasNext = false;

function selectImage() {
    let input = document.createElement('input');
    input.type = 'file';
    input.accept = 'image/*';
    input.onchange = e => {
        image.value = e.target.files[0];
        selectedImageUrl.value = URL.createObjectURL(image.value);
    }
    input.click();
}

async function submitTweek(tweek_id = null) {
    if (body.value.length > 0 || tweek_id != null || image.value != null) {
        let tweek = new FormData();
        tweek.append('body', body.value);
        tweek.append('tweeker', tweeker);
        tweek.append('created_at', created_at);
        tweek.append('avatar', avatar);
        tweek.append('retweek_id', tweek_id);
        tweek.append('image', image.value);
		isPosting.value = true;
        try {
            // Send to backend
            await axios.post('/api/add_tweek/', tweek);
            currentPage = 1;
            await getTweeks();
        } catch (error) {
            console.log(error);
        }
	isPosting.value = false;
    }
    body.value = '';
    selectedImageUrl.value = null;
    image.value = null;
}

async function getTweeks() {
    isLoading.value = true;
    try {
        const response = await axios.get(`/api/get_tweeks/?page=${currentPage}`);
        hasNext = false;
        if (response.data.next) {
            hasNext = true;
        }
        tweeks.value = tweeks.value.concat(response.data.results);
    } catch (error) {
        console.log('error' + error);
    }
    isLoading.value = false;
    formSubmitted = false;
}
const threshold = 100; // threshold value in pixels
let isGettingTweeks = false;

function handleScroll() {
  const scrollPosition = window.scrollY;
  const windowSize = window.innerHeight;
  const documentHeight = document.documentElement.scrollHeight;
  const visibleBottom = scrollPosition + windowSize;

  if (visibleBottom >= (documentHeight - threshold) && hasNext && !isGettingTweeks) {
    currentPage += 1;
    isGettingTweeks = true;
    getTweeks().then(() => {
      isGettingTweeks = false;
    });
  }
}

onMounted(() => {
  getTweeks();
  window.addEventListener('scroll', handleScroll);
});



</script>


<style></style>