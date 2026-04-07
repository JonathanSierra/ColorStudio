<script setup>
const props = defineProps(['cliente', 'filaAbierta']);
const emits = defineEmits(['editar', 'alternar', 'activar', 'desactivar', 'eliminar']);

import ModalMasAcciones from './ModalMasAcciones.vue';
</script>

<template>
    <div class="acciones">
        <button class="editar" v-on:click.stop="$emit('editar', cliente)"><img src="../assets/images/edit_35dp_000000_FILL0_wght400_GRAD0_opsz40.png" alt="editar" /></button>
        <button class="mas-acciones" v-on:click.stop="$emit('alternar', cliente.id)"><img src="../assets/images/more_vert_35dp_000000_FILL0_wght400_GRAD0_opsz40.png" alt="mas acciones" /></button>
        <ModalMasAcciones v-if="filaAbierta === cliente.id" :cliente="cliente" @activar="$emit('activar', cliente)" @desactivar="$emit('desactivar', cliente)" @eliminar="$emit('eliminar', cliente)"></ModalMasAcciones>
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
