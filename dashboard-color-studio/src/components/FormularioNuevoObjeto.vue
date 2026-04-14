<script setup>
import { onMounted, ref, watch } from 'vue';
import BaseModal from './BaseModal.vue';

const props = defineProps(['campos', 'titulo', 'type', 'ancho', 'alto', 'objetoAEditar']);
const emits = defineEmits(['enviar', 'cerrar']);

const formData = ref({});
const textError = ref('');

// const tiposActuales = ref({});

// const esFecha = campo => campo.type === 'date' || campo.type === 'datetime-local';

// const obtenerTipo = campo => {
//     if (tiposActuales.value[campo.nombre] || formData.value[campo.nombre]) {
//         return campo.type;
//     }
//     if (esFecha(campo)) {
//         return 'text';
//     }
//     return campo.type;
// };

// const manejarFocus = campo => {
//     if (esFecha(campo)) {
//         tiposActuales.value[campo.nombre] = campo.type;
//     }
// };

// const manejarBlur = campo => {
//     if (esFecha(campo) && !formData.value[campo.nombre]) {
//         tiposActuales.value[campo.nombre] = 'text';
//     }
// };

const enviarInformacion = () => {
    const faltanCampos = props.campos.some(campo => {
        if (campo.requerido === true) {
            const valor = formData.value[campo.nombre];
            return valor === '' || valor === undefined;
        }
        return false;
    });
    if (faltanCampos) {
        textError.value = 'Debes completar todos los campos.';
    } else {
        textError.value = '';
        emits('enviar', formData.value);
    }
};

watch(
    () => props.objetoAEditar,
    nuevo => {
        if (nuevo) {
            formData.value = { ...nuevo };
        } else {
            formData.value = {};
        }
    },
    { immediate: true }
);
</script>
<template>
    <BaseModal :ancho="ancho" :alto="alto" @cerrar="$emit('cerrar')">
        <template #BaseModalHeader>
            <h2>{{ titulo }}</h2>
        </template>
        <template #BaseModalMain>
            <div v-for="campo in campos" class="campo">
                <h3>{{ campo.titulo }}</h3>
                <input v-if="campo.type !== 'select'" :class="{ 'fecha-vacia': !formData[campo.nombre] }" v-model="formData[campo.nombre]" :type="campo.type" :pattern="campo.pattern" :maxlength="campo.maxlength" name="" id="" />
                <select v-else v-model="formData[campo.nombre]" name="" id="">
                    <option v-for="opcion in campo.opciones" :key="opcion.id" :value="opcion.id">{{ opcion.nombre }}</option>
                </select>
            </div>
        </template>
        <template #BaseModalFooter>
            <span v-if="textError" class="text-error">{{ textError }}</span>
            <button @click="$emit('cerrar')" class="btn-cancelar">Cancelar</button>
            <button v-on:click="enviarInformacion">Listo</button>
        </template>
    </BaseModal>
</template>
<style scoped>
.campo {
    max-height: 4rem;
    max-width: 50%;
    padding: 0 1rem;
    border-radius: 10px;
    background-color: var(--bg-card-color);
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
}

.campo input,
.campo select {
    border: none;
    background-color: var(--bg-color);
    color: var(--text-primary-color);
    border-radius: 5px;
    height: 1.8rem;
}

h3,
h2 {
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
