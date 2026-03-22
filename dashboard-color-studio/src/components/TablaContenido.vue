<script setup>
import { computed } from 'vue';

const props = defineProps({
    datos: Array,
    columnas: Array
});

const columnasVisibles = computed(() => {
    return props.columnas.filter(columna => columna.campo !== 'id');
});
</script>
<template>
    <div class="contenedor-table">
        <table>
            <thead>
                <tr>
                    <th v-for="columna in columnasVisibles" :key="columna.campo">
                        {{ columna.titulo }}
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="fila in datos" :key="fila.id">
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
    height: 100%;
}

table {
    color: black;
    width: 100%;
    align-self: center;
    border-collapse: separate;
    border-spacing: 0;
    table-layout: fixed;
    empty-cells: show;
}
table tr {
    height: 3rem;
    max-height: 3rem;
}

table td {
    font-size: 15px;
}

table th {
    font-size: 17px;
    border-bottom: 2px solid rgb(228, 238, 246);
}

table th,
td {
    background-color: white;
    text-align: center;
}

table thead {
    font-weight: bold;
}

tbody tr:nth-child(odd) td {
    background-color: rgb(228, 239, 255);
}
tbody tr:nth-child(even) td {
    background-color: rgb(243, 248, 255);
}
</style>
