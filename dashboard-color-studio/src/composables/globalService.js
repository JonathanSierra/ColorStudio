import { ref } from 'vue';

export const mensajeToast = ref('');
export const tipoNotificacion = ref('exito');

export const mostrarNotificacion = (texto, tipo = 'exito') => {
    mensajeToast.value = texto;
    tipoNotificacion.value = tipo;
    setTimeout(() => {
        mensajeToast.value = '';
    }, 3000);
};
