<template>
    <div
      class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0 max-[600px]:mb-14"
    >
      <DefaultHeader
        :mainText="'Seguidores'"
        :sideText="'Usuários: ' + users.length"
      />
      <router-link
        :to="`/profile/${user.username}`"
        v-for="user in users"
        class="flex flex-row h-fit w-full p-2 pt-3 pl-3 border-solid border-b-2 hover:bg-gray-100 dark:hover:bg-gray-700 border-gray-100 dark:border-gray-700"
      >
        <Avatar :avatar_url="user.avatar" class="mr-3" />
        <div class="flex flex-col">
          <div class="flex">
            <div class="font-bold">{{ user.username }}</div>
          </div>
          <div class="flex">
            <router-link
            :to="`/followers/${user.username}`"
            >Followers: {{ user.followed_by }}</router-link>
          </div>
          <div class="flex">
            <router-link
            :to="`/following/${user.username}`"
            >Following: {{ user.following }}</router-link>
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
  import { useUserStore } from "../store/UserStore";

  const users = ref([]);
  const isLoading = ref(true);
  const cookie_user_id = document.cookie
  .split("; ")
  .find((row) => row.startsWith("user_id="))
  ?.split("=")[1];
  async function getUsers() {
    isLoading.value = true;
    await axios
      .get(`/api/users/following/${cookie_user_id}`)
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
