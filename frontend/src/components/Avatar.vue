<template>
  <div class="flex shrink-0 w-12 h-full mr-1">
    <img class="rounded-full h-12 w-12" :src="avatar_url" />
  </div>
</template>

<script setup>
import { onMounted } from "vue";

const props = defineProps({
  avatar_url: {
    type: String,
    required: true,
  },
});

onMounted(() => {
  console.log(props.avatar_url);
});
</script>
