<template>
  <div
    class="sticky max-[600px]:fixed max-[600px]:bottom-0 min-[600px]:top-0 left-0 px-2 h-screen max-[600px]:h-fit max-[600px]:w-screen bg-white dark:bg-dark max-[600px]:border-t-2 border-gray-100 dark:border-gray-700"
  >
    <div
      class="flex flex-col min-[600px]:h-full max-[600px]:flex-row justify-between"
    >
      <div class="flex flex-col justify-center">
        <form method="get" action="" class="m-0">
          <div
            class="flex flex-row p-2 my-2 max-[600px]:my-0 border-solid border-2 border-gray-100 dark:border-gray-700 w-[200px] rounded-full"
          >
            <div>
              <input
                class="text-sm h-fit w-full outline-none bg-white dark:bg-dark"
                type="text"
                name="query"
                placeholder="Search"
              />
            </div>
            <div>
              <button><i class="p-1 fa-solid fa-magnifying-glass"></i></button>
            </div>
          </div>
        </form>
      </div>
      <div class="relative w-full max-[600px]:w-60" @click="toggle">
        <div
          class="flex justify-between w-full hover:bg-gray-200 dark:hover:bg-gray-700 hover:rounded-full"
        >
          <div class="flex p-1">
            <Avatar :avatar_url="userStore.avatar" />
            <h1 class="ml-1 font-semibold">{{ userStore.username }}</h1>
          </div>
          <div class="flex m-3">
            <i class="m-auto text-xl fa-solid fa-bars"></i>
          </div>
        </div>
        <transition
          enter-active-class="transition ease-out duration-100"
          enter-from-class="transform opacity-0 scale-95"
          enter-to-class="transform opacity-100 scale-100"
          leave-active-class="transition ease-in duration-75"
          leave-from-class="transform opacity-100 scale-100"
          leave-to-class="transform opacity-0 scale-95"
        >
          <div
            id="rSidebar_menu"
            v-show="show"
            class="absolute w-48 h-fit flex flex-col bottom-16 right-2 min-w-max bg-white dark:bg-dark shadow-3 dark:shadow-[0_0px_5px_2px_rgba(255,255,255,0.2)] rounded-md"
          >
            <div class="flex hover:bg-gray-200 dark:hover:bg-gray-700">
              <button class="flex font-semibold text-lg p-1" @click="toggleDarkMode()">
                <div class="flex w-11 h-11">
                  <i class="text-xl m-auto fa-solid" :class="darkmode ? 'fa-sun' : 'fa-moon'"></i>
                </div>
                <span class="m-auto mx-3"> {{
                  darkmode ? "Light Mode" : "Dark Mode"
                }} </span>
              </button>
            </div>
            <div class="flex hover:bg-gray-200 dark:hover:bg-gray-700">
              <router-link to="/edit" class="flex font-semibold text-lg p-1">
                <div class="flex w-11 h-11">
                  <i class="text-lg m-auto fa-solid fa-user-pen"></i>
                </div>
                <span class="m-auto mx-3"> Editar Profile </span>
              </router-link>
            </div>
            <div
              class="flex hover:bg-gray-200 text-red-500 dark:hover:bg-gray-700"
            >
              <router-link to="/logout" class="flex font-semibold text-lg p-1">
                <div class="flex w-11 h-11">
                  <i
                    class="text-xl m-auto rotate-180 fa-solid fa-right-from-bracket"
                  ></i>
                </div>
                <span class="m-auto mx-3"> Logout </span>
              </router-link>
            </div>
          </div>
        </transition>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useUserStore } from "../store/UserStore.js";
import Avatar from "./Avatar.vue";

const expiryDate = new Date();
expiryDate.setTime(expiryDate.getTime() + 3 * 24 * 60 * 60 * 1000);

const userStore = useUserStore();

let show = ref(false);

const darkmode = ref(false);

function toggleDarkMode(){
  axios
    .post(`/api/darkmode/`, {
      user_id : userStore.user_id,
    })
    .then((response) => {
      darkmode.value = response.data.dark_mode
      if (darkmode.value == true) {
        document.documentElement.classList.add("dark");
        document.cookie = "dark_mode=true; expires=" + expiryDate.toUTCString() + "; path=/";
      } else {
        document.documentElement.classList.remove("dark");
        document.cookie = "dark_mode=false; expires=" + expiryDate.toUTCString() + "; path=/";
      }
    })
    .catch((error) => {
      console.log("error" + error);
    });
}

function toggle() {
  show.value = !show.value;
}
</script>
