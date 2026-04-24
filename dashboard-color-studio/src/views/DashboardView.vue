<script setup>
import axios from 'axios';
import { ref, computed } from 'vue';
import TablaContenido from '../components/TablaContenido.vue';
import { onMounted } from 'vue';
import Card from '../components/Card.vue';
import { usePaginacion } from '../composables/paginacion';
import { formatearFecha } from '../utils/formatters';
import Paginacion from '../components/Paginacion.vue';
import Acciones from '../components/Acciones.vue';
import FormularioNuevoObjeto from '../components/FormularioNuevoObjeto.vue';
import { obtenerProcesos } from '../composables/procesosService';
import { crearSesion } from '../composables/historialService';
import { eliminarCita } from '../composables/citasService';
import { editarCita } from '../composables/citasService';
import { mostrarNotificacion } from '../composables/globalService';

const columnasCitasHoy = [
    { titulo: 'Cliente', campo: 'nombre_cliente' },
    { titulo: 'Proceso', campo: 'nombre_proceso' },
    { titulo: 'Fecha', campo: 'fecha_hora_cita' },
    { titulo: 'Acciones', campo: 'acciones' }
];

const citas = ref([]);
const filaAbierta = ref(null);
const mostrarModalNuevaCita = ref(false);
const mostrarModalEditarCita = ref(false);
const citaAEditar = ref(null);
const procesos = ref([]);

const { paginaActual: paginaActualCitasHoy, itemsPorPagina: itemsPorPaginaCitasHoy, totalPaginas: totalPaginasCitasHoy, paginasVisibles: paginasVisiblesCitasHoy, itemsPaginados: citasHoyPaginadas, textoPaginacion: textoPaginacionCitasHoy, primeraPagina: primeraPaginaCitasHoy, paginaAnterior: paginaAnteriorCitasHoy, paginaSiguiente: paginaSiguienteCitasHoy, ultimaPagina: ultimaPaginaCitasHoy } = usePaginacion(citas, 5, 'citas', true);

const camposCita = computed(() => [
    { titulo: 'Proceso:', nombre: 'proceso_id', type: 'select', requerido: true, opciones: procesos.value },
    { titulo: 'Fecha:', nombre: 'fecha_hora_cita', type: 'datetime-local', requerido: true }
]);

onMounted(async () => {
    cargarCitas();
    cargarProcesos();
});

const cargarCitas = async () => {
    const respuesta = await axios.get('http://127.0.0.1:8000/citas');
    citas.value = respuesta.data;
    console.log(citas.value);
};

const cargarProcesos = async () => {
    const respuesta = await axios.get('http://127.0.0.1:8000/procesos');
    procesos.value = respuesta.data;
    console.log(procesos.value);
};

const handleConfirmarCita = async cita => {
    const sesionMapeada = {
        proceso_id: cita.proceso_id,
        fecha_hora_sesion: cita.fecha_hora_cita,
        valor_sesion: cita.valor_proceso,
        cita_id: cita.id
    };

    await crearSesion(sesionMapeada, cita.cliente_id);
    cerrarTodo();
    mostrarNotificacion('Cita confirmada con exito!');
    await eliminarCita(sesionMapeada.cita_id);
    await cargarCitas();
    if (paginaActualCitasHoy.value > totalPaginasCitasHoy.value) {
        if (totalPaginasCitasHoy.value === 0) {
            paginaActualCitasHoy.value = 1;
        } else {
            paginaActualCitasHoy.value = totalPaginasCitasHoy.value;
        }
    }
};

const alternarMenuAcciones = id => {
    filaAbierta.value = filaAbierta.value === id ? null : id;
};

const abrirModalEditarCita = cita => {
    citaAEditar.value = cita;
    mostrarModalEditarCita.value = true;
};

const cerrarTodo = () => {
    mostrarModalNuevaCita.value = false;
    mostrarModalEditarCita.value = false;
    filaAbierta.value = null;
};

const handleCancelarCita = async cita => {
    await eliminarCita(cita.id);
    mostrarNotificacion('Cita Eliminada con exito!');
    cerrarTodo();
    cargarCitas();
};

const handleEditarCita = async datosCitaActualizada => {
    const id = citaAEditar.value.id;
    await editarCita(datosCitaActualizada, id);
    mostrarModalEditarCita.value = false;
    mostrarNotificacion('Cita Actualizada con exito!');
    cargarCitas();
};
</script>
<template>
    <Teleport to="body">
        <FormularioNuevoObjeto v-if="mostrarModalEditarCita" ancho="32%" alto="40%" titulo="Editar Cita" :campos="camposCita" :objetoAEditar="citaAEditar" @enviar="handleEditarCita" @cerrar="mostrarModalEditarCita = false" @actualizar="handleEditarCita"></FormularioNuevoObjeto>
    </Teleport>
    <h1>Dashboard</h1>
    <div class="cards-container">
        <Card class="citas-hoy">
            <template v-slot:header-content>
                <h2>Citas para hoy</h2>
            </template>
            <TablaContenido :columnas="columnasCitasHoy" :datos="citasHoyPaginadas">
                <template #fecha_hora_cita="{ fila }"> {{ formatearFecha(fila.fecha_hora_cita) }} </template>
                <template #acciones="{ fila }">
                    <Acciones tipo="Cita" :item="fila" :fila-abierta="filaAbierta" @editar="abrirModalEditarCita" @alternar="alternarMenuAcciones" @confirmar="handleConfirmarCita" @cancelar="handleCancelarCita"></Acciones>
                </template>
                <template v-slot:footer-content>
                    <div class="footer-box">
                        <Paginacion :texto-paginacion="textoPaginacionCitasHoy" :paginas-visibles="paginasVisiblesCitasHoy" :pagina-actual="paginaActualCitasHoy" @primera="primeraPaginaCitasHoy" @siguiente="paginaSiguienteCitasHoy" @anterior="paginaAnteriorCitasHoy" @ultima="ultimaPaginaCitasHoy" @cambiar-pagina="nueva => (paginaActualCitasHoy = nueva)"></Paginacion>
                    </div>
                </template>
            </TablaContenido>
        </Card>
        <Card class="cumpleaños-proximos">
            <template v-slot:header-content>
                <h2>Proximos Cumpleaños</h2>
            </template>
            <ul class="lista-cumpleaños-proximos">
                <li><img src="../assets/images/cake_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" />Cita</li>
            </ul>
        </Card>
    </div>
</template>

<style scoped>
.cards-container {
    display: flex;
    justify-content: space-between;
    margin: 0 2rem;
    height: 40%;
    gap: 2rem;
}

.card-header {
    width: 100%;
    height: 20%;
    background-color: rgb(249, 186, 207);
    border-radius: 30px 30px 0 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.lista-citas-proximos {
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    width: 95%;
    height: 80%;
    align-self: center;
    margin: 0;
}
.lista-cumpleaños-proximos {
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    width: 95%;
    height: 80%;
    align-self: center;
    margin: 0;
    padding: 0;
}

li {
    display: flex;
    border: 2px solid red;
    align-items: center;
}

li img {
    border: 2px solid red;
    width: 30px;
    height: 30px;
    background-color: rgb(249, 186, 207);
    border-radius: 30px;
    padding: 4px;
    margin: 0 5px;
}

.citas-hoy {
    width: 60%;
    height: 100%;
}

.citas-hoy h2 {
    margin: 0 0 0 1rem;
    font-size: 20px;
}

.cumpleaños-proximos {
    width: 25%;
    height: 100%;
}

.cumpleaños-proximos h2 {
    margin: 0 0 0 1rem;
    font-size: 20px;
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
</style>
