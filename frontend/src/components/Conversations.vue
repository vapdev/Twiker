<template>
    <div class="sticky max-[600px]:fixed max-[600px]:bottom-0 min-[600px]:top-0 min-[600px]:left-0 max-[600px]:right-0 h-screen max-[600px]:h-12 max-[600px]:w-screen bg-white dark:bg-slate-900 overflow-y-hidden">
        <div class="flex flex-col max-[600px]:flex-row h-full max-[600px]:w-screen border-solid border-r-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0 overflow">
            <div class="p-3 bg-white dark:bg-slate-900 top-0 w-full h-fit min-[600px]:opacity-95 text-2xl border-solid border-b-2 border-gray-100 dark:border-gray-700 max-[600px]:hidden">
                <span class="opacity-100">Conversas</span>
            </div>
            <div v-for="conversation in conversations" class="flex">
                <a @click="goToConversation(conversation.user_id)" class="flex h-fit w-full max-[600px]:w-fit p-4 pt-3 pl-3 border-solid min-[600px]:border-b-2 max-[600px]:border hover:bg-gray-100 dark:hover:bg-gray-700 border-gray-100 dark:border-gray-700">
                    <figure>
                        <p class="h-12 w-12 max-lg:h-8 max-lg:w-8 rounded-full bg-gray-400 mr-3">
                        </p>
                    </figure>
                    <div>
                        <p>{{ conversation.username }}</p>
                        <p class="max-lg:hidden">{{ conversation.formatted_time }}</p>
                    </div>
                </a>
            </div>
        </div>
    </div>
</template>

<script setup>

import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const conversations = ref([]);
const router = useRouter();

function getConversations(){
    axios.get(`/api/conversations`,) 
    .then(response => {
        conversations.value = response.data;
    }).catch(error => {
        console.log('error' + error)
    })
}
function goToConversation(user_id) {
    router.push(`/conversation/${user_id}`)
}
onMounted(() => {
    getConversations();
})

</script>