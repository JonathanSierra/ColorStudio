import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export const obtenerHistorialDeCliente = async id => {
    try {
        const respuesta = await axios.get(`${API_URL}/historial/${id}`);
        return respuesta.data;
    } catch (error) {
        console.error('Ha ocurrido un error: ', error);
        throw error;
    }
};

export const eliminarSesion = async id => {
    try {
        const respuesta = await axios.delete(`${API_URL}/eliminarSesion/${id}`);
        return respuesta.data;
    } catch (error) {
        throw error;
    }
};

export const crearSesion = async (datos, id) => {
    try {
        const respuesta = await axios.post(`${API_URL}/crearSesion/${id}`, datos);
        return respuesta.data;
    } catch (error) {
        throw error;
    }
};
