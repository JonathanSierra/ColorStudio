import { computed, onMounted, onUnmounted, ref } from 'vue';

export function usePaginacion(fuenteDeDatos, itemsPorPaginaInicial = 5, nombreDeFuente = 'nombreDeFuente', esDinamico = false) {
    const paginaActual = ref(1);
    const itemsPorPagina = ref(itemsPorPaginaInicial);

    const totalPaginas = computed(() => {
        return Math.ceil(fuenteDeDatos.value.length / itemsPorPagina.value);
    });

    const itemsPaginados = computed(() => {
        const inicio = (paginaActual.value - 1) * itemsPorPagina.value;
        const fin = inicio + itemsPorPagina.value;

        return fuenteDeDatos.value.slice(inicio, fin);
    });

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

    const textoPaginacion = computed(() => {
        const inicio = (paginaActual.value - 1) * itemsPorPagina.value + 1;
        const calculo = paginaActual.value * itemsPorPagina.value;
        const fin = Math.min(calculo, fuenteDeDatos.value.length);
        return `Mostrando ${inicio} - ${fin} de ${fuenteDeDatos.value.length} ${nombreDeFuente}`;
    });

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
            paginaActual.value++;
        }
    };

    const ultimaPagina = () => {
        paginaActual.value = totalPaginas.value;
    };
    // -----------------------------------------------------

    const calcularItemsPorPagina = () => {
        const alturaPantalla = window.innerHeight;
        if (alturaPantalla > 1000) return 10;
        if (alturaPantalla > 800) return 8;
        return 5;
    };

    const actualizarDimensiones = () => {
        if (esDinamico) {
            itemsPorPagina.value = calcularItemsPorPagina();
        }
        paginaActual.value = 1;
    };

    onMounted(() => {
        if (esDinamico) {
            actualizarDimensiones();
            window.addEventListener('resize', actualizarDimensiones);
        }
    });

    onUnmounted(() => {
        if (esDinamico) {
            window.removeEventListener('resize', actualizarDimensiones);
        }
    });

    return {
        paginaActual,
        itemsPorPagina,
        totalPaginas,
        paginasVisibles,
        itemsPaginados,
        textoPaginacion,
        primeraPagina,
        paginaAnterior,
        paginaSiguiente,
        ultimaPagina
    };
}
