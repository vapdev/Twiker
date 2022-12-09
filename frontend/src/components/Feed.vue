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
            <div v-for:="tweek in tweeks" :key="tweek.id"
                class="flex h-fit w-full px-3 border-solid border-b-2 hover:bg-gray-100 dark:hover:bg-gray-700 border-gray-100 dark:border-gray-700">
                <div class="flex flex-col w-full">
                    <div v-if="tweek.retweek" class="flex items-center mb-1">
                        <i class="text-blue-600 fa-solid fa-retweet mr-2"></i>
                        <span class="flex font-semibold"> {{ tweek.tweeker_name + ' compartilhou' }} </span>
                    </div>
                    <div class="flex h-3"></div>
                    <div class="flex">
                        <div class="flex w-14 h-full pr-2">
                            <img class="rounded-full h-12 w-12">
                        </div>
                        <div class="flex flex-col w-full pb-3">
                            <div>
                                <span class="font-semibold text-lg">
                                    {{ tweek.retweek ? tweek.retweek_tweeker_name : tweek.tweeker_name }}
                                </span>
                                <span class="ml-2">
                                    {{ tweek.retweek ? tweek.retweek_formatted_time : tweek.formatted_time }}
                                </span>
                            </div>
                            <span class="flex text-xl break-all">{{ tweek.retweek ? tweek.retweek_body : tweek.body }}</span>
                            <div v-if="!tweek.is_retweek" class="flex flex-row justify-between w-2/3 mt-3">
                                <div class="flex">
                                    <div class="w-8 h-8 p-1 text-center hover:bg-yellow-200 hover:rounded-full">
                                        <i class="fa-regular fa-comment-dots"></i>
                                    </div>
                                    <span class="pt-1"></span>
                                </div>
                                <div class="flex">
                                    <div @click.stop="toggleRetweek(tweek)" class="w-8 h-8 p-1 text-center hover:bg-blue-300 hover:rounded-full">
                                        <i :id="'retweek-'+tweek.id" :class=" tweek.is_retweeked ? 'text-blue-600 fa-solid fa-retweet' : 'fa-solid fa-retweet'"></i>
                                    </div>
                                    <span class="pt-1">{{ tweek.retweek_count }}</span>
                                </div>
                                <div class="flex">
                                    <div @click.stop="toggleLike(tweek)" class="flex mx-2">
                                        <div class="w-8 h-8 p-1 text-center hover:bg-green-200 hover:rounded-full">
                                            <i :id="'like-'+tweek.id" :class=" !tweek.is_liked ? 'fa-regular fa-thumbs-up' : 'fa-solid fa-thumbs-up' "></i>
                                        </div>
                                        <span :id="'likes-'+tweek.id" class="pt-1">{{ tweek.likes_count }}</span>
                                    </div>
                                    <div class="flex mx-2">
                                        <div @click.stop="toggleDislike(tweek)" class="w-8 h-8 p-1 text-center hover:bg-red-200 hover:rounded-full">
                                            <i :id="'dislike-'+tweek.id" :class=" !tweek.is_disliked ? 'fa-regular fa-thumbs-down' : 'fa-solid fa-thumbs-down' "></i>
                                        </div>
                                        <span  :id="'dislikes-'+tweek.id" class="pt-1">{{ tweek.dislikes_count }}</span>
                                    </div>
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
</template>

<script>
import axios from 'axios'
import { getTransitionRawChildren } from 'vue';

document.body.addEventListener('keydown', function(e) {
  if(!(e.keyCode == 13 && (e.metaKey || e.ctrlKey))) return;
        let target = e.target;
        let submit_button = document.querySelector('#submit-tweek');
        if(target.form) {
            submit_button.click();
      }
  });

export default {
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
        console.log("auth token: " + localStorage.getItem('token'))
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
            await axios.get(`/api/get_tweeks/?page=${this.currentPage}`,
                {
                    headers: {'Authorization': `Token ${localStorage.getItem('token')}`}
                }) 
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
                axios.get(`/api/tweek/${tweek.retweek_id}/`,
                    {
                        headers: {'Authorization': `Token ${localStorage.getItem('token')}`}
                    })
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
            axios.post('/api/add_like/', tweek_id,
                {
                    headers: {'Authorization': `Token ${localStorage.getItem('token')}`}
                })
            .then(response => {
                console.log(response.data)
            }).catch(error => {
                console.log('error' + error)
            })
        },
        unlikeTweek(tweek){
            tweek.is_liked = false;
            tweek.likes_count -= 1;
            var tweek_id = {
                'tweek_id': tweek.id
            };
            axios.post('/api/remove_like/', tweek_id,
                {
                    headers: {'Authorization': `Token ${localStorage.getItem('token')}`}
                })
            .then(response => {
                console.log(response.data)
            }).catch(error => {
                console.log('error' + error)
            })
        },
        async toggleRetweek(tweek){
            console.log('aqui 1')
            if(tweek.is_retweeked){
                await this.unretweekTweek(tweek.id);
            }else{
                console.log("submit" + tweek.id)
                await this.submitTweek(tweek.id);
            }
        },
        async unretweekTweek(tweek_id){
            var tweek = {
                'tweek_id': tweek_id,
            };
            axios.post('/api/remove_retweek/', tweek,
                {
                    headers: {'Authorization': `Token ${localStorage.getItem('token')}`}
                })  
            .then(response => {
                console.log(response.data)
            }).catch(error => {
                console.log('error' + error)
            })
            this.getTweeks();
        },
        async toggleDislike(tweek){
            if(tweek.retweek_id){
                axios.get(`/api/tweek/${tweek.retweek_id}/`,
                    {
                        headers: {'Authorization': `Token ${localStorage.getItem('token')}`}
                    })
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
            axios.post('/api/add_dislike/', tweek_id,
                {
                    headers: {'Authorization': `Token ${localStorage.getItem('token')}`}
                })
            .then(response => {
                console.log(response.data)
            }).catch(error => {
                console.log('error' + error)
            })
        },
        undislikeTweek(tweek){
            tweek.is_disliked = false;
            tweek.dislikes_count -= 1;
            var tweek_id = {
                'tweek_id': tweek.id
            };
            axios.post('/api/remove_dislike/', tweek_id,
                {
                    headers: {'Authorization': `Token ${localStorage.getItem('token')}`}
                })
            .then(response => {
                console.log(response.data)
            }).catch(error => {
                console.log('error' + error)
            })
        },
        deleteTweek(tweek_id){
            var tweek = {
                'tweek_id': tweek_id,
            };
            axios.post('/api/delete_tweek/', tweek,
                {
                    headers: {'Authorization': `Token ${localStorage.getItem('token')}`}
                })
            .then(response => {
                console.log(response.data)
            }).catch(error => {
                console.log('error' + error)
            })
            const el = document.getElementById('tweek-' + tweek_id);
            el.remove();
        },
        async submitTweek(tweek_id=null){
            console.log('id'+tweek_id)
            if (this.body.length > 0 || tweek_id != null){
                let tweek = {
                    'body': this.body,
                    'tweeker': this.tweeker,
                    'created_at': this.created_at,
                    'avatar': this.avatar,
                    'retweek_id': tweek_id,
                };
                // Send to backend
                await axios.post('/api/add_tweek/', tweek, {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Token ${localStorage.getItem('token')}`,
                        'X-CSRFToken': '{{ csrf_token }}',
                    },
                })
                .then((response) => {
                    console.log(response)
                })
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