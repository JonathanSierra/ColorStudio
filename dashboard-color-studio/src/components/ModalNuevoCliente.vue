<script setup>
import BaseModal from './BaseModal.vue';

import { ref } from 'vue';

const nombreCliente = ref();
const fechaNacimiento = ref();
const numeroCelular = ref();

const emit = defineEmits(['cerrar', 'crear']);

const enviarInformacion = () => {
    const datosNuevoCliente = {
        nombre: nombreCliente.value,
        fecha_cumpleaños: fechaNacimiento.value,
        numero_celular: numeroCelular.value
    };

    emit('crear', datosNuevoCliente);
};
</script>

<template>
    <BaseModal @cerrar="$emit('cerrar')">
        <template #BaseModalHeader>
            <h2>Crear nuevo cliente</h2>
        </template>
        <template #BaseModalMain>
            <div class="campo">
                <h3>Nombre:</h3>
                <input v-model="nombreCliente" type="text" name="nombre" id="" />
            </div>
            <div class="campo">
                <h3>Numero de celular:</h3>
                <input v-model="numeroCelular" type="text" name="numero-celular" id="" />
            </div>
            <div class="campo">
                <h3>Fecha de nacimiento:</h3>
                <input v-model="fechaNacimiento" type="date" name="fecha-nacimiento" id="" />
            </div>
        </template>
        <template #BaseModalFooter>
            <button @click="$emit('cerrar')" class="btn-cancelar">Cancelar</button>
            <button v-on:click="enviarInformacion" class="btn-crear">Crear</button>
        </template>
    </BaseModal>
</template>

<style scoped>
.campo {
    max-height: 4rem;
    max-width: 50%;
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
</style>
