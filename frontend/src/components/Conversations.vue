<template>
  <div
    class="sticky max-[600px]:fixed max-[600px]:bottom-0 min-[600px]:top-0 min-[600px]:left-0 max-[600px]:right-0 h-screen max-[600px]:h-14 max-[600px]:w-screen w-[216px] bg-white dark:bg-dark max-[600px]:overflow-y-hidden overflow-auto"
  >
    <div
      class="flex flex-col max-[600px]:flex-row h-full max-[600px]:w-screen border-solid border-r-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0 overflow"
    >
      <div
        class="p-3 bg-white dark:bg-dark top-0 w-full h-fit min-[600px]:opacity-95 text-2xl border-solid border-b-2 border-gray-100 dark:border-gray-700 max-[600px]:hidden"
      >
        <span class="opacity-100">Conversas</span>
      </div>
      <LoadingSpinner v-if="isLoading" :size="8" class="mt-5" />
      <div v-for="conversation in conversations" class="flex">
        <a href=""
          @click="goToConversation(conversation.user_id)"
          class="flex h-fit w-full max-[600px]:w-fit p-4 pt-3 pl-3 border-solid min-[600px]:border-b-2 max-[600px]:border hover:bg-gray-100 dark:hover:bg-gray-700 border-gray-100 dark:border-gray-700"
        >
          <Avatar :avatar_url="conversation.avatar" />
          <div>
            <p>{{ conversation.username }}</p>
            <p class="max-lg:hidden">
              {{ formatted_time(conversation.modified_at) }}
            </p>
          </div>
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
import Avatar from "../components/Avatar.vue";
import LoadingSpinner from "../components/LoadingSpinner.vue";
import axios from "axios";
import { formatted_time } from "../utils/my-utils.js";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

const conversations = ref([]);
const isLoading = ref(true);
const router = useRouter();

async function getConversations() {
  isLoading.value = true;
  await axios
    .get(`/api/conversations/`)
    .then((response) => {
      conversations.value = response.data;
    })
    .catch((error) => {
      console.log("error" + error);
    });
  isLoading.value = false;
}
function goToConversation(user_id) {
  router.replace(`/conversation/${user_id}`);
}
onMounted(() => {
  getConversations();
});
</script>
