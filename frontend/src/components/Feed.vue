<template>
    <div class="flex min-w-full">
        <div id="feedapp"
            class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0">
            <div
                class="min-[600px]:sticky p-3 bg-white dark:bg-slate-900 top-0 min-[600px]:opacity-90 w-full h-fit text-2xl">
                <a href="">
                    <span class="opacity-100 font-semibold">Página inicial</span>
                </a>
            </div>
            <div class="flex h-30 w-full pt-3 pl-3 border-solid border-b-2 border-gray-100 dark:border-gray-700">
                <div class="flex w-14 h-full pt-1">
                    <img class="rounded-full h-12 w-12">
                </div>
                <div class="flex flex-col w-full pl-1">
                    <form v-on:submit.prevent="submitTweek()">
                        <div class="flex w-full py-5">
                            <textarea placeholder="What you tweeking bro..."
                                class="text-xl resize-none h-fit w-full outline-none bg-white dark:bg-slate-900"
                                type="text" v-model="body"></textarea>
                        </div>
                        <div class="flex border-solid border-t-2 border-gray-100 dark:border-gray-700 w-full">
                            <div class="flex my-2 w-full">
                                <div class="flex justify-between w-full">
                                    <div class="flex">
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
            <div v-for="tweek in tweeks" :key="tweek.id">
                <div class="flex h-fit w-full p-3 border-solid border-b-2 hover:bg-gray-100 dark:hover:bg-gray-700 border-gray-100 dark:border-gray-700">
                    <div class="flex flex-col w-full">
                        <div v-if="tweek.retweek" class="flex items-center mb-1">
                            <i class="text-blue-600 fa-solid fa-retweet mr-2"></i>
                            <span class="flex font-semibold"> {{ tweek.tweeker_name + ' compartilhou' }} </span>
                        </div>
                        <div class="flex">
                            <div class="flex w-14 h-full mr-2">
                                <img class="rounded-full h-12 w-12" :src="tweek.retweek ? tweek.retweek_avatar_url : tweek.avatar_url">
                            </div>
                            <div class="flex flex-col w-full">
                                <div>
                                    <span class="font-semibold text-lg">
                                        {{ tweek.retweek ? tweek.retweek_tweeker_name : tweek.tweeker_name }}
                                    </span>
                                    <span class="ml-2">
                                        {{ tweek.retweek ? tweek.retweek_formatted_time : tweek.formatted_time }}
                                    </span>
                                </div>
                                <span class="flex text-xl break-all">{{ tweek.retweek ? tweek.retweek_body : tweek.body }}</span>
                                <div v-if="!tweek.is_retweek" class="flex flex-row justify-between w-2/3 mt-1">
                                    <div class="flex items-center">
                                        <div class="flex w-8 h-8 hover:bg-yellow-200 hover:rounded-full">
                                            <i class="m-auto fa-regular fa-comment-dots"></i>
                                        </div>
                                        <span>12</span>
                                    </div>
                                    <div class="flex items-center">
                                        <div @click.stop="toggleRetweek(tweek)" class="flex w-8 h-8 hover:bg-blue-300 hover:rounded-full">
                                            <i :id="'retweek-'+tweek.id" :class="tweek.is_retweeked ? 'text-blue-600 fa-solid fa-retweet' : 'fa-solid fa-retweet'" class="m-auto"></i>
                                        </div>
                                        <span>{{ tweek.retweek_count }}</span>
                                    </div>
                                    <div class="flex items-center">
                                        <div @click.stop="toggleLike(tweek)" class="flex w-8 h-8 p-1 mx-1 text-center hover:bg-green-200 hover:rounded-full">
                                            <i :id="'like-'+tweek.id" :class=" !tweek.is_liked ? 'fa-regular fa-thumbs-up' : 'fa-solid fa-thumbs-up'" class="m-auto"></i>
                                        </div>
                                        <span :id="'likes-'+tweek.id">{{ tweek.likes_count }}</span>
                                        <div @click.stop="toggleDislike(tweek)" class="flex w-8 h-8 p-1 mx-1 text-center hover:bg-red-200 hover:rounded-full">
                                            <i :id="'dislike-'+tweek.id" :class=" !tweek.is_disliked ? 'fa-regular fa-thumbs-down' : 'fa-solid fa-thumbs-down'" class="m-auto"></i>
                                        </div>
                                        <span  :id="'dislikes-'+tweek.id">{{ tweek.dislikes_count }}</span>
                                    </div>
                                </div>
                                <div v-if="tweek.retweek">
                                    <div @click.stop="viewTweek(tweek.id)"><p class="text-md mt-2 text-blue-300 w-fit hover:text-blue-100 rounded-xl">Ver tweek original</p></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { getTransitionRawChildren } from 'vue';
