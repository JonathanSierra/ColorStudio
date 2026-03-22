<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import TablaContenido from '../components/TablaContenido.vue';
import Card from '../components/Card.vue';
import ModalNuevoCliente from '../components/ModalNuevoCliente.vue';
import ModalEditarCliente from '../components/ModalEditarCliente.vue';
import ModalMasAcciones from '../components/ModalMasAcciones.vue';
import ModalFiltros from '../components/ModalFiltros.vue';

const misClientes = ref([]);
const clienteAEditar = ref(null);
const paginaActual = ref(1);
const itemsPorPagina = ref(5);
const filaAbierta = ref(null);
const mostrarModalNuevoCliente = ref(false);
const mostrarModalEditarCliente = ref(false);
const mostrarModalFiltros = ref(false);
const mostrarClientesInactivos = ref(false);

const misColumnas = [
    { titulo: 'Id', campo: 'id' },
    { titulo: 'Nombre', campo: 'nombre' },
    { titulo: 'Cumpleaños', campo: 'fecha_cumpleaños' },
    { titulo: 'Numero de celular', campo: 'numero_celular' },
    { titulo: 'Fecha de Registro', campo: 'fecha_registro' },
    { titulo: 'Acciones', campo: 'acciones' }
];

onMounted(() => {
    cargarClientes();
});

const cargarClientes = async () => {
    const respuesta = await axios.get('http://127.0.0.1:8000/clientes');
    misClientes.value = respuesta.data;
    console.log('Total Clientes = ' + totalClientes.value);
    console.log('Total Paginas = ' + totalPaginas.value);
};

const clientesPaginados = computed(() => {
    const inicio = (paginaActual.value - 1) * itemsPorPagina.value;
    const fin = inicio + itemsPorPagina.value;

    return clientesFiltrados.value.slice(inicio, fin);
});

const totalClientes = computed(() => {
    return clientesFiltrados.value.length;
});

const totalPaginas = computed(() => {
    return Math.ceil(totalClientes.value / itemsPorPagina.value);
});

const clientesFiltrados = computed(() => {
    if (mostrarClientesInactivos.value) {
        return misClientes.value.filter(cliente => cliente.activo === 0);
    } else {
        return misClientes.value.filter(cliente => cliente.activo === 1);
    }
});

const textoPaginacion = computed(() => {
    const inicio = (paginaActual.value - 1) * itemsPorPagina.value + 1;
    const calculo = paginaActual.value * itemsPorPagina.value;
    const fin = Math.min(calculo, totalClientes.value);
    return `Mostrando ${inicio} - ${fin} de ${totalClientes.value} clientes`;
});

const alternarMenuAcciones = id => {
    filaAbierta.value = filaAbierta.value === id ? null : id;
};

const formatearFecha = fecha => {
    if (!fecha) return '';
    const [año, mes, dia] = fecha.split('-');
    return `${dia}/${mes}/${año}`;
};

const cerrarTodo = () => {
    mostrarModalFiltros.value = false;
    filaAbierta.value = null;
};

// Botones para moverse entre paginas
const primeraPagina = () => {
    paginaActual.value = 1;
};

const paginaAnterior = () => {
    if (paginaActual.value > 1) {
        paginaActual.value = paginaActual.value - 1;
    }
};

const paginaSiguiente = () => {
    if (paginaActual.value < totalPaginas.value) {
        paginaActual.value = paginaActual.value + 1;
    }
};

const ultimaPagina = () => {
    paginaActual.value = totalPaginas.value;
};
// -----------------------------------------------------

const paginasVisibles = computed(() => {
    let inicio = Math.max(1, paginaActual.value - 2);
    let final = Math.min(totalPaginas.value, inicio + 4);

    if (final === totalPaginas.value) {
        inicio = Math.max(1, final - 4);
    }

    const rango = [];
    for (let i = inicio; i <= final; i++) {
        rango.push(i);
    }

    return rango;
});

const abrirModalEditarCliente = cliente => {
    clienteAEditar.value = cliente;
    mostrarModalEditarCliente.value = true;
};

const alternarModalFiltros = () => {
    if (mostrarModalFiltros.value) {
        mostrarModalFiltros.value = false;
    } else {
        mostrarModalFiltros.value = true;
    }
};

const guardarNuevoCliente = async datosNuevoCliente => {
    await axios.post('http://127.0.0.1:8000/añadirCliente', datosNuevoCliente);
    mostrarModalNuevoCliente.value = false;
    cargarClientes();
};
const guardarClienteActualizado = async datosClienteActualizado => {
    const id = clienteAEditar.value.id;
    await axios.put(`http://127.0.0.1:8000/editarCliente/${id}`, datosClienteActualizado);
    mostrarModalEditarCliente.value = false;
    cargarClientes();
};

