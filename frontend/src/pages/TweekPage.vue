<template>
    <div class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0">
        <Tweek :tweek="tweeks" :key="id"/>
    </div>
</template>

<script setup>
import axios from 'axios'
import Tweek from '../components/Tweek.vue';
import { ref, onMounted } from 'vue';

const props = defineProps(['id']); 
const tweeks = ref([]);

async function getTweek(){
    await axios.get(`api/tweek/${props.id}`) 
    .then(response => {
        tweeks.value = response.data.tweek
    }).catch(error => {
        console.log('error' + error)
    })
}

onMounted(async () => {
    await getTweek();
});
</script>

