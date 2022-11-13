<template>
    <div class="flex min-w-full">
        <div id="feedapp" class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0">
            <div class="min-[600px]:sticky p-3 bg-white dark:bg-slate-900 top-0 min-[600px]:opacity-90 w-full h-fit text-2xl">
                <a href="#">
                    <span class="opacity-100 font-semibold">Página inicial</span>
                </a>
            </div>
            <div class="flex h-30 w-full pt-3 pl-3 border-solid border-b-2 border-gray-100 dark:border-gray-700">
                <div class="flex w-14 h-full pt-1">
                </div>
                <div class="flex flex-col w-full pl-1">
                    <form v-on:submit.prevent="submitTweek()">
                        <div class="flex w-full py-5">
                            <textarea placeholder="What you tweeking bro..." class="text-xl resize-none h-fit w-full outline-none bg-white dark:bg-slate-900" type="text" v-model="body"></textarea>
                        </div>
                        <div class="flex border-solid border-t-2 border-gray-100 dark:border-gray-700 w-full">
                            <div class="flex my-2 w-full">
                                <div class="flex justify-between w-full">
                                    <div class="flex">
                                        <button class=""><i class="p-1 fa-regular fa-image"></i></button>
                                    </div>
                                    <div class="flex">
                                        <button id="submit-tweet" type="submit" class="bg-green-400 rounded-full text-white font-bold mx-3 px-5 py-2">Submit</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
                <div v-for="tweek in tweeks" v-bind:key="tweek.id" class="flex h-fit w-full px-3 border-solid border-b-2 hover:bg-gray-100 dark:hover:bg-gray-700 border-gray-100 dark:border-gray-700">
                    <a href="#" @click="viewTweek(tweek.id)">
                    <div class="flex flex-col w-full">
                        <div v-if="tweek.retweek" class="flex mb-2">
                            <span class="flex font-semibold">{{ tweek.tweeker_name + ' compartilhou'}}</span>
                        </div>
                        <div v-else class="flex h-3"></div>
                        <div class="flex">
                            <div class="flex w-14 h-full pr-2">
                                <img class="rounded-full h-12 w-12" :src="tweek.retweek ? tweek.retweek_avatar_url : tweek.avatar_url">
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
                                <div v-if="!tweek.retweek" class="flex flex-row justify-between w-2/3 mt-3">
                                    <div class="flex">
                                        <div class="w-8 h-8 p-1 text-center hover:bg-yellow-200 hover:rounded-full">
                                            <i class="fa-regular fa-comment-dots"></i>
                                        </div>
                                        <span class="pt-1"></span>
                                    </div>
                                    <div class="flex">
                                        <div @click.stop="toggleRetweek(tweek.id)" class="w-8 h-8 p-1 text-center hover:bg-blue-300 hover:rounded-full">
                                            <i :id="'retweek-'+tweek.id" :class=" retweeked_tweeks.includes(tweek.id) ? 'text-blue-600 fa-solid fa-retweet' : 'fa-solid fa-retweet'"></i>
                                        </div>
                                        <span class="pt-1">{{ tweek.retweek_count }}</span>
                                    </div>
                                    <div class="flex">
                                        <div class="flex mx-2">
                                            <div @click.stop="toggleLike(tweek)" class="w-8 h-8 p-1 text-center hover:bg-green-200 hover:rounded-full">
                                                <i :id="'like-'+tweek.id" :class=" !tweek.is_liked ? 'fa-regular fa-thumbs-up' : 'fa-solid fa-thumbs-up' "></i>
                                            </div>
                                            <span :id="'likes-'+tweek.id" class="pt-1">{{ tweek.likes_count }}</span>
                                        </div>
                                        <div class="flex mx-2">
                                            <div @click.stop="toggleDislike(tweek)" class="w-8 h-8 p-1 text-center hover:bg-red-200 hover:rounded-full">
                                                <i :id="'dislike-'+tweek.id" :class=" !tweek.is_disliked ? 'fa-regular fa-thumbs-down' : 'fa-solid fa-thumbs-down' "></i>
                                            </div>
                                            <span :id="'dislikes-'+tweek.id" class="pt-1">{{ tweek.dislikes_count }}</span>
                                        </div>
                                    </div>
                                </div>
                                <div v-if="tweek.retweek">
                                    <a href="#"><p class="text-md mt-2 text-blue-300">Ver tweek original</p></a>
                                </div>
                            </div>
                        </div>
                    </div>
                    </a>
                </div>
        </div>
    </div>
</template>


