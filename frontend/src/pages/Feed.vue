<template>
  <div class="flex min-w-full max-[600px]:mb-14">
    <div
      class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0"
    >
      <DefaultHeader :mainText="'Página Inicial'" />
      <NewTextBox
        v-bind:is-posting="isPosting"
        @callSubmitTweek="submitTweek"
        :text="'What you tweeking bro...'"
      />
      <Tweek
        v-for="tweek in tweeks"
        :key="tweek.id"
        :tweek="tweek"
        @callGetTweeks="getTweeks"
      />
      <LoadingSpinner v-if="isLoading" :size="8" class="mt-5" />
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import Tweek from "../components/Tweek.vue";
import { ref, onMounted, defineAsyncComponent } from "vue";
import NewTextBox from "../components/NewTextBox.vue";
import DefaultHeader from "../components/DefaultHeader.vue";
import { useUserStore } from "../store/UserStore";

const userStore = useUserStore();

function textAreaAdjust(element) {
  element.style.height = "32px";
  element.style.height = element.scrollHeight + "px";
}
const LoadingSpinner = defineAsyncComponent(() =>
  import("../components/LoadingSpinner.vue")
);

const tweeks = ref([]);
const isLoading = ref(true);
const isPosting = ref(false);
let currentPage = 1;
let hasNext = false;

let lastTweekId = null; // initialize last tweet ID to null

async function submitTweek(tweek_id = null, body = null, image = null) {
  if (body.length > 0 || tweek_id != null || image.value != null) {
    let tweek = new FormData();
    tweek.append("body", body);
    tweek.append("retweek_id", tweek_id);
    tweek.append("image", image);
    isPosting.value = true;
    try {
      await axios.post("/api/add_tweek/", tweek);
      currentPage = 1;
      lastTweekId = null; // reset last tweet ID to null
      await getTweeks();
    } catch (error) {
      console.log(error);
    }
    isPosting.value = false;
  }
}

async function getTweeks(refresh = false) {
  isLoading.value = true;
  try {
    if (refresh) {
      currentPage = 1;
      lastTweekId = null; // reset last tweet ID to null
    }
    let url = `/api/get_tweeks/?page=${currentPage}`;
    if (lastTweekId) {
      url += `&last_tweek_id=${lastTweekId}`; // add last tweet ID to URL if it exists
    }
    const response = await axios.get(url);
    hasNext = false;
    if (response.data.next) {
      hasNext = true;
    }
    if (lastTweekId) {
      tweeks.value = tweeks.value.concat(response.data.results); // add new tweets to end of existing tweets
    } else {
      tweeks.value = response.data.results; // replace existing tweets with new tweets if no last tweet ID
    }
    if (response.data.results.length > 0) {
      lastTweekId = response.data.results[response.data.results.length - 1].id; // set last tweet ID to ID of last tweet in response
    }
  } catch (error) {
    console.log("error" + error);
  }
  isLoading.value = false;
}
const threshold = 100; // threshold value in pixels
let isGettingTweeks = false;

function handleScroll() {
  const scrollPosition = window.scrollY;
  const windowSize = window.innerHeight;
  const documentHeight = document.documentElement.scrollHeight;
  const visibleBottom = scrollPosition + windowSize;

  if (
    visibleBottom >= documentHeight - threshold &&
    hasNext &&
    !isGettingTweeks
  ) {
    currentPage += 1;
    isGettingTweeks = true;
    getTweeks().then(() => {
      isGettingTweeks = false;
    });
  }
}

onMounted(async () => {
  await getTweeks();
  window.addEventListener("scroll", handleScroll);
});
</script>

<style></style>
