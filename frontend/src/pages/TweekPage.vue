<template>
    <div class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0">
        <Tweek v-if="!isLoading" :tweek="tweek" :key="id"/>
        <LoadingSpinner v-if="isLoading" :size="8" class="mt-5" />
        <NewTextBox v-bind:is-posting="isPosting" @callSubmitTweek="submitTweek" :text="'Tweeke sua resposta'" />
        <Tweek v-for="tweek in tweeks" :key="tweek.id" :tweek="tweek" @callGetTweeks="getReplies" />
    </div>
    
</template>

<script setup>
import axios from 'axios'
import Tweek from '../components/Tweek.vue';
import { ref, onMounted } from 'vue';
import LoadingSpinner from '../components/LoadingSpinner.vue';
import NewTextBox from '../components/NewTextBox.vue';

const props = defineProps({
    id: {
        type: Number,
        required: true
    }
});

const tweeks = ref([]);
const tweek = ref({});
const isLoading = ref(true);
const isPosting = ref(false);

async function submitTweek(tweek_id = null, body = null, image = null, tweek_type = null) {
    if (body.length > 0 || tweek_id != null || image.value != null) {
        let tweek = new FormData();
        tweek.append('body', body);
        tweek_type = 'reply';
        tweek.append('tweek_type', tweek_type);
        tweek_id = props.id;
        tweek.append('parent_id', tweek_id);
        tweek.append('image', image);
        isPosting.value = true;
        try {
            await axios.post('/api/add_tweek/', tweek);
            await getReplies();
        } catch (error) {
            console.log(error);
        }
        isPosting.value = false;
    }
}

async function getTweek(){
    isLoading.value = true;
    await axios.get(`api/tweek/${props.id}`) 
    .then(response => {
        tweek.value = response.data.tweek
    }).catch(error => {
        console.log('error' + error)
    })
    isLoading.value = false;
}

async function getReplies(){
    isLoading.value = true;
    await axios.get(`api/tweek/${props.id}/replies`) 
    .then(response => {
        tweeks.value = response.data.tweeks
    }).catch(error => {
        console.log('error' + error)
    })
    isLoading.value = false;
}

onMounted(async () => {
    await getTweek();
    await getReplies();
});
</script>

