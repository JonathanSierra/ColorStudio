<script setup>
import { computed, onMounted, ref } from 'vue';
import BaseModal from './BaseModal.vue';
import { eliminarSesion, obtenerHistorialDeCliente } from '../composables/historialService';
import { crearCita, editarCita, eliminarCita, obtenerCitasDeCliente } from '../composables/citasService';
import { mostrarNotificacion, mensajeToast, tipoNotificacion } from '../composables/globalService';
import Paginacion from './Paginacion.vue';
import Acciones from './Acciones.vue';
import { crearSesion } from '../composables/historialService';
import TablaContenido from './TablaContenido.vue';
import Card from './Card.vue';
import { formatearDinero } from '../utils/formatters';
import { formatearFecha } from '../utils/formatters';
import { usePaginacion } from '../composables/paginacion';
import FormularioNuevoObjeto from '../components/FormularioNuevoObjeto.vue';
import { obtenerProcesos } from '../composables/procesosService';

const props = defineProps(['item', 'tipo', 'alto']);

const emits = defineEmits(['cerrar']);

const historial = ref([]);
const citas = ref([]);
const mostrarModalNuevaCita = ref(false);
const citaAEditar = ref(null);
const mostrarModalEditarCita = ref(false);
const filaAbierta = ref(null);
const procesos = ref([]);

const { paginaActual: paginaActualHistorial, itemsPorPagina: itemsPorPaginaHistorial, totalPaginas: totalPaginasHistorial, paginasVisibles: paginasVisiblesHistorial, itemsPaginados: historialPaginado, textoPaginacion: textoPaginacionHistorial, primeraPagina: primeraPaginaHistorial, paginaAnterior: paginaAnteriorHistorial, paginaSiguiente: paginaSiguienteHistorial, ultimaPagina: ultimaPaginaHistorial } = usePaginacion(historial, 5, 'en historial');
const { paginaActual: paginaActualCitas, itemsPorPagina: itemsPorPaginaCitas, totalPaginas: totalPaginasCitas, paginasVisibles: paginasVisiblesCitas, itemsPaginados: citasPaginadas, textoPaginacion: textoPaginacionCitas, primeraPagina: primeraPaginaCitas, paginaAnterior: paginaAnteriorCitas, paginaSiguiente: paginaSiguienteCitas, ultimaPagina: ultimaPaginaCitas } = usePaginacion(citas, 5, 'citas');

onMounted(async () => {
    if (props.tipo === 'Cliente') {
        procesos.value = await obtenerProcesos();
    }
});

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

const camposCita = computed(() => [
    { titulo: 'Proceso:', nombre: 'proceso_id', type: 'select', requerido: true, opciones: procesos.value },
    { titulo: 'Fecha:', nombre: 'fecha_hora_cita', type: 'datetime-local', requerido: true }
]);

onMounted(async () => {
    if (props.tipo === 'Cliente') {
        cargarCitas();
    }
});

onMounted(async () => {
    if (props.tipo === 'Cliente') {
        cargarHistorial();
    }
});

const cerrarTodo = () => {
    mostrarModalNuevaCita.value = false;
    mostrarModalEditarCita.value = false;
    filaAbierta.value = null;
};

const cargarCitas = async () => {
    const datos = await obtenerCitasDeCliente(props.item.id);
    citas.value = datos;
};

const cargarHistorial = async () => {
    const datos = await obtenerHistorialDeCliente(props.item.id);
    historial.value = datos;
};

