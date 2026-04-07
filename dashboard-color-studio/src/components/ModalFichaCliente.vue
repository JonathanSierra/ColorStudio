<script setup>
import { onMounted, ref } from 'vue';
import BaseModal from './BaseModal.vue';
import { eliminarSesion, obtenerHistorialDeCliente } from '../composables/historialService';
import { crearCita, editarCita, eliminarCita, obtenerCitasDeCliente } from '../composables/citasService';
import { mostrarNotificacion, mensajeToast, tipoNotificacion } from '../composables/globalService';
import Paginacion from './Paginacion.vue';
import AccionesCitas from './AccionesCitas.vue';
import { crearSesion } from '../composables/historialService';
import TablaContenido from './TablaContenido.vue';
import Card from './Card.vue';
import { formatearDinero } from '../utils/formatters';
import { formatearFecha } from '../utils/formatters';
import ModalNuevaCita from './ModalNuevaCita.vue';
import { usePaginacion } from '../composables/paginacion';
import ModalEditarCita from './ModalEditarCita.vue';
import AccionesHistorial from './AccionesHistorial.vue';

const props = defineProps(['cliente']);

const emits = defineEmits(['cerrar']);

const historial = ref([]);
const citas = ref([]);
const mostrarModalNuevaCita = ref(false);
const citaAEditar = ref(null);
const mostrarModalEditarCita = ref(false);
const filaAbierta = ref(null);

const { paginaActual: paginaActualHistorial, itemsPorPagina: itemsPorPaginaHistorial, totalPaginas: totalPaginasHistorial, paginasVisibles: paginasVisiblesHistorial, clientesPaginados: historialPaginado, textoPaginacion: textoPaginacionHistorial, primeraPagina: primeraPaginaHistorial, paginaAnterior: paginaAnteriorHistorial, paginaSiguiente: paginaSiguienteHistorial, ultimaPagina: ultimaPaginaHistorial } = usePaginacion(historial, 5, 'en historial');
const { paginaActual: paginaActualCitas, itemsPorPagina: itemsPorPaginaCitas, totalPaginas: totalPaginasCitas, paginasVisibles: paginasVisiblesCitas, clientesPaginados: citasPaginadas, textoPaginacion: textoPaginacionCitas, primeraPagina: primeraPaginaCitas, paginaAnterior: paginaAnteriorCitas, paginaSiguiente: paginaSiguienteCitas, ultimaPagina: ultimaPaginaCitas } = usePaginacion(citas, 5, 'citas');

const alternarMenuAcciones = id => {
    filaAbierta.value = filaAbierta.value === id ? null : id;
};

const abrirModalEditarCita = cita => {
    citaAEditar.value = cita;
    mostrarModalEditarCita.value = true;
};

const columnasHistorial = [
    { titulo: 'Proceso', campo: 'nombre_proceso' },
    { titulo: 'Fecha', campo: 'fecha_hora_sesion' },
    { titulo: 'Valor', campo: 'valor_sesion' },
    { titulo: 'Acciones', campo: 'acciones' }
];
const columnasCitas = [
    { titulo: 'Proceso', campo: 'nombre_proceso' },
    { titulo: 'Fecha', campo: 'fecha_hora_cita' },
    { titulo: 'Acciones', campo: 'acciones' }
];

onMounted(async () => {
    cargarCitas();
});

onMounted(async () => {
    cargarHistorial();
});

const cerrarTodo = () => {
    mostrarModalNuevaCita.value = false;
    mostrarModalEditarCita.value = false;
    filaAbierta.value = null;
};

const cargarCitas = async cliente => {
    const datos = await obtenerCitasDeCliente(props.cliente.id);
    citas.value = datos;
};

const cargarHistorial = async cliente => {
    const datos = await obtenerHistorialDeCliente(props.cliente.id);
    historial.value = datos;
};

const handleConfirmarCita = async (datosNuevaSesion, cliente) => {
    const sesionMapeada = {
        proceso_id: datosNuevaSesion.proceso_id,
        fecha_hora_sesion: datosNuevaSesion.fecha_hora_cita,
        valor_sesion: datosNuevaSesion.valor_proceso,
        cita_id: datosNuevaSesion.id
    };

    await crearSesion(sesionMapeada, props.cliente.id);
    cerrarTodo();
    mostrarNotificacion('Cita confirmada con exito!');
    await eliminarCita(sesionMapeada.cita_id);
    await cargarHistorial();
    await cargarCitas();
    if (paginaActualCitas.value > totalPaginasCitas.value) {
        if (totalPaginasCitas.value === 0) {
            paginaActualCitas.value = 1;
        } else {
            paginaActualCitas.value = totalPaginasCitas.value;
        }
    }
};

const handleCancelarCita = async cita => {
    await eliminarCita(cita.id);
    mostrarNotificacion('Cita Eliminada con exito!');
    cerrarTodo();
    cargarCitas();
};

const handleEliminarSesion = async sesion => {
    await eliminarSesion(sesion.id);
    mostrarNotificacion('Sesion Eliminada con exito!');
    cargarHistorial();
};

const handleEditarCita = async datosCitaActualizada => {
    const id = citaAEditar.value.id;
    await editarCita(datosCitaActualizada, id);
    mostrarModalEditarCita.value = false;
    mostrarNotificacion('Cita Actualizada con exito!');
    cargarCitas();
};

