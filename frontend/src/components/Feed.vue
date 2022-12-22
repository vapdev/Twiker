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
                    <img class="rounded-full h-12 w-12" src="">
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
            <Tweek v-for="tweek in tweeks" :key="tweek.id" :tweek="tweek" @callGetTweeks="getTweeks"/>
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
        Tweek,
    },
    data() {
        return {
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
