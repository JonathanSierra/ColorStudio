<script setup>
import axios from 'axios';
import { ref } from 'vue';

const misProcesos = ref([])
const misClientes = ref([])

import { onMounted } from 'vue';
import Card from '../components/Card.vue';

onMounted(async () => {
    const respuesta = await axios.get('http://127.0.0.1:8000/procesos')

    misProcesos.value = respuesta.data

    console.log(misProcesos.value)

})
</script>
<template>
    <h1>Dashboard</h1>
    <div class="cards-container">
        <Card class="citas-hoy">
            <template v-slot:header-content>
                <h2>Citas para hoy</h2>
            </template>
            <ul class="lista-citas-proximos">
                <li v-for="clienteHoy in clientesHoy">Cita</li>
            </ul>
        </Card>
        <Card class="cumpleaños-proximos">
            <template v-slot:header-content>
                <h2>Proximos Cumpleaños</h2>
            </template>
            <ul class="lista-cumpleaños-proximos">
                <li> <img src="../assets/images/cake_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="">Cita</li>
            </ul>
        </Card>
    </div>
</template>

<style scoped>
.cards-container{
    display: flex;
    justify-content: space-between;
    margin: 0 2rem;
    height: 40%;
    gap: 2rem;
}

.card-header{
    width: 100%;
    height: 20%;
    background-color: rgb(249, 186, 207);
    border-radius: 30px 30px 0 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.lista-citas-proximos{
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    width: 95%;
    height: 80%;
    align-self: center;
    margin: 0;
}
.lista-cumpleaños-proximos{
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    width: 95%;
    height: 80%;
    align-self: center;
    margin: 0;
    padding: 0;
}

li{
    display: flex;
    border: 2px solid red;
    align-items: center;
}

li img{
    border: 2px solid red;
    width: 30px;
    height: 30px;
    background-color: rgb(249, 186, 207);
    border-radius: 30px;
    padding: 4px;
    margin: 0 5px;
}

.citas-hoy{
    width: 60%;
    height: 100%;
}

.citas-hoy h2{
    margin: 0 0 0 1rem;
    font-size: 20px;
}

.cumpleaños-proximos{
    width: 25%;
    height: 100%;
}

.cumpleaños-proximos h2{
    margin: 0 0 0 1rem;
    font-size: 20px;
}
</style>