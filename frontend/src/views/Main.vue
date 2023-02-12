<template>
    <div class="flex justify-center max-[600px]:flex-col max-[600px]:min-h-full w-full bg-white dark:bg-slate-900 text-black dark:text-gray-300">
        <aside class="flex max-[600px]:w-fit justify-end max-[600px]:sticky max-[600px]:top-0 max-[600px]:left-0 z-50">
        <lSideBar />
        </aside>
        <main class="flex max-w-2xl grow max-[600px]:min-h-full max-[720px]:max-w-[600px]">
        <router-view :key="$route.params.id || $route.params" />
        </main>
        <aside class="flex">
        <router-view name="right"/>
        </aside>
    </div>
</template>

<script setup>
import axios from 'axios';
import lSideBar from '../components/lSideBar.vue';
import { useStore } from 'vuex'

const store = useStore();

function getAuthenticatedUser() {
  axios.get('/api/auth_user/')
    .then(response => {
      store.commit('setUsername', response.data.username);
      store.commit('setUserId', response.data.id);
      localStorage.setItem('username', response.data.username);
      localStorage.setItem('user_id', response.data.id);
    })
    .catch(error => {
      console.log(error)
    })
}

getAuthenticatedUser()

</script>
