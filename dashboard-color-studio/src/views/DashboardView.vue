<script setup>
import axios from 'axios';
import { ref } from 'vue';

const misProcesos = ref([])

import { onMounted } from 'vue';
import Card from '../components/Card.vue';
import TablaContenido from '../components/TablaContenido.vue';


onMounted(async () => {
    const respuesta = await axios.get('http://127.0.0.1:8000/procesos')

    misProcesos.value = respuesta.data

    console.log(misProcesos.value)

})
</script>
<template>
    <h1>Dashboard</h1>
    <div class="card-container">
        <Card class="citas-hoy">
            <h2>Citas para hoy</h2>
            <TablaContenido class="tabla-citas-hoy"></TablaContenido>
        </Card>
        <Card class="cumpleaños-hoy">
            <h2>Cumpleaños hoy</h2>
            <TablaContenido class="tabla-cumpleaños-hoy"></TablaContenido>
        </Card>
    </div>
</template>

<style scoped>
.card-container{
    display: flex;
    justify-content: space-between;
    margin: 0 1rem;
    height: 40%;
    gap: 2rem;
}

.tabla-citas-hoy{
    width: 95%;
    align-self: center;
    margin: 0;
}
.tabla-cumpleaños-hoy{
    width: 95%;
    align-self: center;
}

.citas-hoy{
    width: 60%;
    height: 100%;
    padding: 0.2rem 0;
}

.citas-hoy h2{
    margin: 0 0 0 1rem;
    font-size: 20px;
}

.cumpleaños-hoy{
    width: 25%;
    height: 100%;
    padding: 0.2rem 0.5rem;
}

.cumpleaños-hoy h2{
    margin: 0 0 0 0.5rem;
    font-size: 20px;
}

h1 {
    padding: 0.5rem 0 0 10px;
    font-size: 30px;
}
</style>