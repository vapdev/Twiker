<template>
  <div
    class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0"
  >
    <DefaultHeader :mainText="'Conversas'" />
    <div class="flex flex-col h-full w-full">
      <ChatBox :user_id="id"></ChatBox>
    </div>
  </div>
</template>

<script setup>
import DefaultHeader from "../components/DefaultHeader.vue";
import ChatBox from "../components/ChatBox.vue";

const props = defineProps(["id"]);
</script>
