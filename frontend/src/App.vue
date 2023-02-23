<template>
  <div class="bg-white dark:bg-dark text-black dark:text-gray-300">
    <router-view />
  </div>
</template>

<script setup>
import axios from "axios";
import { useRouter, useRoute } from "vue-router";
import { useUserStore } from "../src/store/UserStore.js";

const userStore = useUserStore();

userStore.initializeStore();

const router = useRouter();
const route = useRoute();

const token = userStore.token;

function verifyToken() {
  if (token) {
    axios.defaults.headers.common["Authorization"] = `Token ${token}`;
  } else if (route.name !== "SignUp") {
    axios.defaults.headers.common["Authorization"] = "";
    return router.replace("/login");
  } else {
    return router.replace("/signup");
  }
}

verifyToken();
</script>
