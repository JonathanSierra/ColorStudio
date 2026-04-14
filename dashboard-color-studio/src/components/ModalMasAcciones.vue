<script setup>
import { computed } from 'vue';
import BasePopOver from './BasePopOver.vue';
import PersonIcon from '../assets/images/person_30dp_000000_FILL0_wght400_GRAD0_opsz24.png';
import ProductIcon from '../assets/images/package_2_30dp_000000_FILL0_wght400_GRAD0_opsz24.png';

const props = defineProps(['item', 'tipo']);

const emits = defineEmits(['desactivar', 'activar', 'eliminar', 'confirmar', 'cancelar', 'abrir']);

const isActive = computed(() => {
    if ((props.tipo === 'Cliente' && props.item.estado === 'Activo') || (props.tipo === 'Producto' && props.item.estado === 'Disponible')) {
        return true;
    } else {
        return false;
    }
});

const itemIcon = computed(() => {
    if (props.tipo === 'Producto') {
        return ProductIcon;
    }
    if (props.tipo === 'Cliente') {
        return PersonIcon;
    }
});
</script>

<template>
    <BasePopOver ancho="160px" left="60%">
        <template #PopOverContent>
            <li v-if="tipo === 'Cliente' || tipo === 'Producto'" v-on:click.stop="$emit('abrir')"><img :src="itemIcon" alt="" />Ver {{ tipo }}</li>
            <li v-if="tipo === 'Cliente'" v-on:click.stop=""><img src="../assets/images/whatsapp.png" alt="" />Enviar WhatsApp</li>
            <template v-if="tipo !== 'Cita'">
                <li v-if="isActive" v-on:click.stop="$emit('desactivar', item)"><img src="../assets/images/delete_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" />Desactivar {{ tipo }}</li>
                <li v-else v-on:click.stop="$emit('activar', item)"><img src="../assets/images/check_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" />Reactivar {{ tipo }}</li>
                <li v-if="!isActive" v-on:click.stop="$emit('eliminar', item)"><img src="../assets/images/delete_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" />Eliminar {{ tipo }}</li>
            </template>
            <template v-if="tipo === 'Cita'">
                <li v-if="tipo === 'Cita'" v-on:click.stop="$emit('confirmar', item)"><img src="../assets/images/check_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" />Confirmar</li>
                <li v-if="tipo === 'Cita'" v-on:click.stop="$emit('cancelar', item)"><img src="../assets/images/delete_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" />Cancelar</li>
            </template>
        </template>
    </BasePopOver>
</template>
<style scoped>
li img {
    filter: var(--icon-filter);
    width: 1.1rem;
    height: 1.1rem;
    margin-right: 3px;
}
</style>
