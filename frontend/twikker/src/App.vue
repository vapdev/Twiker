<template>
    <body>
        <div class="flex flex-row max-[600px]:flex-col w-full justify-center bg-white dark:bg-slate-900 text-black dark:text-gray-300">
            <aside class="flex w-full max-[600px]:w-fit justify-end max-[600px]:sticky max-[600px]:top-0 max-[600px]:left-0">
                <Sidebar />
            </aside>
            <main class="flex max-w-2xl w-full shrink-0  max-[720px]:max-w-[600px] ">
                <Feed />
            </main>
            <aside class="flex w-full">
                <RightSidebar />
            </aside>
        </div>
    </body>
</template>

<script setup>
import { RouterView } from 'vue-router';
import Sidebar from './components/Sidebar.vue';
import Feed from './components/Feed.vue';
import RightSidebar from './components/RightSidebar.vue';
</script>

<style>
@import './assets/css/all.css';
</style>
