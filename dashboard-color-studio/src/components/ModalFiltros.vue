<script setup>
const emits = defineEmits(['inactivos', 'activos', 'porFecha']);
</script>

<template>
    <div class="modal-window">
        <ul>
            <li v-on:click="$emit('activos')">Activos</li>
            <li v-on:click="$emit('inactivos')">Inactivos</li>
            <li v-on:click="$emit('porFecha')">Por fecha</li>
        </ul>
    </div>
</template>
<style scoped>
.modal-window {
    border: 2px solid rgb(5, 148, 244);
    display: flex;
    justify-content: center;
    flex-direction: column;
    position: absolute;
    top: -0.5%;
    right: -38.5%;
    background: white;
    z-index: 10;
    width: 80px;
    padding: 5px;
    border-radius: 10px;
}

li {
    display: flex;
    border-radius: 5px;
    align-items: center;
    font-size: 14px;
    transition: all ease-in 50ms;
    cursor: pointer;
    list-style-type: none;
    padding-left: 2px;
}

li img {
    width: 1.1rem;
    height: 1.1rem;
    margin-right: 3px;
}

ul {
    flex-direction: column;
    gap: 3px;
    display: flex;
    margin: 0;
    padding: 0;
}

li:hover {
    background-color: rgb(208, 208, 208);
}
</style>
