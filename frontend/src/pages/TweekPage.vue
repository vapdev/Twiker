<template>
    <Tweek :tweek="tweeks" :key="id"/>
</template>

<script setup>
import Tweek from '../components/Tweek.vue';
import { ref } from 'vue';

const props = defineProps(['id']); 
const tweek = ref([]);

</script>

