<script setup>
import BasePopOver from './BasePopOver.vue';

const props = defineProps(['cita']);

const emits = defineEmits(['confirmar', 'cancelar']);
</script>

<template>
    <BasePopOver ancho="100px" left="70%" top="-1px">
        <template #PopOverContent>
            <li v-on:click.stop="$emit('confirmar', cita)"><img src="../assets/images/check_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" />Confirmar</li>
            <li v-on:click.stop="$emit('cancelar', cita)"><img src="../assets/images/delete_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" />Cancelar</li>
        </template>
    </BasePopOver>
</template>
<style scoped>
li img {
    width: 1.1rem;
    height: 1.1rem;
    margin-right: 3px;
}

:deep(ul) {
    right: 100%;
}

li {
    width: auto;
    white-space: nowrap;
}
</style>
