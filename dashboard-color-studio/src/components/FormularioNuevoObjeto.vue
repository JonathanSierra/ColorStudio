<script setup>
import { ref } from 'vue';
import BaseModal from './BaseModal.vue';

const props = defineProps(['campos', 'titulo', 'type']);
const emits = defineEmits(['enviar', 'cerrar']);

const formData = ref({});
</script>
<template>
    <BaseModal @cerrar="$emit('cerrar')">
        <template #BaseModalHeader>
            <h2>{{ titulo }}</h2>
        </template>
        <template #BaseModalMain>
            <div v-for="campo in campos" class="campo">
                <h3>{{ campo.titulo }}</h3>
                <input v-model="formData[campo.nombre]" :type="campo.type" name="" id="" />
            </div>
        </template>
        <template #BaseModalFooter>
            <button v-on:click="$emit('enviar', formData)">Enviar</button>
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

.text-error {
    font-size: 17px;
    color: red;
    margin-right: auto;
    align-self: center;
}
</style>
