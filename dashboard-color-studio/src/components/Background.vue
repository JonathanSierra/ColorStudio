<template>
    <div class="background">
        <slot>

        </slot>
    </div>
</template>
<style scoped>
.background {
    background-image: url(../assets/images/interior-design-renderings-3d-rendering-of-luxurious-for-a-beauty-salon_9850621.webp);
    background-repeat: no-repeat;
    background-size: cover;
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