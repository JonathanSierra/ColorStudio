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
    color: black;
    margin: 0 0 50px 0;
    width: 70vw;
    min-height: 80%;
    border-collapse: separate;
    border-spacing: 0;
    overflow: hidden;
    table-layout: fixed;
    empty-cells: show;
    border-radius: 20px;
}

table td{
    font-size: 20px;
}

table th{
    font-size: 22px;
}

table th,
td {
    background-color: white;
    text-align: center;
}

table thead {
    font-weight: bold;
}

tbody tr:nth-child(odd) td{
    background-color: rgb(228, 239, 255);
}

tbody tr:nth-child(even) td{
    background-color: rgb(243, 248, 255);
}
</style>