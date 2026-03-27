<script setup>
import { ref } from 'vue';
import BasePopOver from './BasePopOver.vue';

const emits = defineEmits(['inactivos', 'activos', 'filtroFechaRegistro']);

const props = defineProps(['mostrarClientesInactivos']);

const mostrarRango = ref(false);
const fechaDesde = ref('');
const fechaHasta = ref('');
</script>

<template>
    <BasePopOver ancho="100px">
        <template #PopOverContent>
            <li v-on:click="$emit('activos')" :class="{ 'filtro-activo': !mostrarClientesInactivos }">Activos</li>
            <li v-on:click="$emit('inactivos')" :class="{ 'filtro-activo': mostrarClientesInactivos }">Inactivos</li>
            <li class="filtro-fecha-ingreso" v-on:click="mostrarRango = true">Fecha de ingreso</li>
            <BasePopOver v-if="mostrarRango" class="modal-rango-fecha-ingreso" ancho="300px">
                <template class="template" #PopOverContent>
                    <div class="desde-hasta">
                        <div class="desde">
                            <span>Desde:</span>
                            <input v-model="fechaDesde" type="date" />
                        </div>
                        <div class="hasta">
                            <span>Hasta:</span>
                            <input v-model="fechaHasta" type="date" />
                        </div>
                        <button v-on:click="$emit('filtroFechaRegistro', { desde: fechaDesde, hasta: fechaHasta })"><span>Aplicar</span></button>
                    </div>
                </template>
            </BasePopOver>
        </template>
    </BasePopOver>
</template>
<style scoped>
.modal-window {
    border: 2px solid rgb(5, 148, 244);
    position: absolute;
    top: -0.5%;
    right: -47.5%;
}

li img {
    width: 1.1rem;
    height: 1.1rem;
    margin-right: 3px;
}

.filtro-activo {
    color: white !important;
    background-color: rgb(5, 148, 244) !important;
}

.filtro-fecha-ingreso {
    font-size: 12.5px;
}

.modal-rango-fecha-ingreso {
    position: absolute;
    top: 77px;
    right: -2px;
}

.desde-hasta {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    gap: 17px;
}

.desde,
.hasta {
    display: flex;
    align-items: center;
    width: 47%;
    gap: 5px;
}

span {
    font-size: 12px;
}

button {
    display: flex;
    width: 20%;
    height: 1.5rem;
    align-items: center;
    justify-content: center;
}

.modal-rango-fecha-ingreso input {
    width: 70%;
    height: 1.5rem;
    color: black;
    background-color: rgb(228, 238, 246);
    border-radius: 5px;
}
</style>
