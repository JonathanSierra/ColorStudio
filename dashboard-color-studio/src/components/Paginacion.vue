<script setup>
const props = defineProps(['paginasVisibles', 'itemsPorPagina', 'itemsPaginados', 'textoPaginacion', 'paginaActual', 'totalPaginas']);
const emits = defineEmits(['primera', 'anterior', 'siguiente', 'ultima', 'cambiar-pagina']);
</script>

<template>
    <div class="rowing">
        <span>{{ textoPaginacion }}</span>
    </div>
    <div class="table-page">
        <button v-on:click="$emit('primera')"><img src="../assets/images/first_page_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" /></button>
        <button v-on:click="$emit('anterior')"><img src="../assets/images/keyboard_arrow_left_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" /></button>
        <button v-for="pagina in paginasVisibles" :key="pagina" v-on:click="$emit('cambiar-pagina', pagina)" :class="{ 'boton-activo': paginaActual === pagina }">{{ pagina }}</button>
        <button v-on:click="$emit('siguiente')"><img src="../assets/images/keyboard_arrow_right_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" /></button>
        <button v-on:click="$emit('ultima')"><img src="../assets/images/last_page_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" /></button>
    </div>
</template>

<style scoped>
.rowing {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 2rem;
}

.table-page {
    display: flex;
    gap: 10px;
    align-items: center;
    justify-content: space-evenly;
    height: 2rem;
}

.boton-activo {
    color: white !important;
    background-color: rgb(5, 148, 244) !important;
}

.table-page img {
    width: 20px;
    height: 20px;
}

.table-page button {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: white;
    width: 1rem;
    height: 1rem;
    border-radius: 100%;
    padding: 10px;
    color: black;
}
</style>
