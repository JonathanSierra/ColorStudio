<script setup>
import { obtenerProcesos } from '../composables/procesosService';
import BaseModal from './BaseModal.vue';
import { onMounted } from 'vue';
import { ref, watch } from 'vue';

const procesos = ref([]);
const procesoCita = ref();
const fechaCita = ref();
const textError = ref('');

const props = defineProps(['cita']);

const emit = defineEmits(['cerrar', 'actualizar']);

onMounted(async () => {
    const datos = await obtenerProcesos();
    procesos.value = datos;

    if (props.cita) {
        const procesoEncontrado = procesos.value.find(p => p.nombre === props.cita.nombre_proceso);
        if (procesoEncontrado) {
            procesoCita.value = procesoEncontrado.id;
        }
    }
});

const enviarInformacion = () => {
    const datosCitaActualizada = {
        proceso_id: procesoCita.value,
        fecha_hora_cita: fechaCita.value
    };

    emit('actualizar', datosCitaActualizada);
};

watch(
    () => props.cita,
    nuevo => {
        if (nuevo) {
            const partesFecha = nuevo.fecha_hora_cita.split('/');
            if (partesFecha.length === 3) {
                fechaCita.value = `${partesFecha[2]}-${partesFecha[1]}-${partesFecha[0]}`;
            } else {
                fechaCita.value = nuevo.fecha_hora_cita;
            }
        }

        console.log('Fecha recibida:', nuevo.fecha_hora_cita);
    },
    { immediate: true }
);
</script>

<template>
    <BaseModal ancho="30%" alto="40%" gap="2rem" @cerrar="$emit('cerrar')">
        <template #BaseModalHeader>
            <h2>Editar Cita</h2>
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
                <input v-model="fechaCita" type="date" name="fecha-cita" id="" />
            </div>
        </template>
        <template #BaseModalFooter>
            <button @click="$emit('cerrar')" class="btn-cancelar">Cancelar</button>
            <button v-on:click="enviarInformacion" class="btn-actualizar">Actualizar</button>
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
</style>
