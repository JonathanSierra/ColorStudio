<script setup>
import axios from 'axios';
import { ref } from 'vue';

const misProcesos = ref([])

import { onMounted } from 'vue';


onMounted(async () => {
    const respuesta = await axios.get('http://127.0.0.1:8000/procesos')

    misProcesos.value = respuesta.data

    console.log(misProcesos.value)

})
</script>
<template>
    <h1>Dashboard</h1>
</template>

<style scoped>
h1 {
    padding: 0.5rem 0 0 10px;
    font-size: 30px;
}
</style>