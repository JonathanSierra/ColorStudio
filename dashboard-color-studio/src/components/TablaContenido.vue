<script setup>
import { computed } from 'vue';

const emits = defineEmits(['fila-click']);

const props = defineProps({
    minHeight: {
        type: String,
        default: 'auto'
    },
    claseFila: Function,
    datos: Array,
    columnas: Array
});

const columnasVisibles = computed(() => {
    return props.columnas.filter(columna => columna.campo !== 'id');
});
</script>
<template>
    <div class="contenedor-table" :style="{ minHeight: props.minHeight }">
        <table :class="{ 'tabla-vacia': datos.length === 0 }">
            <thead>
                <tr>
                    <th v-for="columna in columnasVisibles" :key="columna.campo">
                        {{ columna.titulo }}
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-if="datos.length === 0" class="fila-tabla-vacia">
                    <td :colspan="columnasVisibles.length" class="mensaje-tabla-vacia">No hay datos para mostrar</td>
                </tr>
                <tr @click="$emit('fila-click', fila)" v-for="fila in datos" :class="claseFila ? claseFila(fila) : ''" :key="fila.id">
                    <td v-for="columna in columnasVisibles" :key="columna.campo">
                        <slot :name="columna.campo" :fila="fila">
                            {{ fila[columna.campo] }}
                        </slot>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<style scoped>
.contenedor-table {
    width: 100%;
    height: auto;
    background-color: var(--bg-card-color);
}

table {
    color: var(--text-primary-color);
    width: 100%;
    align-self: center;
    border-collapse: separate;
    border-spacing: 0;
    table-layout: fixed;
    empty-cells: show;
}

.tabla-vacia {
    height: 100%;
}

table tr {
    height: 3rem;
    max-height: 3rem;
}

table td {
    font-size: 15px;
    color: var(--text-primary-color);
}

table th {
    font-size: 17px;
    border-bottom: 2px solid var(--bg-color);
}

.mensaje-tabla-vacia {
    background-color: var(--bg-card-color) !important;
    color: var(--text-secondary-color);
    vertical-align: middle;
    text-align: center;
}

table th,
td {
    background-color: var(--table-primary-color);
    text-align: center;
}

table thead {
    font-weight: bold;
}

tbody tr:nth-child(odd) td {
    background-color: var(--table-secondary-color);
}
tbody tr:nth-child(even) td {
    background-color: var(--table-primary-color);
}
</style>
