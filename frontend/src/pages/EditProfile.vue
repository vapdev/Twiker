<template>
  <div class="flex flex-col w-full dark:bg-dark border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0 max-[600px]:mb-14">
    <div id="profile" class="flex flex-col p-6 pb-3 border-solid border-b-2 border-gray-100 dark:border-gray-700">
      <div class="bg-opacity-40">
        <div class="flex w-full justify-between">
          <div class="flex">
            <article>
              <Avatar class="scale-125" :avatar_url="userStore.avatar" />
            </article>
            <div class="font-bold text-lg ml-5">{{ userStore.username }}</div>
          </div>
        </div>
        <div class="mt-4 mb-3">
          <div>
            <label class="font-semibold">Bio:</label>
            <div
              class="flex flex-col w-full dark:border-gray-700 max-[600px]:border-x-0"
            >
              <div class="flex w-full py-2">
                <textarea
                  @input="textAreaAdjust($event.target)"
                  id="textarea"
                  :placeholder="text"
                  class="text-md resize-none border border-gray-500 rounded-lg h-16 p-1 overflow-hidden w-full break-all outline-none pl-1.5 pr-6 bg-white dark:bg-dark"
                  type="text"
                  v-model="bio"
                >
                </textarea>
              </div>
            <label class="mt-6 font-semibold">Foto de perfil:</label>
              <div @click.prevent="selectImage()" class="flex mt-3">
                <div class="w-10 h-10 flex justify-center rounded-full hover:bg-gray-500">
                  <button><i class="p-1 fa-regular fa-image"></i></button>
                </div>
              </div>
              <img v-if="selectedImageUrl" :src="selectedImageUrl" />
            </div>
          </div>
        </div>
        <div class="flex justify-end">
          <div class="flex flex-col ml-4">
            <button @click="editProfile()" class="p-1 rounded-xl bg-green-400 hover:text-white">
              Save changes
            </button>
          </div>
        </div>
      </div>
    </div>
    <LoadingSpinner v-if="isLoading" :size="8" class="mt-5" />
  </div>
</template>


<script setup>
import DefaultHeader from "../components/DefaultHeader.vue";
import Avatar from "../components/Avatar.vue";
import axios from "axios";
import { ref } from "vue";
import { useUserStore } from "../store/UserStore";
import LoadingSpinner from "../components/LoadingSpinner.vue";
import { formatMonthYear } from "../utils/my-utils.js";

const userStore = useUserStore();

const selectedImageUrl = ref("");
const image = ref(null);
const bio = ref(userStore.biography)

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

function editProfile() {
  let formData = new FormData();
  if (image.value) {
    formData.append("avatar", image.value);
  }
  if (bio.value) {
    formData.append("bio", bio.value);
  }
  axios.post("/api/update_profile/", formData)
    .then(() => {
      location.reload();
    })
    .catch((error) => {
      console.error(error);
    });
}


</script>
