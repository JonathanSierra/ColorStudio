<script setup>
import BasePopOver from './BasePopOver.vue';

const props = defineProps(['item', 'tipo']);

const emits = defineEmits(['desactivar', 'activar', 'eliminar']);
</script>

<template>
    <BasePopOver ancho="150px" left="60%">
        <template #PopOverContent>
            <li v-if="tipo === 'Cliente'" v-on:click.stop=""><img src="../assets/images/person_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" />Ver perfil</li>
            <li v-if="tipo === 'Cliente'" v-on:click.stop=""><img src="../assets/images/history_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" />Ver historial</li>
            <li v-if="tipo === 'Cliente'" v-on:click.stop=""><img src="../assets/images/whatsapp.png" alt="" />Enviar WhatsApp</li>
            <li v-if="item.activo" v-on:click.stop="$emit('desactivar', item)"><img src="../assets/images/delete_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" />Desactivar {{ tipo }}</li>
            <li v-else v-on:click.stop="$emit('activar', item)"><img src="../assets/images/check_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" />Reactivar {{ tipo }}</li>
            <li v-if="!item.activo" v-on:click.stop="$emit('eliminar', item)"><img src="../assets/images/delete_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" />Eliminar {{ tipo }}</li>
        </template>
    </BasePopOver>
</template>
<style scoped>
li img {
    width: 1.1rem;
    height: 1.1rem;
    margin-right: 3px;
}
</style>
