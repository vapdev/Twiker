<template>
  <div
    class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0 max-[600px]:mb-14"
  >
    <DefaultHeader :mainText="'Notificações'" />
    <div
      v-for="notification in notifications"
      id="notificationapp"
      class="flex flex-col"
    >
      <div
        class="flex flex-row h-fit w-full p-4 pt-3 pl-3 border-solid border-b-2 hover:bg-gray-100 dark:hover:bg-gray-700 border-gray-100 dark:border-gray-700"
      >
        <div>
          <a v-if="notification.notification_type == 'message'">
            <strong>{{ notification.created_by_username }}</strong> te mandou
            uma mensagem
            <small>{{ formatted_time(notification.created_at) }}</small>
          </a>
          <a v-if="notification.notification_type == 'follower'">
            <strong>{{ notification.created_by_username }}</strong> começou a te
            seguir
            <small>{{ formatted_time(notification.created_at) }}</small>
          </a>
          <a v-if="notification.notification_type == 'like'">
            <strong>{{ notification.created_by_username }}</strong> curtiu um
            tweek que você fez
            <small>{{ formatted_time(notification.created_at) }}</small>
          </a>
          <a v-if="notification.notification_type == 'dislike'">
            <strong>{{ notification.created_by_username }}</strong> não curtiu
            um tweek que você fez
            <small>{{ formatted_time(notification.created_at) }}</small>
          </a>
          <a v-if="notification.notification_type == 'mention'">
            <strong>{{ notification.created_by_username }}</strong> mencionou
            você em um tweek
            <small>{{ formatted_time(notification.created_at) }}</small>
          </a>
        </div>
      </div>
    </div>
    <LoadingSpinner v-if="isLoading" :size="8" class="mt-5" />
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { formatted_time } from "../utils/my-utils.js";
import LoadingSpinner from "../components/LoadingSpinner.vue";
import DefaultHeader from "../components/DefaultHeader.vue";

const notifications = ref([]);
const isLoading = ref(true);

const cookie_user_id = document.cookie
  .split("; ")
  .find((row) => row.startsWith("user_id="))
  ?.split("=")[1];

async function getNotifications() {
  isLoading.value = true;
  await axios
    .get(`/api/notifications/${cookie_user_id}`)
    .then((response) => {
      notifications.value = response.data;
    })
    .catch((error) => {
      console.log("error" + error);
    });
  isLoading.value = false;
}

onMounted(async () => {
  await getNotifications();
});
</script>
