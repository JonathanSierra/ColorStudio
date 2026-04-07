<script setup></script>

<template>
    <div class="card">
        <header class="card-header">
            <slot name="header-content"></slot>
        </header>
        <slot></slot>
        <footer class="card-footer" v-if="$slots['footer-content']">
            <slot name="footer-content"></slot>
        </footer>
    </div>
</template>

<style scoped>
.card {
    display: flex;
    background-color: rgb(255, 255, 255);
    padding: 0;
    flex-direction: column;
    border-radius: 15px;
    box-shadow: 5px 5px 10px rgb(228, 238, 246);
}

.card-header {
    width: 100%;
    height: 3rem;
    padding: 5px 0;
    background-color: rgb(255, 255, 255);
    border-bottom: 2px solid rgb(228, 238, 246);
    border-radius: 15px 15px 0 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.card-footer {
    background-color: white;
    border-top: 2px solid rgb(228, 238, 246);
    border-radius: 0 0 10px 10px;
    padding: 5px;
}
</style>
