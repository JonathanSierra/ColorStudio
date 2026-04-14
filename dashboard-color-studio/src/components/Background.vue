<template>
    <div class="background">
        <div class="contenedor-glassmorphism">
            <slot> </slot>
        </div>
    </div>
</template>
<style scoped>
.background {
    background-image: url(../assets/images/salon_background_premium_pink_1774203711295.png);
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
    background-attachment: fixed;
    display: flex;
    width: 100dvw;
    background-color: rgb(255, 255, 255);
    min-height: 100dvh;
}

.contenedor-glassmorphism {
    background: var(--bg-glass);
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100dvw;
    min-height: 100dvh;
    backdrop-filter: blur(8px);
}
</style>
