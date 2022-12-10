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

                <div class="flex flex-col">
                    <a href="{% url 'followers' user.username %}">Followers: {{ user.followed_by }}</a>
                    <a href="{% url 'follows' user.username %}">Follows: {{ user.following }}</a>
                        <a href="{% url 'conversation' user.id %}">Send message</a>
                        <span>
                            <a @click="unfollowUser()">Unfollow</a>
                            <a @click="followUser()">Follow</a>
                        </span>
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
                    console.log(this.user)
                }).catch(error => {
                    console.log('error' + error)
                })
            },
            followUser(){
                axios.post(`/api/follow/${this.$route.params.username}`,) 
                .then(response => {
                    console.log(response)
                }).catch(error => {
                    console.log('error' + error)
                })
            },
            unfollowUser(){
                axios.post(`/api/unfollow/${this.$route.params.username}`,) 
                .then(response => {
                    console.log(response)
                }).catch(error => {
                    console.log('error' + error)
                })
            }
        }
    }
</script>