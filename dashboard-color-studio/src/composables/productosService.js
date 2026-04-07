import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export const obtenerProductos = async () => {
    try {
        const respuesta = await axios.get(`${API_URL}/productos`);
        return respuesta.data;
    } catch (error) {
        console.error('Ha ocurrido un error: ', error);
        throw error;
    }
};

export const crearProducto = async datos => {
    try {
        const respuesta = await axios.post(`${API_URL}/añadirProducto`, datos);
        return respuesta.data;
    } catch (error) {
        console.error('Ha ocurrido un error: ', error);
        throw error;
    }
};

export const eliminarProducto = async id => {
    try {
        const respuesta = await axios.delete(`${API_URL}/eliminarProducto/${id}`);
        return respuesta.data;
    } catch (error) {
        console.error('Ha ocurrido un error: ', error);
        throw error;
    }
};

export const editarProducto = async (id, datos) => {
    try {
        const respuesta = await axios.put(`${API_URL}/editarProducto/${id}`, datos);
        return respuesta.data;
    } catch (error) {
        console.error('Ha ocurrido un error: ', error);
        throw error;
    }
};

export const activarProducto = async id => {
    try {
        const respuesta = await axios.patch(`${API_URL}/activarProducto/${id}`);
        return respuesta.data;
    } catch (error) {
        console.error('Ha ocurrido un error: ', error);
        throw error;
    }
};

export const desactivarProducto = async id => {
    try {
        const respuesta = await axios.patch(`${API_URL}/desactivarProducto/${id}`);
        return respuesta.data;
    } catch (error) {
        console.error('Ha ocurrido un error: ', error);
        throw error;
    }
};
