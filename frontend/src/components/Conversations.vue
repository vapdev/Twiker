<template>
    <div class="flex flex-col h-full w-fit border-solid border-r-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0">
        <div class="min-[600px]:sticky p-3 bg-white dark:bg-slate-900 top-0 w-full h-fit min-[600px]:opacity-95 text-2xl border-solid border-b-2 border-gray-100 dark:border-gray-700">
            <span class="opacity-100">Conversas</span>
        </div>
        <router-link :to="`conversation/${ conversation.user_id }`" v-for="conversation in conversations" class="flex h-fit w-full p-4 pt-3 pl-3 border-solid border-b-2 hover:bg-gray-100 dark:hover:bg-gray-700 border-gray-100 dark:border-gray-700" replace>
            <figure>
                <p class="h-12 w-12 rounded-full bg-gray-400 mr-3">
                </p>
            </figure>
            <div>
                <p>{{ conversation.username }}</p>
                <p>{{ conversation.formatted_time }}</p>
            </div>
        </router-link>
    </div>
</template>

<script>
import axios from 'axios'

    export default{
        data () {
            return {
                conversations: [],
            }
        },
        mounted() {
            this.getConversations();
        },
        methods: {
            getConversations(){
                axios.get(`/api/conversations`,) 
                .then(response => {
                    this.conversations = response.data;
                }).catch(error => {
                    console.log('error' + error)
                })
            },
        }
    }
</script>