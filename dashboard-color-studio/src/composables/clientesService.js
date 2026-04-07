import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export const obtenerClientes = async () => {
    try {
        const respuesta = await axios.get(`${API_URL}/clientes`);
        return respuesta.data;
    } catch (error) {
        console.error('Ha ocurrido un error: ', error);
        throw error;
    }
};

export const crearCliente = async datos => {
    try {
        const respuesta = await axios.post(`${API_URL}/añadirCliente`, datos);
        return respuesta.data;
    } catch (error) {
        console.error('Ha ocurrido un error: ', error);
        throw error;
    }
};

export const eliminarCliente = async id => {
    try {
        const respuesta = await axios.delete(`${API_URL}/eliminarCliente/${id}`);
        return respuesta.data;
    } catch (error) {
        console.error('Ha ocurrido un error: ', error);
        throw error;
    }
};

export const editarCliente = async (id, datos) => {
    try {
        const respuesta = await axios.put(`${API_URL}/editarCliente/${id}`, datos);
        return respuesta.data;
    } catch (error) {
        console.error('Ha ocurrido un error: ', error);
        throw error;
    }
};

export const activarCliente = async id => {
    try {
        const respuesta = await axios.patch(`${API_URL}/activarCliente/${id}`);
        return respuesta.data;
    } catch (error) {
        console.error('Ha ocurrido un error: ', error);
        throw error;
    }
};

export const desactivarCliente = async id => {
    try {
        const respuesta = await axios.patch(`${API_URL}/desactivarCliente/${id}`);
        return respuesta.data;
    } catch (error) {
        console.error('Ha ocurrido un error: ', error);
        throw error;
    }
};
