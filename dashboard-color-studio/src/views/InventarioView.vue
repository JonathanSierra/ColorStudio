<script setup>
import { ref } from 'vue';
import { onMounted } from 'vue';
import { obtenerProductos } from '../composables/productosService';
import { usePaginacion } from '../composables/paginacion';
import { formatearDinero } from '../utils/formatters';

const misColumnas = [
    { titulo: 'Id', campo: 'id' },
    { titulo: 'Producto', campo: 'nombre' },
    { titulo: 'Categoria', campo: 'categoria' },
    { titulo: 'Stock', campo: 'stock' },
    { titulo: 'Precio', campo: 'precio' },
    { titulo: 'Acciones', campo: 'acciones' }
];

const { itemsPaginados, paginaActual } = usePaginacion(productos, 10, 'productos');

const productos = ref([]);

onMounted(() => {
    cargarProductos();
});

const cargarProductos = async () => {
    const datos = await obtenerProductos();
    productos.value = datos;
};
</script>
<template>
    <h1>Inventario</h1>
    <card class="card-productos">
        <template v-slot:header-content>
            <h2>productos vista previa</h2>
            <div class="card-header-box">
                <input v-model="terminoBusqueda" class="buscar-producto" type="text" name="buscar-producto" id="" placeholder="Buscar producto" />
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
        <tabla-contenido min-height="27rem" @fila-click="abrirFicha" class="tabla-inventario" :datos="productos" :columnas="misColumnas" :clase-fila="fila => (fila.activo === 0 ? 'producto-inactivo' : '')">
            <template #fecha_cumpleaños="{ fila }">
                {{ formatearFecha(fila.fecha_cumpleaños) }}
            </template>
            <template #fecha_registro="{ fila }">
                {{ formatearFecha(fila.fecha_registro) }}
            </template>
            <template #acciones="{ fila }">
                <Acciones :producto="fila" :fila-abierta="filaAbierta" @editar="abrirModalEditarproducto" @alternar="alternarMenuAcciones" @activar="handleActivarproducto" @desactivar="handleDesactivarproducto" @eliminar="handleEliminarproducto"></Acciones>
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
</style>
