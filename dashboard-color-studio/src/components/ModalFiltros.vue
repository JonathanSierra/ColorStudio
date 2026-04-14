<script setup>
import { computed, onMounted, ref } from 'vue';
import BasePopOver from './BasePopOver.vue';

const props = defineProps(['filtroEstado', 'fechaInicio', 'fechaFinal', 'item', 'tipo']);
const emits = defineEmits(['cambiar-estado', 'filtroFechaRegistro', 'limpiar-filtros']);

onMounted(() => {
    fechaDesde.value = props.fechaInicio;
    fechaHasta.value = props.fechaFinal;
});

const limpiarTodo = () => {
    fechaDesde.value = '';
    fechaHasta.value = '';
    emits('limpiar-filtros');
    emits('cambiar-estado', 'sinFiltros');
};

const textoActivo = computed(() => {
    if (props.tipo === 'Producto') {
        return 'Disponibles';
    }
    if (props.tipo === 'Cliente') {
        return 'Activos';
    }
});
const textoInactivo = computed(() => {
    if (props.tipo === 'Producto') {
        return 'No Disponibles';
    }
    if (props.tipo === 'Cliente') {
        return 'Inactivos';
    }
});

const mostrarRango = ref(false);
const fechaDesde = ref('');
const fechaHasta = ref('');
</script>

<template>
    <BasePopOver left="98.2%" ancho="100px">
        <template #PopOverContent>
            <li v-on:click="limpiarTodo" :class="{ 'filtro-activo': !props.fechaInicio && !props.fechaFinal && props.filtroEstado === 'sinFiltros' }">No filtrar</li>
            <li v-on:click="$emit('cambiar-estado', 'activos')" :class="{ 'filtro-activo': props.filtroEstado === 'activos' }">{{ textoActivo }}</li>
            <li v-on:click="$emit('cambiar-estado', 'inactivos')" :class="{ 'filtro-activo': props.filtroEstado === 'inactivos' }">{{ textoInactivo }}</li>
            <li v-if="tipo === 'Cliente'" v-on:click="mostrarRango = !mostrarRango" class="filtro-fecha-ingreso" :class="{ 'filtro-activo': mostrarRango || props.fechaInicio || props.fechaFinal }">Fecha de ingreso</li>
            <BasePopOver v-if="mostrarRango" class="modal-rango-fecha-ingreso" right="-2px" top="100%" ancho="300px">
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
    border: 2px solid var(--border-color);
    background-color: var(--bg-color);
    position: absolute;
    top: -0.5%;
    right: -46%;
}

li {
    color: var(--text-primary-color);
}

li img {
    width: 1.1rem;
    height: 1.1rem;
    margin-right: 3px;
}

.filtro-activo {
    color: white !important;
    background-color: var(--accent-hover-color) !important;
}

.filtro-fecha-ingreso {
    font-size: 12.5px;
}

.modal-rango-fecha-ingreso {
    position: absolute;
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
    color: var(--text-secondary-color);
    background-color: var(--bg-input-color);
    border-radius: 5px;
}
</style>
