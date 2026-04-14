<script setup>
const props = defineProps(['item', 'tipo', 'filaAbierta']);
const emits = defineEmits(['editar', 'alternar', 'activar', 'desactivar', 'eliminar', 'confirmar', 'cancelar', 'abrir']);

import ModalMasAcciones from './ModalMasAcciones.vue';
</script>

<template>
    <div class="acciones">
        <template v-if="tipo !== 'Sesion'">
            <button class="editar" v-on:click.stop="$emit('editar', item)"><img src="../assets/images/edit_35dp_000000_FILL0_wght400_GRAD0_opsz40.png" alt="editar" /></button>
            <button class="mas-acciones" v-on:click.stop="$emit('alternar', item.id)"><img src="../assets/images/more_vert_35dp_000000_FILL0_wght400_GRAD0_opsz40.png" alt="mas acciones" /></button>
        </template>
        <button v-if="tipo === 'Sesion'" class="editar" v-on:click.stop="$emit('eliminar', item)"><img src="../assets/images/delete_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="eliminar" /></button>
        <ModalMasAcciones :tipo="tipo" v-if="filaAbierta === item.id" :item="item" @confirmar="$emit('confirmar', item)" @cancelar="$emit('cancelar', item)" @abrir="$emit('abrir', item)" @activar="$emit('activar', item)" @desactivar="$emit('desactivar', item)" @eliminar="$emit('eliminar', item)"></ModalMasAcciones>
    </div>
</template>

<style scoped>
.acciones {
    position: relative;
    display: flex;
    justify-content: center;
    gap: 0.5rem;
}

.mas-acciones,
.editar {
    display: flex;
    padding: 0;
    border: 2px solid rgba(255, 255, 255, 0);
    background-color: rgba(255, 255, 255, 0);
    border-radius: 100%;
}
.mas-acciones img,
.editar img {
    align-self: center;
    width: 22px;
    height: 22px;
    filter: var(--icon-filter);
}
</style>
