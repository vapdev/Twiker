<template>
	<div class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0">
		<div
       class="min-[600px]:sticky p-3 bg-white dark:bg-dark top-0 w-full h-fit min-[600px]:opacity-90 text-2xl border-b-2 border-gray-100 dark:border-gray-700 ">
				<a href="">
						<span class="opacity-100 font-semibold">Editar Perfil</span>
				</a>
    </div>
		<div class="flex flex-col p-2 border-b-2 border-gray-100 dark:border-gray-700">
			<div>
				<Avatar :avatar_url="userStore.avatar" />
			</div>
			<div class="m-8">
				<div @click.prevent="selectImage()" class="flex">
						<button class=""><i class="p-1 fa-regular fa-image"></i></button>
				</div>
				<img v-if="selectedImageUrl" :src="selectedImageUrl"/>
			</div>
			<div class="flex justify-end">
				<button @click="uploadImage()" class="p-1 rounded-xl bg-green-400 hover:text-white">
					Save changes
				</button>
			</div>
		</div>
	</div>
</template>

<script setup>
import Avatar from '../components/Avatar.vue'
import axios from 'axios'
import { ref } from 'vue'
import { useUserStore } from '../store/UserStore';

const userStore = useUserStore();

const selectedImageUrl  = ref('');
const image = ref(null);

function selectImage() {
    let input = document.createElement('input');
    input.type = 'file';
    input.accept = 'image/*';
    input.onchange = e => {
        image.value = e.target.files[0];
        selectedImageUrl.value = URL.createObjectURL(image.value);
    }
    input.click();
}

 function uploadImage(event){
    let avatar = new FormData();
    avatar.append('file', image.value);
		if (image.value){
    	axios.post('/api/update_avatar/', avatar)
		}
}
</script>