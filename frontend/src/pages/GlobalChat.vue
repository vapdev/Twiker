<template>
  <div
    class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0"
  >
    <DefaultHeader :mainText="'Chat Global'" />
    <div class="flex flex-col h-full w-full">
      <ChatBox></ChatBox>
    </div>
  </div>
</template>

<script setup>
import ChatBox from "../components/ChatBox.vue";
import DefaultHeader from "../components/DefaultHeader.vue";
</script>
