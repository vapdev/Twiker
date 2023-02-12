<script setup>
import lSideBar from '../components/lSideBar.vue';
</script>
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

