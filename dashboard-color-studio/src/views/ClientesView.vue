<script setup>
import { ref, onMounted, computed, watch } from 'vue';
import { usePaginacion } from '../composables/paginacion';
import { obtenerClientes, crearCliente, editarCliente, activarCliente, desactivarCliente, eliminarCliente } from '../composables/clientesService';
import { mostrarNotificacion, mensajeToast, tipoNotificacion } from '../composables/globalService';
import TablaContenido from '../components/TablaContenido.vue';
import Card from '../components/Card.vue';
import ModalMasAcciones from '../components/ModalMasAcciones.vue';
import ModalFiltros from '../components/ModalFiltros.vue';
import BaseToast from '../components/BaseToast.vue';
import ModalFicha from '../components/ModalFicha.vue';
import Acciones from '../components/Acciones.vue';
import { formatearFecha } from '../utils/formatters';
import Paginacion from '../components/Paginacion.vue';
import FormularioNuevoObjeto from '../components/FormularioNuevoObjeto.vue';

const misClientes = ref([]);
const clienteAEditar = ref(null);
const filaAbierta = ref(null);
const mostrarModalNuevoCliente = ref(false);
const mostrarModalEditarCliente = ref(false);
const mostrarModalFiltros = ref(false);
const filtroEstado = ref('sinFiltros');
const terminoBusqueda = ref('');
const mostrarFicha = ref(false);
const clienteSeleccionado = ref(null);
const fechaInicio = ref('');
const fechaFinal = ref('');

const misColumnas = [
    { titulo: 'Id', campo: 'id' },
    { titulo: 'Nombre', campo: 'nombre' },
    { titulo: 'Cumpleaños', campo: 'fecha_cumpleaños' },
    { titulo: 'Numero de celular', campo: 'numero_celular' },
    { titulo: 'Fecha de Registro', campo: 'fecha_registro' },
    { titulo: 'Acciones', campo: 'acciones' }
];

const camposCliente = [
    { titulo: 'Nombre:', nombre: 'nombre', type: 'text', requerido: true },
    { titulo: 'Numero de celular:', nombre: 'numero_celular', type: 'tel', requerido: true, pattern: '[0-9 +]*', maxlength: '15' },
    { titulo: 'Fecha de Nacimiento:', nombre: 'fecha_cumpleaños', type: 'date', requerido: true }
];

onMounted(() => {
    cargarClientes();
});

const cargarClientes = async () => {
    const datos = await obtenerClientes();
    misClientes.value = datos;
};

const totalClientes = computed(() => {
    return clientesFiltrados.value.length;
});

const clientesFiltrados = computed(() => {
    let filtrados = misClientes.value;

    if (filtroEstado.value === 'activos') {
        filtrados = filtrados.filter(c => c.estado === 'Activo');
    } else if (filtroEstado.value === 'inactivos') {
        filtrados = filtrados.filter(c => c.estado === 'Inactivo');
    }
    if (terminoBusqueda.value) {
        const busqueda = terminoBusqueda.value.toLowerCase().trim();
        filtrados = filtrados.filter(cliente => cliente.nombre.toLowerCase().includes(busqueda) || cliente.numero_celular.includes(busqueda) || cliente.fecha_cumpleaños.includes(busqueda));
    }

    if (fechaInicio.value) {
        filtrados = filtrados.filter(cliente => {
            let fechaCorta = cliente.fecha_registro.slice(0, 10);
            return fechaCorta >= fechaInicio.value;
        });
    }

    if (fechaFinal.value) {
        filtrados = filtrados.filter(cliente => {
            let fechaCorta = cliente.fecha_registro.slice(0, 10);
            return fechaCorta <= fechaFinal.value;
        });
    }

    return filtrados;
});

const { paginaActual, itemsPorPagina, totalPaginas, paginasVisibles, itemsPaginados: clientesPaginados, textoPaginacion, primeraPagina, paginaAnterior, paginaSiguiente, ultimaPagina } = usePaginacion(clientesFiltrados, 1, 'Clientes', true);

