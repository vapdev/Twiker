<template>
    <Tweek :tweek="tweeks" :key="id"/>
</template>

<script>
import Tweek from './Tweek.vue';
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
        console.log("id is: " + this.id)
    },
}
</script>