const activarCliente = async cliente => {
    const id = cliente.id;
    await axios.patch(`http://127.0.0.1:8000/activarCliente/${id}`);
    filaAbierta.value = null;
    cargarClientes();
};
const desactivarCliente = async cliente => {
    const id = cliente.id;
    await axios.patch(`http://127.0.0.1:8000/desactivarCliente/${id}`);
    filaAbierta.value = null;
    cargarClientes();
};
</script>

<template>
    <Teleport to="body">
        <ModalEditarCliente v-if="mostrarModalEditarCliente" :cliente="clienteAEditar" @cerrar="mostrarModalEditarCliente = false" @actualizar="guardarClienteActualizado"></ModalEditarCliente>
        <ModalNuevoCliente v-if="mostrarModalNuevoCliente" @cerrar="mostrarModalNuevoCliente = false" @crear="guardarNuevoCliente"></ModalNuevoCliente>
    </Teleport>
    <h1>Clientes</h1>
    <card class="card-clientes">
        <template v-slot:header-content>
            <h2>Clientes vista previa</h2>
            <div class="card-header-box">
                <input class="buscar-cliente" type="text" name="buscar-cliente" id="" placeholder="Buscar cliente" />
                <div class="buttons-box">
                    <button v-on:click="mostrarModalNuevoCliente = true" class="añadir-cliente">
                        <span>Añadir Cliente</span>
                    </button>
                    <button v-on:click="alternarModalFiltros" class="filtro-cliente">
                        <span>Filtrar</span>
                    </button>
                    <ModalFiltros v-if="mostrarModalFiltros" @activos="mostrarClientesInactivos = false" @inactivos="mostrarClientesInactivos = true" @por-fecha=""></ModalFiltros>
                </div>
            </div>
        </template>
        <tabla-contenido class="tabla-clientes" :datos="clientesPaginados" :columnas="misColumnas">
            <template #fecha_cumpleaños="{ fila }">
                {{ formatearFecha(fila.fecha_cumpleaños) }}
            </template>
            <template #acciones="{ fila }">
                <div class="acciones">
                    <button class="editar" v-on:click="abrirModalEditarCliente(fila)"><img src="../assets/images/edit_35dp_000000_FILL0_wght400_GRAD0_opsz40.png" alt="editar" /></button>
                    <button class="mas-acciones" v-on:click="alternarMenuAcciones(fila.id)"><img src="../assets/images/more_vert_35dp_000000_FILL0_wght400_GRAD0_opsz40.png" alt="mas acciones" /></button>
                    <ModalMasAcciones v-if="filaAbierta === fila.id" :cliente="fila" @activar="activarCliente" @desactivar="desactivarCliente"></ModalMasAcciones>
                </div>
            </template>
        </tabla-contenido>
        <template v-slot:footer-page-actions>
            <div class="footer-box">
                <div class="rowing">
                    <span>{{ textoPaginacion }}</span>
                </div>
                <div class="table-page">
                    <button v-on:click="primeraPagina"><img src="../assets/images/first_page_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" /></button>
                    <button v-on:click="paginaAnterior"><img src="../assets/images/keyboard_arrow_left_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" /></button>
                    <button v-for="pagina in paginasVisibles" :key="pagina" v-on:click="paginaActual = pagina" :class="{ 'boton-activo': paginaActual === pagina }">{{ pagina }}</button>
                    <button v-on:click="paginaSiguiente"><img src="../assets/images/keyboard_arrow_right_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" /></button>
                    <button v-on:click="ultimaPagina"><img src="../assets/images/last_page_30dp_000000_FILL0_wght400_GRAD0_opsz24.png" alt="" /></button>
                </div>
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
    border-left: 2px solid rgb(228, 238, 246);
    height: 70%;
    width: 60%;
    padding: 0 1rem;
}

.buscar-cliente {
    color: black;
    background-color: rgb(255, 255, 255);
    border: 2px solid rgb(228, 238, 246);
    border-radius: 5px;
    width: 45%;
    height: 95%;
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

.añadir-cliente {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: rgb(5, 148, 244);
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
    background-color: white;
    height: 2rem;
    color: rgb(5, 148, 244);
    border: 2px solid rgb(5, 148, 244);
    width: 30%;
}

.acciones {
    position: relative;
    display: flex;
    justify-content: center;
    gap: 0.5rem;
}
.mas-acciones {
    display: flex;
    padding: 0;
    background-color: rgba(255, 255, 255, 0);
}
.editar {
    display: flex;
    padding: 0;
    background-color: rgba(255, 255, 255, 0);
}
.mas-acciones img {
    align-self: center;
    width: 20px;
    height: 20px;
}
.editar img {
    align-self: center;
    width: 20px;
    height: 20px;
}

.boton-activo {
    color: white !important;
    background-color: rgb(5, 148, 244) !important;
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
