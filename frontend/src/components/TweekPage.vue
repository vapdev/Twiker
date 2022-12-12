<template>
    <div class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0">
        <div class="min-[600px]:sticky p-3 bg-white dark:bg-slate-900 top-0 w-full h-fit min-[600px]:opacity-95 text-2xl border-solid border-b-2 border-gray-100 dark:border-gray-700">
            <span class="opacity-100">Notificações</span>
        </div>
        <div class="flex h-fit w-full p-3 border-solid border-b-2 hover:bg-gray-100 dark:hover:bg-gray-700 border-gray-100 dark:border-gray-700">
            <div class="flex flex-col w-full">
                <div v-if="tweek.retweek" class="flex items-center mb-1">
                    <i class="text-blue-600 fa-solid fa-retweet mr-2"></i>
                    <span class="flex font-semibold"> {{ tweek.tweeker_name + ' compartilhou' }} </span>
                </div>
                <div class="flex">
                    <div class="flex w-14 h-full mr-2">
                        <img class="rounded-full h-12 w-12" :src="tweek.retweek ? tweek.retweek_avatar_url : tweek.avatar_url">
                    </div>
                    <div class="flex flex-col w-full">
                        <div>
                            <span class="font-semibold text-lg">
                                {{ tweek.retweek ? tweek.retweek_tweeker_name : tweek.tweeker_name }}
                            </span>
                            <span class="ml-2">
                                {{ tweek.retweek ? tweek.retweek_formatted_time : tweek.formatted_time }}
                            </span>
                        </div>
                        <span class="flex text-xl break-all">{{ tweek.retweek ? tweek.retweek_body : tweek.body }}</span>
                        <div v-if="!tweek.is_retweek" class="flex flex-row justify-between w-2/3 mt-1">
                            <div class="flex items-center">
                                <div class="flex w-8 h-8 hover:bg-yellow-200 hover:rounded-full">
                                    <i class="m-auto fa-regular fa-comment-dots"></i>
                                </div>
                                <span>12</span>
                            </div>
                            <div class="flex items-center">
                                <div @click.stop="toggleRetweek(tweek)" class="flex w-8 h-8 hover:bg-blue-300 hover:rounded-full">
                                    <i :id="'retweek-'+tweek.id" :class="tweek.is_retweeked ? 'text-blue-600 fa-solid fa-retweet' : 'fa-solid fa-retweet'" class="m-auto"></i>
                                </div>
                                <span>{{ tweek.retweek_count }}</span>
                            </div>
                            <div class="flex items-center">
                                <div @click.stop="toggleLike(tweek)" class="flex w-8 h-8 p-1 mx-1 text-center hover:bg-green-200 hover:rounded-full">
                                    <i :id="'like-'+tweek.id" :class=" !tweek.is_liked ? 'fa-regular fa-thumbs-up' : 'fa-solid fa-thumbs-up'" class="m-auto"></i>
                                </div>
                                <span :id="'likes-'+tweek.id">{{ tweek.likes_count }}</span>
                                <div @click.stop="toggleDislike(tweek)" class="flex w-8 h-8 p-1 mx-1 text-center hover:bg-red-200 hover:rounded-full">
                                    <i :id="'dislike-'+tweek.id" :class=" !tweek.is_disliked ? 'fa-regular fa-thumbs-down' : 'fa-solid fa-thumbs-down'" class="m-auto"></i>
                                </div>
                                <span  :id="'dislikes-'+tweek.id">{{ tweek.dislikes_count }}</span>
                            </div>
                        </div>
                        <div v-if="tweek.retweek">
                            <div @click.stop="viewTweek(tweek.id)"><p class="text-md mt-2 text-blue-300 w-fit hover:text-blue-100 rounded-xl">Ver tweek original</p></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            tweeks: []
        }
    }
}
</script>