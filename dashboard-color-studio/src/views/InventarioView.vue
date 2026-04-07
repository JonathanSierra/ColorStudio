<script setup>
import { ref, onMounted, computed, watch } from 'vue';
import { obtenerProductos, activarProducto, crearProducto, desactivarProducto, editarProducto, eliminarProducto } from '../composables/productosService';
import { usePaginacion } from '../composables/paginacion';
import { formatearDinero } from '../utils/formatters';
import { formatearFecha } from '../utils/formatters';
import { mostrarNotificacion, mensajeToast, tipoNotificacion } from '../composables/globalService';
import TablaContenido from '../components/TablaContenido.vue';
import Card from '../components/Card.vue';
import ModalMasAcciones from '../components/ModalMasAcciones.vue';
import ModalFiltros from '../components/ModalFiltros.vue';
import BaseToast from '../components/BaseToast.vue';
import Acciones from '../components/Acciones.vue';
import Paginacion from '../components/Paginacion.vue';
import FormularioNuevoObjeto from '../components/FormularioNuevoObjeto.vue';

const misColumnas = [
    { titulo: 'Id', campo: 'id' },
    { titulo: 'Producto', campo: 'nombre' },
    { titulo: 'Categoria', campo: 'categoria' },
    { titulo: 'Stock', campo: 'stock' },
    { titulo: 'Precio', campo: 'precio' },
    { titulo: 'Acciones', campo: 'acciones' }
];

const camposProducto = [
    { titulo: 'Nombre:', nombre: 'nombre', type: 'text' },
    { titulo: 'Descripcion:', nombre: 'descripcion', type: 'text' },
    { titulo: 'Categoria:', nombre: 'categoria', type: 'text' },
    { titulo: 'Precio:', nombre: 'precio', type: 'number' },
    { titulo: 'Stock:', nombre: 'stock', type: 'number' }
];

const misProductos = ref([]);
const productoAEditar = ref(null);
const filaAbierta = ref(null);
const mostrarModalNuevoProducto = ref(false);
const mostrarModalEditarProducto = ref(false);
const mostrarModalFiltros = ref(false);
const filtroEstado = ref('sinFiltros');
const terminoBusqueda = ref('');
const mostrarFicha = ref(false);
const productoSeleccionado = ref(null);
const fechaInicio = ref('');
const fechaFinal = ref('');

onMounted(() => {
    cargarProductos();
});

const cargarProductos = async () => {
    const datos = await obtenerProductos();
    misProductos.value = datos;
};

const productosFiltrados = computed(() => {
    let filtrados = misProductos.value;

    if (filtroEstado.value === 'activos') {
        filtrados = filtrados.filter(c => c.activo === 1);
    } else if (filtroEstado.value === 'inactivos') {
        filtrados = filtrados.filter(c => c.activo === 0);
    }
    if (terminoBusqueda.value) {
        const busqueda = terminoBusqueda.value.toLowerCase().trim();
        filtrados = filtrados.filter(producto => producto.nombre.toLowerCase().includes(busqueda) || producto.categoria.toLowerCase().includes(busqueda) || producto.precio.toString().includes(busqueda));
    }

    return filtrados;
});

const { paginaActual, itemsPorPagina, totalPaginas, paginasVisibles, itemsPaginados: productosPaginados, textoPaginacion, primeraPagina, paginaAnterior, paginaSiguiente, ultimaPagina } = usePaginacion(productosFiltrados, 10, 'Productos');

const alternarMenuAcciones = id => {
    filaAbierta.value = filaAbierta.value === id ? null : id;
};

const cerrarTodo = () => {
    mostrarModalFiltros.value = false;
    filaAbierta.value = null;
};

const abrirModalEditarProducto = producto => {
    productoAEditar.value = producto;
    mostrarModalEditarProducto.value = true;
};

const abrirFicha = producto => {
    productoSeleccionado.value = producto;
    mostrarFicha.value = true;
};

const alternarModalFiltros = () => {
    if (mostrarModalFiltros.value) {
        mostrarModalFiltros.value = false;
    } else {
        mostrarModalFiltros.value = true;
    }
};

const handleCrearProducto = async datosNuevoProducto => {
    await crearProducto(datosNuevoProducto);
    mostrarModalNuevoProducto.value = false;
    mostrarNotificacion('Producto Creado con exito!');
    cargarProductos();
};
const handleEditarProducto = async datosProductoActualizado => {
    const id = productoAEditar.value.id;
    await editarProducto(id, datosProductoActualizado);
    mostrarModalEditarProducto.value = false;
    mostrarNotificacion('Producto Actualizado con exito!');
    cargarProductos();
};

