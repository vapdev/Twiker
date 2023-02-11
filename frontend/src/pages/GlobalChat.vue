<script setup>
import ChatBox from '../components/ChatBox.vue';
</script>

<template>
    <div class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0">
        <div class="min-[600px]:sticky p-3 bg-white dark:bg-slate-900 top-0 w-full h-fit min-[600px]:opacity-90 text-2xl border-b-2 border-gray-700 ">
            <a href="{% url 'global' %}">
                <span class="opacity-100 font-semibold">Global chat</span>
            </a>
        </div>
        <div class="flex flex-col h-full w-full">
            <ChatBox conversation_id="0"></ChatBox>
        </div>
    </div>
</template>
