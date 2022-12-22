<script setup>
import rSideBar from '../components/rSideBar.vue';
import lSideBar from '../components/lSideBar.vue';
import Users from '../components/Users.vue';
</script>
<template>
    <div class="flex flex-row max-[600px]:flex-col w-full justify-center bg-white dark:bg-slate-900 dark:text-gray-300 text-black">
        <aside class="flex w-full max-[600px]:w-fit justify-end max-[600px]:sticky max-[600px]:top-0 max-[600px]:left-0">
        <lSideBar />
        </aside>
        <main class="flex max-w-2xl w-full shrink-0  max-[720px]:max-w-[600px] ">
        <Users />
        </main>
        <aside class="flex w-full">
        <rSideBar />
        </aside>
    </div>
</template>