const handleActivarProducto = async producto => {
    const id = producto.id;
    await activarProducto(id);
    filaAbierta.value = null;
    mostrarNotificacion('Producto Reactivado con exito!');
    cargarProductos();
};
const handleDesactivarProducto = async producto => {
    const id = producto.id;
    await desactivarProducto(id);
    filaAbierta.value = null;
    mostrarNotificacion('Producto Desactivado con exito');
    cargarProductos();
};
const handleEliminarProducto = async producto => {
    const id = producto.id;
    await eliminarProducto(id);
    filaAbierta.value = null;
    mostrarNotificacion('Producto Eliminado con exito');
    cargarProductos();
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
        <FormularioNuevoObjeto v-if="mostrarModalNuevoProducto" titulo="Añadir Producto" :campos="camposProducto" @enviar="handleCrearProducto" @cerrar="mostrarModalNuevoProducto = false"></FormularioNuevoObjeto>
    </Teleport>
    <h1>Inventario</h1>
    <card class="card-productos">
        <template v-slot:header-content>
            <h2>Productos vista previa</h2>
            <div class="card-header-box">
                <input v-model="terminoBusqueda" class="buscar-producto" type="text" name="buscar-producto" id="" placeholder="Buscar Producto" />
                <div class="buttons-box">
                    <button v-on:click="mostrarModalNuevoProducto = true" class="añadir-producto">
                        <span>Añadir producto</span>
                    </button>
                    <button v-on:click="alternarModalFiltros" class="filtro-producto">
                        <span>Filtrar</span>
                    </button>
                    <ModalFiltros v-if="mostrarModalFiltros" :fecha-inicio="fechaInicio" :fecha-final="fechaFinal" @limpiar-filtros="handleLimpiarFiltros" :filtro-estado="filtroEstado" @cambiar-estado="nuevo => (filtroEstado = nuevo)" @filtro-fecha-registro="handleFechaFiltro"></ModalFiltros>
                </div>
            </div>
        </template>
        <tabla-contenido min-height="27rem" @fila-click="abrirFicha" class="tabla-inventario" :datos="productosPaginados" :columnas="misColumnas" :clase-fila="fila => (fila.activo === 0 ? 'producto-inactivo' : '')">
            <template #precio="{ fila }">
                {{ formatearDinero(fila.precio) }}
            </template>
            <template #acciones="{ fila }">
                <Acciones tipo="Producto" :item="fila" :fila-abierta="filaAbierta" @editar="abrirModalEditarProducto" @alternar="alternarMenuAcciones" @activar="handleActivarProducto" @desactivar="handleDesactivarProducto" @eliminar="handleEliminarProducto"></Acciones>
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
h1 {
    padding: 0.5rem 0 0 10px;
    font-size: 30px;
}

.tabla-productos {
    flex: 1;
    width: 100%;
}

:deep(.card-header) {
    flex-shrink: 0;
}

:deep(.card-footer) {
    flex-shrink: 0;
}

:deep(.tabla-productos tbody tr td) {
    transition: all ease-in-out 80ms;
}

:deep(.tabla-productos tbody tr:hover td) {
    background-color: rgb(217, 228, 245);
    cursor: pointer;
}

:deep(.producto-inactivo td) {
    color: #a0a0a0;
    font-style: italic;
    background-color: #f9f9f9;
}

:deep(.producto-inactivo .acciones) {
    color: black; /* O el color que desees */
    font-style: normal;
}

:deep(.producto-inactivo:hover td) {
    background-color: #f2f2f2;
}

.card-productos {
    width: 95%;
    height: 70%;
    margin: 0 1rem;
    align-self: center;
}

.card-productos h2 {
    margin: 0 0 0 1rem;
    font-size: 25px;
}

.card-header-box {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-left: 2px solid rgb(228, 238, 246);
    height: 70%;
    width: 60%;
    padding: 0 1rem;
}

.buscar-producto {
    color: black;
    background-color: rgb(255, 255, 255);
    border: 2px solid rgb(228, 238, 246);
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

.añadir-producto {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: rgb(5, 148, 244);
    width: 60%;
    height: 2rem;
}

.añadir-producto span {
    text-align: center;
    font-size: 15px;
}

.filtro-producto {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: white;
    height: 2rem;
    color: rgb(5, 148, 244);
    border: 2px solid rgb(5, 148, 244);
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
