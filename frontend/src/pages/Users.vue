<template>
  <div
    class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0 max-[600px]:mb-14">
    <DefaultHeader :mainText="'Todos Usuários'" :sideText="'Usuários: ' + users.length" />
    <div class="flex flex-col justify-center">
      <form method="GET" action="" class="m-0" @submit.prevent="getUsers">
        <div
          class="flex ml-2 flex-row p-2 my-2 max-[600px]:my-0 border-solid border-2 border-gray-100 dark:border-gray-700 w-[200px] rounded-full">
          <input class="text-sm h-fit w-full outline-none bg-white dark:bg-dark" type="text" name="query"
            v-model="searchQuery" placeholder="Search" />
          <button><i class="p-1 fa-solid fa-magnifying-glass"></i></button>
        </div>
        <div class="mb-2">
            <select v-model="selectedOption" @change="getUsers()">
              <option value="0">Ordem alfabética</option>
              <option value="1">Mais Seguidos</option>
              <option value="2">Mais Seguindo</option>
            </select>
          </div>
      </form>
    </div>
    <router-link :to="`/profile/${user.username}`" v-for="user in users"
      class="flex flex-row h-fit w-full p-2 pt-3 pl-3 border-solid border-b-2 hover:bg-gray-100 dark:hover:bg-gray-700 border-gray-100 dark:border-gray-700">
      <Avatar :avatar_url="user.avatar" class="mr-3" />
      <div class="flex flex-col">
        <div class="flex">
          <div class="font-bold">{{ user.username }}</div>
        </div>
        <div class="flex">
          <a>Seguidores: {{ user.followed_by }}</a>
        </div>
        <div class="flex">
          <a>Seguindo: {{ user.following }}</a>
        </div>
      </div>
    </router-link>
    <LoadingSpinner v-if="isLoading" :size="8" class="mt-5" />
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import Avatar from "../components/Avatar.vue";
import LoadingSpinner from "../components/LoadingSpinner.vue";
import DefaultHeader from "../components/DefaultHeader.vue";

const users = ref([]);
const isLoading = ref(true);
const searchQuery = ref('');
const selectedOption = ref(0);
async function getUsers() {
  isLoading.value = true;
  await axios
    .get(`/api/users/?query=${searchQuery.value}&order_by=${selectedOption.value}`)
    .then((response) => {
      users.value = response.data;
    })
    .catch((error) => {
      console.log("error" + error);
    });
  isLoading.value = false;
}
onMounted(() => {
  getUsers();
});
</script>