const alternarMenuAcciones = id => {
    filaAbierta.value = filaAbierta.value === id ? null : id;
};

const cerrarTodo = () => {
    mostrarModalFiltros.value = false;
    filaAbierta.value = null;
};

const abrirModalEditarCliente = cliente => {
    clienteAEditar.value = cliente;
    mostrarModalNuevoCliente.value = true;
};

const abrirFicha = cliente => {
    clienteSeleccionado.value = cliente;
    mostrarFicha.value = true;
};

const alternarModalFiltros = () => {
    if (mostrarModalFiltros.value) {
        mostrarModalFiltros.value = false;
    } else {
        mostrarModalFiltros.value = true;
    }
};

const handleEnviar = datos => {
    if (clienteAEditar.value) {
        handleEditarCliente(datos);
    } else {
        handleCrearCliente(datos);
    }
};

const handleCrearCliente = async datosNuevoCliente => {
    await crearCliente(datosNuevoCliente);
    mostrarModalNuevoCliente.value = false;
    mostrarNotificacion('Cliente Creado con exito!');
    cargarClientes();
};
const handleEditarCliente = async datosClienteActualizado => {
    console.log('¡He recibido los datos para editar!', datosClienteActualizado);
    const id = clienteAEditar.value.id;
    await editarCliente(id, datosClienteActualizado);
    mostrarModalNuevoCliente.value = false;
    clienteAEditar.value = null;
    mostrarNotificacion('Cliente Actualizado con exito!');
    cargarClientes();
};

const handleActivarCliente = async cliente => {
    const id = cliente.id;
    await activarCliente(id);
    filaAbierta.value = null;
    mostrarNotificacion('Cliente Reactivado con exito!');
    cargarClientes();
};
const handleDesactivarCliente = async cliente => {
    const id = cliente.id;
    await desactivarCliente(id);
    filaAbierta.value = null;
    mostrarNotificacion('Cliente Desactivado con exito');
    cargarClientes();
};
const handleEliminarCliente = async cliente => {
    const id = cliente.id;
    await eliminarCliente(id);
    filaAbierta.value = null;
    mostrarNotificacion('Cliente Eliminado con exito');
    cargarClientes();
};

const handleFechaFiltro = datos => {
    fechaInicio.value = datos.desde;
    fechaFinal.value = datos.hasta;
};

const handleLimpiarFiltros = () => {
    fechaInicio.value = '';
    fechaFinal.value = '';
    terminoBusqueda.value = '';
    filtroEstado.value = 'sinFiltros';
    paginaActual.value = 1;
};

watch(filtroEstado, () => (paginaActual.value = 1));

watch(terminoBusqueda, () => (paginaActual.value = 1));
</script>