<script>
document.body.addEventListener('keydown', function(e) {
  if(!(e.keyCode == 13 && (e.metaKey || e.ctrlKey))) return;
        let target = e.target;
        let submit_button = document.querySelector('#submit-tweet');
        if(target.form) {
            submit_button.click();
      }
  });

export default {
    name: 'Feed',
    data: function() {
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
        console.log("montado")
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
        getTweeks() {
            console.log("bah tche..")
            fetch(`http://127.0.0.1:8000/api/get_tweeks/1/?page=${this.currentPage}`)
                .then(response => {
                    return response.json()
                })
                .then(data => {
                        this.hasNext = false
                        if (data.next) {
                            this.hasNext = true
                        }
                        // this.tweeks = data.results
                        console.log('data', data)
                        for (let i = 0; i < data.results.length; i++) {
                            this.tweeks.push(data.results[i])
                        }
                }).catch(error => {
                    console.log('errooo' + error)
                })
        },
        viewTweek(tweek_id) {
            window.location.href = `/tweek/${tweek_id}`
        },
        async toggleLike(tweek){
            if(tweek.retweek_id){
                await fetch(`/api/tweek/${tweek.retweek_id}/`)
                    .then(response => {
                        return response.json()
                    }
                ).then(data => {
                    tweek = data['tweek']
                });
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
            fetch('/api/add_like/',{
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    credentials: 'same-origin',
                    body: JSON.stringify(tweek_id)
                })
                .then((response) => {
                    console.log(response);
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        unlikeTweek(tweek){
            tweek.is_liked = false;
            tweek.likes_count -= 1;
            var tweek_id = {
                'tweek_id': tweek.id
            };
            fetch('/api/remove_like/',{
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    // 'X-CSRFToken': '{{ csrf_token }}',
                },
                credentials: 'same-origin',
                body: JSON.stringify(tweek_id)
                })
                .then((response) => {
                    console.log(response);
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        async toggleRetweek(tweek_id){
            if(this.retweeked_tweeks.includes(tweek_id)){
                let el = document.getElementById(`retweek-${tweek_id}`);
                await this.unretweekTweek(tweek_id);
            }else{
                await this.submitTweek(tweek_id);
            }
            window.location.reload();
        },
        async unretweekTweek(tweek_id){
            this.retweeked_tweeks = this.retweeked_tweeks.filter(item => item !== tweek_id)
            var tweek = {
                'tweek_id': tweek_id,
            };
            await fetch('/api/remove_retweek/',{
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    // 'X-CSRFToken': '{{ csrf_token }}',
                },
                credentials: 'same-origin',
                body: JSON.stringify(tweek)
                })
                .then((response) => {
                    console.log(response);
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        async toggleDislike(tweek){
            if(tweek.retweek_id){
                await fetch(`/api/tweek/${tweek.retweek_id}/`)
                    .then(response => {
                        return response.json()
                    }
                ).then(data => {
                    tweek = data['tweek']
                });
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
            fetch('/api/add_dislike/',{
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        // 'X-CSRFToken': '{{ csrf_token }}',
                    },
                    credentials: 'same-origin',
                    body: JSON.stringify(tweek_id)
                })
                .then((response) => {
                    console.log(response);
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        undislikeTweek(tweek){
            tweek.is_disliked = false;
            tweek.dislikes_count -= 1;
            var tweek_id = {
                'tweek_id': tweek.id
            };
            fetch('/api/remove_dislike/',{
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        // 'X-CSRFToken': '{{ csrf_token }}',
                    },
                    credentials: 'same-origin',
                    body: JSON.stringify(tweek_id)
                })
                .then((response) => {
                    console.log(response);
                })
                .catch((error) => {
                    console.log(error);
            });
        },
        deleteTweek(tweek_id){
            var tweek = {
                'tweek_id': tweek_id,
            };
            fetch('/api/delete_tweek/',{
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    // 'X-CSRFToken': '{{ csrf_token }}',
                },
                credentials: 'same-origin',
                body: JSON.stringify(tweek)
                })
                .then((response) => {
                    console.log(response);
                })
                .catch((error) => {
                    console.log(error);
                });

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
                await fetch('/api/add_tweek/',{
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        // 'X-CSRFToken': '{{ csrf_token }}',
                    },
                    credentials: 'same-origin',
                    body: JSON.stringify(tweek)
                })
                .then((response) => {
                    console.log(response)
                })
                .catch((error) => {
                    console.log(error)
                })
                this.currentPage = 1;
                this.tweeks=[];
                this.getTweeks()
            }
            this.body = '';
        }
    },
}
</script>