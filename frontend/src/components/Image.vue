<template>
    <div>
        <input type="file" @change="uploadImage"/>
        <img v-if="imageUrl" :src="imageUrl"/>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'

const imageUrl  = ref('');

async function uploadImage(event){
    const file = event.target.files[0];
    const formData = new FormData();
    formData.append('file', file);
    await axios.post('/api/upload_image/', formData)
    .then(response => {
        imageUrl.value = response.data['image_url']
    })
    .catch(error => {
        console.log('error' + error)
    })
}
</script>