const handleConfirmarCita = async datosNuevaSesion => {
    const sesionMapeada = {
        proceso_id: datosNuevaSesion.proceso_id,
        fecha_hora_sesion: datosNuevaSesion.fecha_hora_cita,
        valor_sesion: datosNuevaSesion.valor_proceso,
        cita_id: datosNuevaSesion.id
    };

    await crearSesion(sesionMapeada, props.item.id);
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

const handleCrearCita = async datosNuevaCita => {
    await crearCita(datosNuevaCita, props.item.id);
    mostrarModalNuevaCita.value = false;
    mostrarNotificacion('Cita creada con exito!');
    await cargarCitas();
};
</script>
<template>
    <Teleport to="body">
        <FormularioNuevoObjeto v-if="mostrarModalEditarCita" ancho="32%" alto="40%" titulo="Editar Cita" :campos="camposCita" :objetoAEditar="citaAEditar" @enviar="handleEditarCita" @cerrar="mostrarModalEditarCita = false" @actualizar="handleEditarCita"></FormularioNuevoObjeto>
        <FormularioNuevoObjeto v-if="mostrarModalNuevaCita" ancho="32%" alto="40%" titulo="Añadir Cita" :campos="camposCita" @enviar="handleCrearCita" @cerrar="mostrarModalNuevaCita = false"></FormularioNuevoObjeto>
    </Teleport>
    <BaseModal overflow="visible" ancho="60%" alto="alto" gap="1rem" @cerrar="$emit('cerrar')">
        <template #BaseModalHeader
            ><h4>Ficha de {{ tipo }}</h4></template
        >
        <template #BaseModalMain>
            <div v-if="filaAbierta || mostrarModalNuevaCita" class="invisible-click-listener" v-on:click="cerrarTodo"></div>
            <div v-if="tipo === 'Cliente'" class="item-info">
                <h3>
                    Nombre: <span>{{ props.item.nombre }}</span>
                </h3>
                <h3>
                    Numero de telefono: <span>{{ props.item.numero_celular }}</span>
                </h3>
                <h3>
                    Fecha de Nacimiento: <span>{{ formatearFecha(props.item.fecha_cumpleaños) }}</span>
                </h3>
            </div>
            <div v-if="tipo === 'Producto'" class="item-info">
                <h3>
                    Nombre: <span>{{ props.item.nombre }}</span>
                </h3>
                <h3>
                    Categoria: <span>{{ props.item.categoria }}</span>
                </h3>
                <h3>
                    Descripcion: <span>{{ props.item.descripcion }}</span>
                </h3>
                <h3>
                    Precio: <span>{{ formatearDinero(props.item.precio) }}</span>
                </h3>
                <h3>
                    Stock: <span>{{ props.item.stock }}</span>
                </h3>
            </div>
            <div v-if="tipo === 'Cliente'" class="table-box">
                <Card class="card-historial">
                    <template #header-content><h4>Historial</h4></template>
                    <TablaContenido v-if="tipo === 'Cliente'" min-height="18rem" :datos="historialPaginado" :columnas="columnasHistorial" class="tabla-contenido">
                        <template #acciones="{ fila }">
                            <Acciones tipo="Sesion" :item="fila" @eliminar="handleEliminarSesion"></Acciones>
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
                    <TablaContenido v-if="tipo === 'Cliente'" min-height="18rem" :datos="citasPaginadas" :columnas="columnasCitas" class="tabla-contenido">
                        <template #acciones="{ fila }">
                            <Acciones tipo="Cita" :item="fila" :fila-abierta="filaAbierta" @editar="abrirModalEditarCita" @alternar="alternarMenuAcciones" @confirmar="handleConfirmarCita" @cancelar="handleCancelarCita"></Acciones>
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
.item-info {
    display: grid;
    grid-template-columns: 1fr 1fr;
    width: 100%;
    padding: 1.5rem;
    gap: 1.5rem;
}

.item-info h3 {
    margin: 0;
    font-weight: bold;
}

.item-info h3:first-child {
    grid-column: 1 / span 2;
    font-size: 1.4rem;
    border-bottom: 2px solid var(--input-border-color);
    padding-bottom: 10px;
}

.item-info h3 span {
    font-weight: lighter;
    display: inline-block;
    margin-left: 5px;
}

.item-info h3:nth-child(odd):not(:first-child) {
    text-align: right;
    justify-self: end;
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
    width: 1rem;
    height: 1rem;
    border-radius: 100%;
    padding: 10px;
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
