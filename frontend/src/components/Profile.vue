<template>
    <div class="flex-col w-full bg-white dark:bg-slate-900 border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0" id="twikkerprofileapp">
        <div class="flex flex-col p-4 border-solid border-b-2 border-gray-100 dark:border-gray-700">
            <div class="flex">
                <div class="flex flex-col">
                        <article>
                            <figure>
                                <div class="h-14 w-14 rounded-full border-2 border-white bg-gray300"></div>
                            </figure>
                        </article> 
                    <h1>{{ user.username }}</h1>
                </div>
                <div class="flex flex-col ml-4">
                    <a class="cursor-pointer">Followers: {{ followed_by }}</a>
                    <a class="cursor-pointer">Follows: {{ following }}</a>
                </div>
                <div class="flex flex-col ml-4">
                    <router-link v-if="user.id != this.$store.state.user_id"  :to="`/conversation/${user.id}`" class="cursor-pointer" >Send message</router-link>
                    <span class="cursor-pointer" @click="unfollowUser()">Unfollow</span>
                    <span class="cursor-pointer" @click="followUser()">Follow</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
    export default{
        data() {
            return {
                user: '',
                followed_by: '',
                following: '',
            }
        },
        mounted() {
            this.getUser()
        },
        methods: {
            async getUser(){
                await axios.get(`/api/user_data/${this.$route.params.username}`,) 
                .then(response => {
                    this.user = response.data
                    this.followed_by = response.data.followed_by
                    this.following = response.data.following
                }).catch(error => {
                    console.log('error' + error)
                })
            },
            followUser(){
                axios.post(`/api/follow/${this.$route.params.username}`,)
                .then(response => {
                    this.getUser()
                }) 
                .catch(error => {
                    console.log('error' + error)
                })
            },
            unfollowUser(){
                axios.post(`/api/unfollow/${this.$route.params.username}`,) 
                .then(response => {
                    this.getUser()
                })
                .catch(error => {
                    console.log('error' + error)
                })
            }
        }
    }
</script>