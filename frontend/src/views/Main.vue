<template>
  <div
    class="flex justify-center max-[600px]:flex-col max-[600px]:min-h-full w-full bg-white dark:bg-dark text-black dark:text-gray-300"
  >
    <aside
      class="flex max-[600px]:w-fit justify-end max-[600px]:sticky max-[600px]:top-0 max-[600px]:left-0 z-50"
    >
      <lSideBar />
    </aside>
    <main
      class="flex max-w-2xl grow max-[600px]:min-h-full max-[720px]:max-w-[600px]"
    >
      <router-view :key="$route.params.id || $route.params" />
    </main>
    <aside class="flex">
      <router-view name="right" />
    </aside>
  </div>
</template>

<script setup>
import axios from "axios";
import lSideBar from "../components/lSideBar.vue";
import { useUserStore } from "../store/UserStore.js";

const userStore = useUserStore();

const expiryDate = new Date();
expiryDate.setTime(expiryDate.getTime() + 3 * 24 * 60 * 60 * 1000);

async function getAuthenticatedUser() {
  await axios
    .get("/api/auth_user/")
    .then((response) => {
      userStore.setUsername(response.data.username);
      userStore.setUserId(response.data.id);
      userStore.setAvatar(response.data.avatar);
      document.cookie = `username=${
        response.data.username
      }; expires=${expiryDate.toUTCString()}; path=/`;
      document.cookie = `user_id=${
        response.data.id
      }; expires=${expiryDate.toUTCString()}; path=/`;
    })
    .catch((error) => {
      console.log(error);
    });
}

getAuthenticatedUser();
</script>
