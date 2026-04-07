<script setup>
const props = defineProps(['sesion', 'filaAbierta']);
const emits = defineEmits(['eliminar']);
</script>

<template>
    <div class="acciones">
        <button class="editar" v-on:click.stop="$emit('eliminar', sesion)"><img src="../assets/images/delete_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="eliminar" /></button>
    </div>
</template>

<style scoped>
.acciones {
    position: relative;
    display: flex;
    justify-content: center;
    gap: 0.5rem;
}
.mas-acciones {
    display: flex;
    padding: 0;
    background-color: rgba(255, 255, 255, 0);
}
.editar {
    display: flex;
    padding: 0;
    background-color: rgba(255, 255, 255, 0);
}
.mas-acciones img {
    align-self: center;
    width: 20px;
    height: 20px;
}
.editar img {
    align-self: center;
    width: 20px;
    height: 20px;
}
</style>
