<template>
    <div class="flex-col w-full bg-white dark:bg-dark border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0" id="twikkerprofileapp">
        <div class="border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0">
            <div class="border-gray-100 border-y-2 dark:border-gray-700 pb-3">
                <Image />
                <div>
                    <div class="px-2 pb-1 border-gray-100 border-b-2 dark:border-gray-700 mt-2 mb-5">
                        <h1 class="text-xl">Edit profile</h1>
                    </div>
                    <div class="px-2">
                        <article>
                            <Avatar />
                        </article> 
                        <form method="post" enctype="multipart/form-data" action=".">
                            <!-- {{ form.avatar }} -->
                            <div class="flex justify-end">
                                <div>
                                    <button class="p-1 mt-2 rounded-xl bg-gray-100 text-black hover:bg-gray-500 hover:text-white">Save changes</button>
                                </div>
                            </div>
                        </form>
                    </div>
                    
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import Image from '../components/Image.vue'
import Avatar from '../components/Avatar.vue'
</script>