<script setup>
const props = defineProps({
    datos: Array,
    columnas: Array
})
</script>
<template>
    <table>
        <thead>
            <tr>
                <th v-for="columna in columnas" :key="columna.campo">{{ columna.titulo }}</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="fila in datos" :key="fila.id">
                <td v-for="columna in columnas" :key="columna.campo">{{ fila[columna.campo] }}</td>
            </tr>
        </tbody>
    </table>
</template>

<style scoped>
table {
    margin: 0 0 50px 0;
    width: 70vw;
    border-collapse: collapse;
    table-layout: fixed;
    empty-cells: show;
}

table th,
td {
    text-align: center;
}

table thead {
    font-weight: bold;
}
</style>