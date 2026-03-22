<script setup>
const props = defineProps(['cliente']);

const emits = defineEmits(['desactivar', 'activar', 'eliminar']);
</script>

<template>
    <div class="modal-window">
        <ul>
            <li v-on:click=""><img src="../assets/images/person_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" />Ver perfil</li>
            <li><img src="../assets/images/history_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" />Ver historial</li>
            <li><img src="../assets/images/whatsapp.png" alt="" />Enviar WhatsApp</li>
            <li v-if="cliente.activo" v-on:click="$emit('desactivar', cliente)"><img src="../assets/images/delete_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" />Eliminar</li>
            <li v-else v-on:click="$emit('activar', cliente)"><img src="../assets/images/check_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" />Reactivar Cliente</li>
        </ul>
    </div>
</template>
<style scoped>
.modal-window {
    display: flex;
    justify-content: center;
    flex-direction: column;
    position: absolute;
    top: -0.5%;
    right: -37.3%;
    background: white;
    z-index: 10;
    width: 150px;
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
