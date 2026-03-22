<script setup>
import { ref, watch } from 'vue';

const nombreCliente = ref();
const fechaNacimiento = ref();
const numeroCelular = ref();

const props = defineProps(['cliente']);

const emit = defineEmits(['cerrar', 'actualizar']);

const enviarInformacion = () => {
    const datosClienteActualizado = {
        nombre: nombreCliente.value,
        fecha_cumpleaños: fechaNacimiento.value,
        numero_celular: numeroCelular.value
    };

    emit('actualizar', datosClienteActualizado);
};

watch(
    () => props.cliente,
    nuevo => {
        if (nuevo) {
            nombreCliente.value = nuevo.nombre;

            const partesFecha = nuevo.fecha_cumpleaños.split('/');
            if (partesFecha.length === 3) {
                fechaNacimiento.value = `${partesFecha[2]}-${partesFecha[1]}-${partesFecha[0]}`;
            } else {
                fechaNacimiento.value = nuevo.fecha_cumpleaños;
            }

            numeroCelular.value = nuevo.numero_celular;
        }

        console.log('Fecha recibida:', nuevo.fecha_cumpleaños);
    },
    { immediate: true }
);
</script>

<template>
    <div class="backdrop">
        <div class="modal-window">
            <header>
                <h2>Editar cliente</h2>
            </header>
            <main>
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
            </main>
            <footer>
                <button @click="$emit('cerrar')" class="btn-cancelar">Cancelar</button>
                <button v-on:click="enviarInformacion" class="btn-actualizar">Actualizar</button>
            </footer>
        </div>
    </div>
</template>

<style scoped>
.backdrop {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 2;
    background-color: rgba(0, 0, 0, 0.412);
    width: 100dvw;
    height: 100dvh;
}

.modal-window {
    display: flex;
    overflow: hidden;
    flex-direction: column;
    border-radius: 20px;
    width: 50%;
    height: 60%;
    background-color: rgb(228, 238, 246);
}

.modal-window header {
    overflow: hidden;
    display: flex;
    align-items: center;
    padding: 1rem;
    background-color: white;
    color: black;
}

.modal-window main {
    display: flex;
    padding: 1rem;
    justify-content: space-between;
    gap: 3rem;
    flex-wrap: wrap;
    flex: 1;
}

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

.modal-window footer {
    display: flex;
    justify-content: end;
    gap: 1rem;
    background-color: white;
    color: black;
    padding: 1rem;
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
