<template>
    <div class="background">
        <slot>

        </slot>
    </div>
</template>
<style scoped>
.background {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: -1;
    width: 100dvw;
    background-color: rgb(149, 92, 202);
    height: 100dvh;
}
</style>