const handleCrearCita = async (datosNuevaCita, cliente) => {
    await crearCita(datosNuevaCita, props.cliente.id);
    mostrarModalNuevaCita.value = false;
    mostrarNotificacion('Cita creada con exito!');
    await cargarCitas();
};
</script>
<template>
    <Teleport to="body">
        <ModalEditarCita v-if="mostrarModalEditarCita" :cita="citaAEditar" @cerrar="mostrarModalEditarCita = false" @actualizar="handleEditarCita"></ModalEditarCita>
        <ModalNuevaCita v-if="mostrarModalNuevaCita" @cerrar="mostrarModalNuevaCita = false" @crear="handleCrearCita"></ModalNuevaCita>
    </Teleport>
    <BaseModal overflow="visible" ancho="60%" alto="70%" gap="1rem" @cerrar="$emit('cerrar')">
        <template #BaseModalHeader><h4>Ficha de Cliente</h4></template>
        <template #BaseModalMain>
            <div v-if="filaAbierta || mostrarModalNuevaCita" class="invisible-click-listener" v-on:click="cerrarTodo"></div>
            <div class="cliente-info">
                <h3>
                    Nombre: <span>{{ cliente.nombre }}</span>
                </h3>
                <h3>
                    Numero de telefono: <span>{{ cliente.numero_celular }}</span>
                </h3>
                <h3>
                    Fecha de Nacimiento: <span>{{ formatearFecha(cliente.fecha_cumpleaños) }}</span>
                </h3>
            </div>
            <div class="table-box">
                <Card class="card-historial">
                    <template #header-content><h4>Historial</h4></template>
                    <TablaContenido min-height="18rem" :datos="historialPaginado" :columnas="columnasHistorial" class="tabla-contenido">
                        <template #acciones="{ fila }">
                            <AccionesHistorial :sesion="fila" @eliminar="handleEliminarSesion"></AccionesHistorial>
                        </template>
                        <template #fecha_hora_sesion="{ fila }"> {{ formatearFecha(fila.fecha_hora_sesion) }}</template>
                        <template #valor_sesion="{ fila }">{{ formatearDinero(fila.valor_sesion) }}</template>
                    </TablaContenido>
                    <template #footer-content>
                        <!-- esto debe ser un component -->
                        <div class="footer-box">
                            <Paginacion :texto-paginacion="textoPaginacionHistorial" :paginas-visibles="paginasVisiblesHistorial" :pagina-actual="paginaActualHistorial" @primera="primeraPaginaHistorial" @siguiente="paginaSiguienteHistorial" @anterior="paginaAnteriorHistorial" @ultima="ultimaPaginaHistorial" @cambiar-pagina="nueva => (paginaActualHistorial = nueva)"></Paginacion>
                        </div>
                    </template>
                </Card>
                <Card class="card-citas">
                    <template #header-content>
                        <h4>Citas Pendientes</h4>
                        <button class="añadir-citas-button" v-on:click="mostrarModalNuevaCita = !mostrarModalNuevaCita">Añadir</button>
                    </template>
                    <TablaContenido min-height="18rem" :datos="citasPaginadas" :columnas="columnasCitas" class="tabla-contenido">
                        <template #acciones="{ fila }">
                            <AccionesCitas :cita="fila" :fila-abierta="filaAbierta" @editar="abrirModalEditarCita" @alternar="alternarMenuAcciones" @confirmar="handleConfirmarCita" @cancelar="handleCancelarCita"></AccionesCitas>
                        </template>
                        <template #fecha_hora_cita="{ fila }"> {{ formatearFecha(fila.fecha_hora_cita) }} </template>
                    </TablaContenido>
                    <template #footer-content>
                        <div class="footer-box">
                            <Paginacion :texto-paginacion="textoPaginacionCitas" :paginas-visibles="paginasVisiblesCitas" :pagina-actual="paginaActualCitas" @primera="primeraPaginaCitas" @siguiente="paginaSiguienteCitas" @anterior="paginaAnteriorCitas" @ultima="ultimaPaginaCitas" @cambiar-pagina="nueva => (paginaActualCitas = nueva)"></Paginacion>
                        </div>
                    </template>
                </Card>
            </div>
        </template>
        <template #BaseModalFooter></template>
    </BaseModal>
</template>
<style scoped>
* {
    color: black;
}

.cliente-info {
    display: flex;
    flex-wrap: wrap;
    width: 100%;
    padding: 0 1rem;
    justify-content: space-between;
}

.table-box {
    display: flex;
    gap: 1rem;
    width: 100%;
    height: 75%;
}

.tabla-contenido {
    width: 100%;
    overflow: visible;
}
.card-historial {
    width: 60%;
}

.card-citas {
    width: 40%;
}

.card-header button {
    display: flex;
    color: white;
    align-items: center;
    justify-content: center;
    width: 5rem;
    height: 60%;
    margin: 10px;
}

.footer-box {
    display: flex;
    padding: 0 0.5rem;
    justify-content: space-between;
}

.rowing {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 2rem;
}

.table-page {
    display: flex;
    gap: 10px;
    align-items: center;
    justify-content: space-evenly;
    height: 2rem;
}

.table-page button {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: white;
    width: 1rem;
    height: 1rem;
    border-radius: 100%;
    padding: 10px;
    color: black;
}

.table-page img {
    width: 20px;
    height: 20px;
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

span {
    font-weight: lighter;
}

h4 {
    margin: 0;
}

:deep(.modal-window) {
    overflow: visible;
}

:deep(.card-header) {
    padding: 0;
}

:deep(.card-footer) {
    height: auto;
}

.card-header h4 {
    margin-left: 10px;
}
</style>
