<script setup>
import BasePopOver from './BasePopOver.vue';

const props = defineProps(['cliente']);

const emits = defineEmits(['desactivar', 'activar', 'eliminar']);
</script>

<template>
    <BasePopOver ancho="150px">
        <template #PopOverContent>
            <li v-on:click=""><img src="../assets/images/person_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" />Ver perfil</li>
            <li><img src="../assets/images/history_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" />Ver historial</li>
            <li><img src="../assets/images/whatsapp.png" alt="" />Enviar WhatsApp</li>
            <li v-if="cliente.activo" v-on:click="$emit('desactivar', cliente)"><img src="../assets/images/delete_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" />Desactivar Cliente</li>
            <li v-else v-on:click="$emit('activar', cliente)"><img src="../assets/images/check_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" />Reactivar Cliente</li>
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
