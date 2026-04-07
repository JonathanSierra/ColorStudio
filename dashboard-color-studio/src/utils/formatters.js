export const formatearDinero = monto => {
    return new Intl.NumberFormat('es-CO', {
        style: 'currency',
        currency: 'COP',
        minimumFractionDigits: 0
    }).format(monto);
};

export const formatearFecha = fecha => {
    if (!fecha) return '';
    if (!fecha.includes(':')) {
        const [año, mes, dia] = fecha.split('-');
        return `${dia}/${mes}/${año}`;
    } else {
        const objetoFecha = new Date(fecha);
        const fechaFormateada = objetoFecha.toLocaleDateString('es-CO', { day: '2-digit', month: '2-digit', year: 'numeric' });
        const horaFormateada = objetoFecha.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        return `${fechaFormateada} - ${horaFormateada}`;
    }
};
