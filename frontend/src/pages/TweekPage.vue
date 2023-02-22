<template>
    <div class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0">
        <Tweek v-if="!isLoading" :tweek="tweeks" :key="id"/>
        <LoadingSpinner v-if="isLoading" :size="8" class="mt-5" />
        <NewTextBox v-bind:is-posting="isPosting" @callSubmitTweek="submitTweek" :text="'Tweeke sua resposta'" />
    </div>
    
</template>

<script setup>
import axios from 'axios'
import Tweek from '../components/Tweek.vue';
import { ref, onMounted } from 'vue';
import LoadingSpinner from '../components/LoadingSpinner.vue';
import NewTextBox from '../components/NewTextBox.vue';

const props = defineProps(['id']); 
const tweeks = ref([]);
const isLoading = ref(true);

async function getTweek(){
    isLoading.value = true;
    await axios.get(`api/tweek/${props.id}`) 
    .then(response => {
        tweeks.value = response.data.tweek
    }).catch(error => {
        console.log('error' + error)
    })
    isLoading.value = false;
}

onMounted(async () => {
    await getTweek();
});
</script>

