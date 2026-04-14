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
    padding: 0;
    flex-direction: column;
    border-radius: 15px;
    box-shadow: var(--card-shadow);
}

.card-header {
    width: 100%;
    height: 3rem;
    padding: 5px 0;
    border-bottom: 2px solid var(--bg-color);
    border-radius: 15px 15px 0 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.card-footer {
    border-top: 2px solid var(--bg-color);
    border-radius: 0 0 10px 10px;
    padding: 5px;
}

.card,
.card-header,
.card-footer {
    background-color: var(--bg-card-color);
}
</style>