import Tweek from './Tweek.vue';

document.body.addEventListener('keydown', function(e) {
  if(!(e.keyCode == 13 && (e.metaKey || e.ctrlKey))) return;
        let target = e.target;
        let submit_button = document.querySelector('#submit-tweek');
        if(target.form) {
            submit_button.click();
      }
  });

export default {
    components: {
        Tweek
    },
    data() {
        return {
            count: 0,
            tweeks: [],
            body: '',
            currentPage: 1,
            tweeker: 'tweeker_username',
            created_at: 'Now',
            avatar: 'tweeker_avatar',
            retweeked_tweeks: [],
        }
    },
    mounted() {
        this.getTweeks()
        window.onscroll = () => {
            let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight

            if (bottomOfWindow && this.hasNext) {
                this.currentPage += 1
                this.getTweeks()
            }
        }
    },
    methods: {
        async getTweeks(){
            await axios.get(`/api/get_tweeks/?page=${this.currentPage}`) 
            .then(response => {
                this.hasNext = false
                if (response.data.next) {
                    this.hasNext = true
                }
                this.tweeks = response.data.results
            }).catch(error => {
                console.log('error' + error)
            })
        },
        viewTweek(tweek_id) {
            window.location.href = `/tweek/${tweek_id}`
        },
        async toggleLike(tweek){
            if(tweek.retweek_id){
                await axios.get(`/api/tweek/${tweek.retweek_id}/`,)
                .then(response => {
                    tweek = response.data['tweek']
                }).catch(error => {
                    console.log('error' + error)
                })
            }
            if(tweek.is_disliked){
                this.undislikeTweek(tweek);
            }
            if(tweek.is_liked){
                this.unlikeTweek(tweek);
            }else{
                this.likeTweek(tweek);
            }
        },
        likeTweek(tweek){
            tweek.is_liked = true;
            tweek.likes_count += 1;
            let tweek_id = {
                'tweek_id': tweek.id
            };
            axios.post('/api/add_like/', tweek_id,)
            .catch(error => {
                console.log('error' + error)
            })
        },
        unlikeTweek(tweek){
            tweek.is_liked = false;
            tweek.likes_count -= 1;
            var tweek_id = {
                'tweek_id': tweek.id
            };
            axios.post('/api/remove_like/', tweek_id,)
            .catch(error => {
                console.log('error' + error)
            })
        },
        toggleRetweek(tweek){
            if(tweek.is_retweeked){
                this.unretweekTweek(tweek.id);
            }else{
                this.submitTweek(tweek.id);
            }
        },
        async unretweekTweek(tweek_id){
            var tweek = {
                'tweek_id': tweek_id,
            };
            await axios.post('/api/remove_retweek/', tweek,)  
            .catch(error => {
                console.log('error' + error)
            })
            this.getTweeks();
        },
        async toggleDislike(tweek){
            if(tweek.retweek_id){
                await axios.get(`/api/tweek/${tweek.retweek_id}/`,)
                .then(response => {
                    tweek = response.data['tweek']
                }).catch(error => {
                    console.log('error' + error)
                })
            }
            if(tweek.is_liked){
            this.unlikeTweek(tweek);
            }
            if(tweek.is_disliked){
            this.undislikeTweek(tweek);
            }else{
            this.dislikeTweek(tweek);
            }
        },
        dislikeTweek(tweek){
            tweek.is_disliked = true;
            tweek.dislikes_count += 1;
            let tweek_id = {
                'tweek_id': tweek.id
            }
            axios.post('/api/add_dislike/', tweek_id,)
            .catch(error => {
                console.log('error' + error)
            })
        },
        undislikeTweek(tweek){
            tweek.is_disliked = false;
            tweek.dislikes_count -= 1;
            var tweek_id = {
                'tweek_id': tweek.id
            };
            axios.post('/api/remove_dislike/', tweek_id,)
            .catch(error => {
                console.log('error' + error)
            })
        },
        deleteTweek(tweek_id){
            var tweek = {
                'tweek_id': tweek_id,
            };
            axios.post('/api/delete_tweek/', tweek,)
            .catch(error => {
                console.log('error' + error)
            })
            const el = document.getElementById('tweek-' + tweek_id);
            el.remove();
        },
        async submitTweek(tweek_id=null){
            if (this.body.length > 0 || tweek_id != null){
                let tweek = {
                    'body': this.body,
                    'tweeker': this.tweeker,
                    'created_at': this.created_at,
                    'avatar': this.avatar,
                    'retweek_id': tweek_id,
                };
                // Send to backend
                await axios.post('/api/add_tweek/', tweek,)
                .catch((error) => {
                    console.log(error)
                })
                this.currentPage = 1;
                this.getTweeks()
            }
            this.body = '';
        },
    }
}
</script>
