<template>
    <div class="flex min-w-full">
        <div id="feedapp"
            class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0">
            <div
                class="min-[600px]:sticky p-3 bg-white dark:bg-slate-900 top-0 min-[600px]:opacity-90 w-full h-fit text-2xl">
                <a href="">
                    <span class="opacity-100 font-semibold">Página inicial</span>
                </a>
            </div>
            <div class="flex h-30 w-full pt-3 pl-3 border-solid border-b-2 border-gray-100 dark:border-gray-700">
                <div class="flex w-14 h-full pt-1">
                    <img class="rounded-full h-12 w-12">
                </div>
                <div class="flex flex-col w-full pl-1">
                    <form>
                        <div class="flex w-full py-5">
                            <textarea placeholder="What you tweeking bro..."
                                class="text-xl resize-none h-fit w-full outline-none bg-white dark:bg-slate-900"
                                type="text"></textarea>
                        </div>
                        <div class="flex border-solid border-t-2 border-gray-100 dark:border-gray-700 w-full">
                            <div class="flex my-2 w-full">
                                <div class="flex justify-between w-full">
                                    <div class="flex">
                                        <button class=""><i class="p-1 fa-regular fa-image"></i></button>
                                    </div>
                                    <div class="flex">
                                        <button id="submit-tweet" type="submit"
                                            class="bg-green-400 rounded-full text-white font-bold mx-3 px-5 py-2">Submit</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
            <div
                class="flex h-fit w-full px-3 border-solid border-b-2 hover:bg-gray-100 dark:hover:bg-gray-700 border-gray-100 dark:border-gray-700">
                <div class="flex flex-col w-full">
                    <!-- <div v-if="tweek.retweek" class="flex mb-2">
                        <span class="flex font-semibold">[[ tweek.tweeker_name + ' compartilhou']]</span>
                    </div> -->
                    <div class="flex h-3"></div>
                    <div class="flex">
                        <div class="flex w-14 h-full pr-2">
                            <img class="rounded-full h-12 w-12">
                        </div>
                        <div class="flex flex-col w-full pb-3">
                            <div>
                                <span class="font-semibold text-lg">
                                    Fabio
                                </span>
                                <span class="ml-2">
                                    10:30
                                </span>
                            </div>
                            <span class="flex text-xl break-all">Este é o tweek meu parceiro</span>
                            <div class="flex flex-row justify-between w-2/3 mt-3">
                                <div class="flex">
                                    <div class="w-8 h-8 p-1 text-center hover:bg-yellow-200 hover:rounded-full">
                                        <i class="fa-regular fa-comment-dots"></i>
                                    </div>
                                    <span class="pt-1"></span>
                                </div>
                                <div class="flex">
                                    <div class="w-8 h-8 p-1 text-center hover:bg-blue-300 hover:rounded-full">
                                        <i class="fa-solid fa-retweet"></i>
                                    </div>
                                    <span class="pt-1">14</span>
                                </div>
                                <div class="flex">
                                    <div class="flex mx-2">
                                        <div class="w-8 h-8 p-1 text-center hover:bg-green-200 hover:rounded-full">
                                            <i class="fa-regular fa-thumbs-up"></i>
                                        </div>
                                        <span class="pt-1">35</span>
                                    </div>
                                    <div class="flex mx-2">
                                        <div class="w-8 h-8 p-1 text-center hover:bg-red-200 hover:rounded-full">
                                            <i class="fa-regular fa-thumbs-down"></i>
                                        </div>
                                        <span class="pt-1">21</span>
                                    </div>
                                </div>
                            </div>
                            <!-- <div> -->
                            <!-- <a href="#"><p class="text-md mt-2 text-blue-300">Ver tweek original</p></a> -->
                            <!-- </div> -->
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>