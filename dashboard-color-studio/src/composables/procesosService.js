import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export const obtenerProcesos = async () => {
    try {
        const respuesta = await axios.get(`${API_URL}/procesos`);
        return respuesta.data;
    } catch (error) {
        console.error('Ha ocurrido un error: ', error);
        throw error;
    }
};
