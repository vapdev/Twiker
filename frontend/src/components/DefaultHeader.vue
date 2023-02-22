<template>
    <div
        class="min-[600px]:sticky p-3 bg-white dark:bg-dark top-0 w-full h-fit min-[600px]:opacity-90 text-2xl border-b-2 border-gray-100 dark:border-gray-700 ">
        <div class="flex justify-between">
            <span class="opacity-100 font-semibold">{{ mainText }}</span>
            <p>{{ sideText }}</p>
        </div>
    </div>
</template>

<script setup>

const props = defineProps({
    mainText: {
        type: String,
        required: true,
    },
    sideText: {
        type: String,
        required: true,
    },
});

</script>