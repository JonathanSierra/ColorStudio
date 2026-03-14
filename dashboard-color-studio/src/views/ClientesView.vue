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
    <div class="main">
        <h1>Clientes</h1>
        <p>Pronto aquí cargaremos a Ana, Carolina y María desde la base de datos.</p>

        <tabla-contenido :datos="misClientes" :columnas="misColumnas"></tabla-contenido>

        <router-link to="/">Home</router-link>
    </div>
</template>

<style scoped>
.main h1 {
    margin: 20px 0 10px 0;
}

.main p {
    margin: 20px 0 5rem 0;
}

.main {
    display: flex;
    flex-direction: column;
    align-items: center;
    color: black;
    height: 100vh;
}
</style>