<template>
  <router-link
    :to="`/tweek/${tweek.id}`"
    class="flex w-full break-all p-3 border-solid border-b-2 border-gray-100 dark:border-gray-700"
  >
    <div class="flex flex-col w-full">
      <div v-if="tweek.retweek" class="flex items-center mb-1">
        <i class="text-blue-600 fa-solid fa-retweet mr-2"></i>
        <span class="flex text-sm font-bold opacity-80">
          {{ tweek.tweeker_name + " compartilhou" }}
        </span>
      </div>
      <a
        v-if="tweek.comment_from"
        class="flex items-center mb-1"
        @click.prevent.stop="$router.replace(`/tweek/${tweek.comment_from}`)"
      >
        <i class="text-yellow-400 fa-solid fa-comment mr-2"></i>
        <span class="flex text-sm font-bold opacity-80">
          <span
            >em resposta ao <span class="text-blue-400">tweek</span> de
            {{ tweek.reply_parent_tweeker_name }}
          </span>
        </span>
      </a>
      <div class="flex">
        <div class="flex w-14 h-full mr-2">
          <div
          @click.prevent="
          $router.replace(`/profile/${tweek.tweeker_name}`)"
          >
            <Avatar :avatar_url="tweek.avatar_url" class="pt-1.5" />
          </div>
        </div>
        <div class="flex flex-col w-full">
          <div class="flex justify-between">
            <div>
              <span
                @click.prevent="
                  $router.replace(`/profile/${tweek.tweeker_name}`)
                "
                class="font-semibold text-lg"
              >
                {{ tweek.tweeker_name }}
              </span>
              <span class="ml-2">
                {{ formatted_time(tweek.created_at) }}
              </span>
            </div>
            <div class="relative flex items-center">
              <div
                @click.prevent="toggle"
                class="flex w-8 h-8 hover:bg-white hover:rounded-full hover:bg-opacity-20"
              >
                <i class="m-auto text-xl fa-solid fa-ellipsis"></i>
              </div>
              <transition
                enter-active-class="transition ease-out duration-100"
                enter-from-class="transform opacity-0 scale-95"
                enter-to-class="transform opacity-100 scale-100"
                leave-active-class="transition ease-in duration-75"
                leave-from-class="transform opacity-100 scale-100"
                leave-to-class="transform opacity-0 scale-95"
              >
                <div
                  v-if="tweek.created_by == cookie_user_id"
                  id="tweek_menu"
                  v-show="show"
                  class="absolute flex flex-col right-10 min-w-max bg-white dark:bg-dark shadow-md dark:shadow-[0px_4px_10px_1px_rgba(255,255,255,0.1)] rounded-md"
                >
                  <div
                    @click.prevent.stop="deleteTweek(tweek.id)"
                    class="p-2 hover:bg-white hover:rounded-md hover:bg-opacity-20"
                  >
                    <i class="text-red-400 fa-solid fa-trash mr-2"></i>
                    <span class="break-normal text-red-400 font-semibold"
                      >Deletar tweek</span
                    >
                  </div>
                </div>
              </transition>
            </div>
          </div>
          <div class="flex flex-col">
            <div>
              <span class="flex text-xl break-word cursor-text pr-4">
                {{ tweek.body }}
              </span>
            </div>
            <div
              v-if="tweek.retweek"
              @click.prevent.stop="
                $router.replace(`/tweek/${tweek.retweek_id}`)
              "
              class="flex-col px-2 py-1 mt-1.5 rounded-lg border-2 border-gray-100 dark:border-gray-700"
            >
              <div class="flex">
                <div class="flex w-6 mr-4">
                  <Avatar
                    :avatar_url="tweek.retweek_avatar_url"
                    class="h-6 scale-50"
                  />
                </div>
                <span class="font-semibold text-lg">{{
                  tweek.retweek_tweeker_name
                }}</span>
                <span class="ml-2 pt-0.5">{{
                  formatted_time(tweek.retweek_created_at)
                }}</span>
              </div>
              <div class="flex ml-3 mt-2">
                <span class="flex text-lg break-word cursor-text pr-4">
                  {{ tweek.retweek_body }}
                </span>
              </div>
              <div v-if="tweek.retweek_image" class="pt-4 pb-2 pr-8">
                <img :src="tweek.retweek_image" class="w-full rounded-xl" />
              </div>
            </div>
          </div>
          <div v-if="tweek.image" class="pt-4 pb-2 pr-8">
            <img :src="tweek.image" class="w-full rounded-xl" />
          </div>
          <div
            v-if="!tweek.is_retweek"
            class="flex flex-row justify-between w-2/3 mt-1"
          >
            <div class="flex items-center">
              <div
                class="flex w-8 h-8 hover:bg-yellow-200 hover:rounded-full cursor-pointer"
              >
                <i class="m-auto fa-regular fa-comment-dots"></i>
              </div>
              <span>{{ tweek.replies_count }}</span>
            </div>
            <div class="flex items-center">
              <div
                @click.prevent.stop="toggleRetweek(tweek)"
                class="flex w-8 h-8 hover:bg-blue-300 hover:rounded-full cursor-pointer"
              >
                <i
                  :id="'retweek-' + tweek.id"
                  :class="
                    tweek.is_retweeked
                      ? 'text-blue-600 fa-solid fa-retweet'
                      : 'fa-solid fa-retweet'
                  "
                  class="m-auto"
                ></i>
              </div>
              <span>{{ tweek.retweek_count }}</span>
            </div>
            <div class="flex items-center">
              <div
                @click.prevent="toggleLike(tweek)"
                class="flex w-8 h-8 p-1 mx-1 text-center hover:bg-green-200 hover:rounded-full cursor-pointer"
              >
                <i
                  :id="'like-' + tweek.id"
                  :class="
                    !tweek.is_liked
                      ? 'fa-regular fa-thumbs-up'
                      : 'text-green-300 fa-solid fa-thumbs-up'
                  "
                  class="m-auto"
                ></i>
              </div>
              <span :id="'likes-' + tweek.id">{{ tweek.likes_count }}</span>
              <div
                @click.prevent.stop="toggleDislike(tweek)"
                class="flex w-8 h-8 p-1 mx-1 text-center hover:bg-red-200 hover:rounded-full cursor-pointer"
              >
                <i
                  :id="'dislike-' + tweek.id"
                  :class="
                    !tweek.is_disliked
                      ? 'fa-regular fa-thumbs-down'
                      : 'text-red-300 fa-solid fa-thumbs-down'
                  "
                  class="m-auto"
                ></i>
              </div>
              <span :id="'dislikes-' + tweek.id">{{
                tweek.dislikes_count
              }}</span>
            </div>
          </div>
          <div v-if="tweek.retweek">
            <div
              @click.prevent.stop="
                $router.replace(`/tweek/${tweek.retweek_id}`)
              "
            >
              <p
                class="text-md mt-2 text-blue-300 w-fit hover:text-blue-100 rounded-xl"
              >
                Ver tweek original
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </router-link>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";
import { formatted_time } from "../utils/my-utils.js";
import Avatar from "../components/Avatar.vue";