<template>
    <Teleport to="body">
        <Transition name="toast">
            <BaseToast v-if="mensajeToast" :tipo="tipoNotificacion">
                <template #toastContent>
                    {{ mensajeToast }}
                </template>
            </BaseToast>
        </Transition>
        <ModalFicha v-if="mostrarFicha" tipo="Cliente" :item="clienteSeleccionado" alto="70%" @cerrar="mostrarFicha = false"></ModalFicha>
        <FormularioNuevoObjeto
            v-if="mostrarModalNuevoCliente"
            :titulo="clienteAEditar ? 'Editar Cliente' : 'Añadir Cliente'"
            :objetoAEditar="clienteAEditar"
            :campos="camposCliente"
            @enviar="handleEnviar"
            @cerrar="
                mostrarModalNuevoCliente = false;
                clienteAEditar = null;
            "></FormularioNuevoObjeto>
    </Teleport>
    <h1>Clientes</h1>
    <card class="card-clientes">
        <template v-slot:header-content>
            <h2>Clientes vista previa</h2>
            <div class="card-header-box">
                <input v-model="terminoBusqueda" class="buscar-cliente" type="text" name="buscar-cliente" id="" placeholder="Buscar Cliente" />
                <div class="buttons-box">
                    <button v-on:click="mostrarModalNuevoCliente = true" class="añadir-cliente">
                        <span>Añadir Cliente</span>
                    </button>
                    <button v-on:click="alternarModalFiltros" class="filtro-cliente">
                        <span>Filtrar</span>
                    </button>
                    <ModalFiltros v-if="mostrarModalFiltros" tipo="Cliente" :fecha-inicio="fechaInicio" :fecha-final="fechaFinal" @limpiar-filtros="handleLimpiarFiltros" :filtro-estado="filtroEstado" @cambiar-estado="nuevo => (filtroEstado = nuevo)" @filtro-fecha-registro="handleFechaFiltro"></ModalFiltros>
                </div>
            </div>
        </template>
        <tabla-contenido min-height="27rem" @fila-click="abrirFicha" class="tabla-clientes" :datos="clientesPaginados" :columnas="misColumnas" :clase-fila="fila => (fila.estado === 'Inactivo' ? 'cliente-inactivo' : '')">
            <template #fecha_cumpleaños="{ fila }">
                {{ formatearFecha(fila.fecha_cumpleaños) }}
            </template>
            <template #fecha_registro="{ fila }">
                {{ formatearFecha(fila.fecha_registro) }}
            </template>
            <template #acciones="{ fila }">
                <Acciones tipo="Cliente" :item="fila" :fila-abierta="filaAbierta" @abrir="abrirFicha" @editar="abrirModalEditarCliente" @alternar="alternarMenuAcciones" @activar="handleActivarCliente" @desactivar="handleDesactivarCliente" @eliminar="handleEliminarCliente"></Acciones>
            </template>
        </tabla-contenido>
        <template v-slot:footer-content>
            <div class="footer-box">
                <Paginacion :texto-paginacion="textoPaginacion" :paginas-visibles="paginasVisibles" :pagina-actual="paginaActual" @primera="primeraPagina" @siguiente="paginaSiguiente" @anterior="paginaAnterior" @ultima="ultimaPagina" @cambiar-pagina="nueva => (paginaActual = nueva)"></Paginacion>
            </div>
        </template>
    </card>
    <div v-if="filaAbierta || mostrarModalFiltros" class="invisible-click-listener" v-on:click="cerrarTodo"></div>
</template>

<style scoped>
.tabla-clientes {
    flex: 1;
    width: 100%;
}

:deep(.card-header) {
    flex-shrink: 0;
}

:deep(.card-footer) {
    flex-shrink: 0;
}

:deep(.tabla-clientes tbody tr:hover td) {
    background-color: var(--section-hover-color);
    cursor: pointer;
}

:deep(.cliente-inactivo td) {
    color: #a0a0a0;
    font-style: italic;
    background-color: #f9f9f9;
}

:deep(.cliente-inactivo .acciones) {
    color: black; /* O el color que desees */
    font-style: normal;
}

:deep(.cliente-inactivo:hover td) {
    background-color: #f2f2f2;
}

.card-clientes {
    width: 95%;
    height: 70%;
    margin: 0 1rem;
    align-self: center;
}

.card-clientes h2 {
    margin: 0 0 0 1rem;
    font-size: 25px;
}

.card-header-box {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-left: 2px solid var(--input-border-color);
    height: 70%;
    width: 60%;
    padding: 0 1rem;
}

.buscar-cliente {
    border-radius: 5px;
    width: 45%;
    height: 80%;
}

.buttons-box {
    position: relative;
    height: auto;
    display: flex;
    justify-content: center;
    gap: 1rem;
}

.footer-box {
    display: flex;
    padding: 0 0.5rem;
    justify-content: space-between;
}

.añadir-cliente {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 60%;
    height: 2rem;
}

.añadir-cliente span {
    text-align: center;
    font-size: 15px;
}

.filtro-cliente {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 2rem;
    width: 30%;
}

.invisible-click-listener {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: transparent;
    z-index: 5;
}
</style>
