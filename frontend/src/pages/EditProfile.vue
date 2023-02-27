<template>
  <div
    class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0"
  >
    <DefaultHeader :mainText="'Editar Perfil'" />
    <div
      class="flex flex-col p-2 border-b-2 border-gray-100 dark:border-gray-700"
    >
      <div>
        <Avatar :avatar_url="userStore.avatar" />
      </div>
      <div class="m-8">
        <div @click.prevent="selectImage()" class="flex">
          <button class=""><i class="p-1 fa-regular fa-image"></i></button>
        </div>
        <img v-if="selectedImageUrl" :src="selectedImageUrl" />
        <div @click.prevent="selectBio()" class="mt-4">
          <label class="font-semibold">Biografia:</label>
          <div
            class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0"
          >
            <div class="flex w-full py-2">
              <textarea
                @input="textAreaAdjust($event.target)"
                id="textarea"
                :placeholder="text"
                class="text-xl resize-none overflow-hidden w-full h-8 break-all outline-none pl-1.5 pr-6 bg-white dark:bg-dark"
                type="text"
                v-model="selectedBiography"
              >
              </textarea>
            </div>
          </div>
        </div>
        <br>
      </div>
      </div>
      <div class="flex justify-end mt-4">
      <div class="flex justify-end">
        <button
          @click="uploadImage()"
          class="p-1 rounded-xl bg-green-400 hover:text-white"
        >
          Save changes
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import DefaultHeader from "../components/DefaultHeader.vue";
import Avatar from "../components/Avatar.vue";
import axios from "axios";
import { ref } from "vue";
import { useUserStore } from "../store/UserStore";
import NewTextBox from "../components/NewTextBox.vue";

const userStore = useUserStore();

const selectedImageUrl = ref("");
const image = ref(null);
const selectedBiography = ref(userStore.biography)
function selectImage() {
  let input = document.createElement("input");
  input.type = "file";
  input.accept = "image/*";
  input.onchange = (e) => {
    image.value = e.target.files[0];
    selectedImageUrl.value = URL.createObjectURL(image.value);
  };
  input.click();
}

function uploadImage(event) {
  let formData = new FormData();
  if (image.value) {
    formData.append("file", image.value);
  }
  if (selectedBiography.value) {
    formData.append("bio", selectedBiography.value);
  }
  axios.post("/api/update_avatar/", formData);
}

</script>
