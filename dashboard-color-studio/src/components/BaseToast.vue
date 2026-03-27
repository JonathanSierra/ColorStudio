<script setup>
const props = defineProps(['tipo']);
</script>
<template>
    <div class="toast" :class="tipo">
        <slot name="toastContent"></slot>
    </div>
</template>
<style scoped>
/*Estilos en style.css*/
</style>
