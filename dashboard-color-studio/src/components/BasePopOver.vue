<script setup>
const emits = defineEmits(['cerrar']);

const props = defineProps({
    ancho: { type: String, default: '150px' },
    top: { type: String, default: 'auto' },
    left: { type: String, default: 'auto' },
    right: { type: String, default: 'auto' }
});
</script>
<template>
    <div class="modal-window" :style="{ width: ancho, top: top, left: left, right: right }">
        <ul>
            <slot name="PopOverContent"></slot>
        </ul>
    </div>
</template>
<style scoped>
.modal-window {
    display: flex;
    justify-content: center;
    flex-direction: column;
    position: absolute;
    background: white;
    z-index: 10;
    width: 80px;
    padding: 5px;
    border-radius: 10px;
}

:deep(li) {
    display: flex;
    color: black;
    border-radius: 5px;
    align-items: center;
    font-size: 14px;
    transition: all ease-in 50ms;
    cursor: pointer;
    list-style-type: none;
    padding-left: 2px;
}

ul {
    flex-direction: column;
    gap: 3px;
    display: flex;
    margin: 0;
    padding: 0;
}

:deep(li:hover) {
    background-color: rgb(208, 208, 208);
}
</style>
