<script setup>
import axios from 'axios'
import { ref } from 'vue'

const misClientes = ref([])

import { onMounted } from 'vue';
import TablaContenido from '../components/TablaContenido.vue';

const misColumnas = [
    { titulo: 'Id', campo: 'id' },
    { titulo: 'Nombre Completo', campo: 'nombre' },
    { titulo: 'Cumpleaños', campo: 'fecha_cumpleaños' },
    { titulo: 'Numero de celular', campo: 'numero_celular' },
    { titulo: 'Fecha de Registro', campo: 'fecha_registro' }
]

onMounted(async () => {
    const respuesta = await axios.get('http://127.0.0.1:8000/clientes')

    misClientes.value = respuesta.data

    console.log(misClientes.value)
})
</script>

<template>
        <h1>Clientes</h1>

        <tabla-contenido :datos="misClientes" :columnas="misColumnas"></tabla-contenido>

</template>

<style scoped>
h1 {
    margin: 20px 0 10px 0;
    font-size: 30px;
}

p {
    margin: 20px 0 5rem 0;
}
</style>