<template>
    <div class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0">
        <div class="min-[600px]:sticky p-3 bg-white dark:bg-slate-900 top-0 w-full h-fit min-[600px]:opacity-95 text-2xl border-solid border-b-2 border-gray-100 dark:border-gray-700">
            <span class="opacity-100">Notificações</span>
        </div>
        <div v-for="notification in notifications" id="notificationapp" class="flex flex-col">
            <div class="flex flex-row h-fit w-full p-4 pt-3 pl-3 border-solid border-b-2 hover:bg-gray-100 dark:hover:bg-gray-700 border-gray-100 dark:border-gray-700" >
                <div>
                    <a v-if="notification.notification_type == 'message'" >
                        <strong>{{ notification.created_by }}</strong> sent you a message
                        <small>{{ notification.created_at }}</small>
                    </a>
                    <a v-if="notification.notification_type == 'follower'" >
                        <strong>{{ notification.created_by }}</strong> started following you
                        <small>{{ notification.created_at }}</small>
                    </a>
                    <a v-if="notification.notification_type == 'like'" >
                        <strong>{{ notification.created_by }}</strong> liked a tweek you made
                        <small>{{ notification.created_at }}</small>
                    </a>
                    <a v-if="notification.notification_type == 'dislike'">
                        <strong>{{ notification.created_by }}</strong> liked a tweek you made
                        <small>{{ notification.created_at }}</small>
                    </a>
                    <a v-if="notification.notification_type == 'mention'">
                        <strong>{{ notification.created_by }}</strong> mentioned you in a tweek
                        <small>{{ notification.created_at }}</small>
                    </a>
                </div>
            </div>
        </div>  
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useStore } from 'vuex'

const store = useStore();

const notifications = ref([]);

function getNotifications(){
    axios.get(`/api/notifications/${store.state.user_id}`,) 
    .then(response => {
        notifications.value = response.data;
    }).catch(error => {
        console.log('error' + error)
    })
}

onMounted(() => {
    getNotifications();
})

</script>