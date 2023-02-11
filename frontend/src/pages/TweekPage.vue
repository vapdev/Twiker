<template>
    <Tweek :tweek="tweeks" :key="id"/>
</template>

<script>
import Tweek from '../components/Tweek.vue';

export default {
    props: ['id'],
    components: {
        Tweek,
    },
    data() {
        return {
            tweeks: [],
        }
    },
    mounted() {
    },
}
</script>