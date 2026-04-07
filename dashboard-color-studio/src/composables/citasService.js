import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export const obtenerCitasDeCliente = async cliente_id => {
    try {
        const respuesta = await axios.get(`${API_URL}/citas/${cliente_id}`);
        return respuesta.data;
    } catch (error) {
        console.error('Ha ocurrido un error: ', error);
        throw error;
    }
};

export const eliminarCita = async cita_id => {
    try {
        const respuesta = await axios.delete(`${API_URL}/eliminarCita/${cita_id}`);
        return respuesta.data;
    } catch (error) {
        console.error('Ha ocurrido un error: ', error);
        throw error;
    }
};

export const crearCita = async (datos, cliente_id) => {
    try {
        const respuesta = await axios.post(`${API_URL}/crearCita/${cliente_id}`, datos);
        return respuesta.data;
    } catch (error) {
        console.error('Ha ocurrido un error: ', error);
        throw error;
    }
};

export const editarCita = async (datos, cita_id) => {
    try {
        const respuesta = await axios.put(`${API_URL}/editarCita/${cita_id}`, datos);
        return respuesta.data;
    } catch (error) {
        console.error('Ha ocurrido un error: ', error);
        throw error;
    }
};
