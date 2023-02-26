<template>
  <div
    class="flex h-30 w-full pt-3 pl-3 border-solid border-b-2 border-gray-100 dark:border-gray-700"
  >
    <Avatar :avatar_url="userStore.avatar" />
    <div class="flex flex-col w-full pl-1">
      <form>
        <div class="flex w-full py-2">
          <textarea
            @input="textAreaAdjust($event.target)"
            id="textarea"
            :placeholder="text"
            class="text-xl resize-none overflow-hidden w-full h-8 break-all outline-none pl-1.5 pr-6 bg-white dark:bg-dark"
            type="text"
            v-model="body"
          >
          </textarea>
        </div>
        <div v-if="selectedImageUrl">
          <div class="mr-10 mb-4 mt-2">
            <img :src="selectedImageUrl" class="rounded-xl"/>
          </div>
        </div>
        <div
          class="flex border-solid border-t-2 -mb-1.5 border-gray-100 dark:border-gray-700 w-full"
        >
          <div class="flex mt-2 w-full">
            <div class="flex justify-between h-10 w-full">
              <div @click.prevent="selectImage()" class="flex">
                <button class="rounded-full h-10 w-10 hover:bg-gray-800">
                  <i class="p-1 fa-regular fa-image"></i>
                </button>
              </div>
              <div class="flex">
                <LoadingSpinner v-if="isPosting" :size="8" class="py-1.5" />
                <button
                  @click.prevent="callSubmitTweek()"
                  id="submit-tweek"
                  type="submit"
                  class="bg-green-400 rounded-full text-white font-bold mx-3 px-5 py-2"
                >
                  Enviar
                </button>
              </div>
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from "vue";
import Avatar from "../components/Avatar.vue";
import { useUserStore } from "../store/UserStore";
import LoadingSpinner from "../components/LoadingSpinner.vue";
const userStore = useUserStore();

const body = ref("");
const image = ref(null);
const selectedImageUrl = ref(null);

const emit = defineEmits(["callSubmitTweek"]);

function textAreaAdjust(element) {
  element.style.height = "32px";
  element.style.height = element.scrollHeight + "px";
}

const props = defineProps({
  isPosting: {
    type: Boolean,
    required: true,
  },
  text: {
    type: String,
    required: true,
  },
});

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

async function callSubmitTweek() {
  emit("callSubmitTweek", null, body.value, image.value);
  body.value = "";
  image.value = null;
  selectedImageUrl.value = null;
}

document.body.addEventListener("keydown", function (e) {
  if (!(e.keyCode == 13 && (e.metaKey || e.ctrlKey))) return;
  let target = e.target;
  let submit_button = document.querySelector("#submit-tweek");
  if (target.form && body.value != "") {
    submit_button.click();
  }
});
</script>
