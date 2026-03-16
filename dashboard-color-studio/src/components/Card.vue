<script setup>

</script>

<template>
    <div class="card">
        <slot></slot>
    </div>
</template>

<style scoped>
.card{
    display: flex;
    background-color: rgb(255, 255, 255);
    padding: 0;
    flex-direction: column;
    border-radius: 30px;
}
</style>