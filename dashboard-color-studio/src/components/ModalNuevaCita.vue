<script setup>
import { obtenerProcesos } from '../composables/procesosService';
import BaseModal from './BaseModal.vue';

import { ref, onMounted } from 'vue';

const procesos = ref([]);
const procesoCita = ref();
const fechaCita = ref();
const textError = ref('');

const emit = defineEmits(['cerrar', 'crear']);

onMounted(async () => {
    const datos = await obtenerProcesos();
    procesos.value = datos;
});

const enviarInformacion = () => {
    if (!procesoCita.value || !fechaCita.value) {
        textError.value = 'Debes completar todos los campos.';
    } else {
        const datosNuevaCita = {
            proceso_id: procesoCita.value,
            fecha_hora_cita: fechaCita.value
        };
        emit('crear', datosNuevaCita);
    }
};
</script>

<template>
    <BaseModal ancho="30%" alto="40%" gap="2rem" @cerrar="$emit('cerrar')">
        <template #BaseModalHeader>
            <h2>Crear nueva cita</h2>
        </template>
        <template #BaseModalMain>
            <div class="campo">
                <h3>Proceso:</h3>
                <select v-model="procesoCita" name="seleccionarProceso" id="">
                    <option v-for="proceso in procesos" :key="proceso.id" :value="proceso.id">
                        {{ proceso.nombre }}
                    </option>
                </select>
            </div>
            <div class="campo">
                <h3>Fecha:</h3>
                <input v-model="fechaCita" type="date" name="fecha" id="" />
            </div>
        </template>
        <template #BaseModalFooter>
            <span v-if="textError" class="text-error">{{ textError }}</span>
            <button @click="$emit('cerrar')" class="btn-cancelar">Cancelar</button>
            <button v-on:click="enviarInformacion" class="btn-crear">Crear</button>
        </template>
    </BaseModal>
</template>

<style scoped>
.campo {
    max-height: 4rem;
    padding: 0 1rem;
    border-radius: 10px;
    background-color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
}

.campo input {
    background-color: rgb(228, 238, 246);
    border: none;
    color: black;
    border-radius: 5px;
    height: 1.8rem;
}

.campo select {
    background-color: rgb(228, 238, 246);
    border: none;
    color: black;
    border-radius: 5px;
    height: 1.8rem;
}

.btn-cancelar {
    background-color: white;
    border: 2px solid black;
    color: black;
}

h3,
h2 {
    color: black;
    padding: 0;
    margin: 0;
}

.text-error {
    font-size: 17px;
    color: red;
    margin-right: auto;
    align-self: center;
}
</style>
