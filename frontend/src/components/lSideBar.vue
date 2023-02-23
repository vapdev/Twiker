<template>
  <div
    class="sticky top-0 left-0 px-2 h-screen max-[600px]:h-fit max-[600px]:w-screen bg-white dark:bg-dark max-[600px]:border-b-2 border-gray-100 dark:border-gray-700"
  >
    <div class="flex flex-col max-[600px]:flex-row justify-center">
      <div class="flex py-1 max-[600px]:hidden">
        <router-link
          to="/"
          class="flex justify-center font-semibold p-2 hover:bg-green-200 hover:rounded-full"
        >
          <div class="flex w-11 h-11">
            <i class="text-5xl m-auto fa-solid fa-ankh"></i>
          </div>
        </router-link>
      </div>
      <div class="flex py-1">
        <router-link
          to="/"
          class="flex justify-center font-semibold text-xl max-[600px]:py-1 p-2 hover:bg-gray-200 dark:hover:bg-gray-700 hover:rounded-full"
        >
          <div class="flex w-11 h-11">
            <i class="text-xl m-auto fa-solid fa-house"></i>
          </div>
          <span class="m-auto mx-3 max-[850px]:hidden">Página Inicial</span>
        </router-link>
      </div>
      <div class="flex py-1">
        <router-link
          to="/notifications"
          class="flex font-semibold text-xl max-[600px]:py-1 p-2 hover:bg-gray-200 dark:hover:bg-gray-700 hover:rounded-full"
        >
          <div class="flex w-11 h-11">
            <i class="text-xl m-auto fa-solid fa-bell"></i>
          </div>
          <span id="notifications" class="m-auto mx-3 max-[850px]:hidden"
            >Notificações</span
          >
        </router-link>
      </div>
      <div class="flex py-1">
        <router-link
          to="/users"
          class="flex font-semibold text-xl max-[600px]:py-1 p-2 hover:bg-gray-200 dark:hover:bg-gray-700 hover:rounded-full"
        >
          <div class="flex w-11 h-11">
            <i class="text-xl m-auto fa-solid fa-users"></i>
          </div>
          <span class="m-auto mx-3 max-[850px]:hidden">Todos Usuários</span>
        </router-link>
      </div>
      <div class="flex py-1">
        <router-link
          to="/globalchat"
          class="flex font-semibold text-xl max-[600px]:py-1 p-2 hover:bg-gray-200 dark:hover:bg-gray-700 hover:rounded-full"
          href="{% url 'global' %} "
        >
          <div class="flex w-11 h-11">
            <i class="text-xl m-auto fa-solid fa-earth-americas"></i>
          </div>
          <span class="break-keep m-auto mx-3 max-[850px]:hidden"
            >Chat Global</span
          >
        </router-link>
      </div>
      <div class="flex py-1">
        <router-link
          to="/conversation"
          class="flex font-semibold text-xl max-[600px]:py-1 p-2 hover:bg-gray-200 dark:hover:bg-gray-700 hover:rounded-full"
        >
          <div class="flex w-11 h-11">
            <i class="text-xl m-auto fa-solid fa-comments"></i>
          </div>
          <span class="m-auto mx-3 max-[850px]:hidden">Conversas</span>
        </router-link>
      </div>
      <div class="flex py-1">
        <router-link
          :to="'/profile/' + userStore.username"
          class="flex font-semibold text-xl max-[600px]:py-1 p-2 hover:bg-gray-200 dark:hover:bg-gray-700 hover:rounded-full"
        >
          <div class="flex w-11 h-11">
            <i class="text-xl m-auto fa-solid fa-user"></i>
          </div>
          <span class="m-auto mx-3 max-[850px]:hidden">Perfil</span>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from "../store/UserStore.js";

const userStore = useUserStore();
</script>

<style>
@import "../assets/icons/css/all.css";
</style>