const props = defineProps({
  tweek: Object,
});

const emit = defineEmits(["callGetTweeks"]);

const cookie_user_id = document.cookie
  .split("; ")
  .find((row) => row.startsWith("user_id="))
  ?.split("=")[1];

const show = ref(false);
const body = ref("");
const tweeker = "tweeker_username";
const created_at = "Now";
const avatar = "tweeker_avatar";

function toggle() {
  show.value = !show.value;
}

async function submitTweek(tweek_id = null, tweek_type = "tweek") {
  if (body.value.length > 0 || tweek_id != null) {
    let tweek = new FormData();
    tweek.append("body", body.value);
    tweek.append("tweeker", tweeker);
    tweek.append("created_at", created_at);
    tweek.append("avatar", avatar);
    tweek.append("parent_id", tweek_id);
    tweek.append("tweek_type", tweek_type);

    await axios.post("/api/add_tweek/", tweek).catch((error) => {
      console.log(error);
    });
    emit("callGetTweeks", true);
  }
  body.value = "";
}

async function toggleLike(tweek) {
  if (tweek.retweek_id) {
    await axios
      .get(`/api/tweek/${tweek.retweek_id}/`)
      .then((response) => {
        tweek = response.data["tweek"];
      })
      .catch((error) => {
        console.log("error" + error);
      });
  }
  if (tweek.is_disliked) {
    undislikeTweek(tweek);
  }
  if (tweek.is_liked) {
    unlikeTweek(tweek);
  } else {
    likeTweek(tweek);
  }
}
function likeTweek(tweek) {
  tweek.is_liked = true;
  tweek.likes_count += 1;
  let tweek_id = {
    tweek_id: tweek.id,
  };
  axios.post("/api/add_like/", tweek_id).catch((error) => {
    console.log("error" + error);
  });
}
function unlikeTweek(tweek) {
  tweek.is_liked = false;
  tweek.likes_count -= 1;
  var tweek_id = {
    tweek_id: tweek.id,
  };
  axios.post("/api/remove_like/", tweek_id).catch((error) => {
    console.log("error" + error);
  });
}
function toggleRetweek(tweek) {
  if (tweek.is_retweeked) {
    unretweekTweek(tweek.id);
  } else {
    submitTweek(tweek.id, "retweek");
  }
}
async function commentTweek(tweek_id) {
  submitTweek(tweek_id, "comment");
}
async function unretweekTweek(tweek_id) {
  var tweek = {
    tweek_id: tweek_id,
  };
  await axios.post("/api/remove_retweek/", tweek).catch((error) => {
    console.log("error" + error);
  });
  emit("callGetTweeks", true);
}
async function toggleDislike(tweek) {
  if (tweek.retweek_id) {
    await axios
      .get(`/api/tweek/${tweek.retweek_id}/`)
      .then((response) => {
        tweek = response.data["tweek"];
      })
      .catch((error) => {
        console.log("error" + error);
      });
  }
  if (tweek.is_liked) {
    unlikeTweek(tweek);
  }
  if (tweek.is_disliked) {
    undislikeTweek(tweek);
  } else {
    dislikeTweek(tweek);
  }
}
function dislikeTweek(tweek) {
  tweek.is_disliked = true;
  tweek.dislikes_count += 1;
  let tweek_id = {
    tweek_id: tweek.id,
  };
  axios.post("/api/add_dislike/", tweek_id).catch((error) => {
    console.log("error" + error);
  });
}
function undislikeTweek(tweek) {
  tweek.is_disliked = false;
  tweek.dislikes_count -= 1;
  var tweek_id = {
    tweek_id: tweek.id,
  };
  axios.post("/api/remove_dislike/", tweek_id).catch((error) => {
    console.log("error" + error);
  });
}
async function deleteTweek(tweek_id) {
  var tweek = {
    tweek_id: tweek_id,
  };
  await axios.post("/api/delete_tweek/", tweek).catch((error) => {
    console.log("error" + error);
  });
  emit("callGetTweeks", true);
}
</script>
