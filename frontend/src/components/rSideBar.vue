<template>
    <div class="sticky top-0 left-0 px-2 h-screen max-lg:hidden">
        <div class="flex flex-col justify-between h-full">
            <div>
                <form method="get" action="">
                    <div class="flex flex-row p-2 my-2 border-solid border-2 border-gray-100 dark:border-gray-700 rounded-full">
                        <div>
                            <input class="text-sm h-fit w-full outline-none bg-white dark:bg-slate-900" type="text" name="query" placeholder="Search">
                        </div>
                        <div>
                            <button><i class="p-1 fa-solid fa-magnifying-glass"></i></button>
                        </div>
                    </div>
                </form>
                <div class="flex flex-col w-full">
                    <form v-on:submit.prevent="submitTweek()" class="m-0">
                        <div class="flex w-full pb-3">
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
            <div class="flex flex-row justify-between w-full my-3 hover:bg-gray-200 dark:hover:bg-gray-700 hover:rounded-full">
                <div class="flex p-1">
                    <img class="rounded-full h-12 w-12 m-auto" src="">
                    <h1 class="ml-1  font-semibold ">Fabio</h1>
                </div>
                <div class="flex">
                    <a class=" text-lg m-auto p-1" style="margin-left: auto; " href="">
                        <i class="fa-solid fa-user-pen"></i>
                    </a>
                </div>
            </div>
        </div>
    </div>        
</template>

<script>
import axios from 'axios'

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
            tweeks: [],
            body: '',
            currentPage: 1,
            tweeker: 'tweeker_username',
            created_at: 'Now',
            avatar: 'tweeker_avatar',
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
