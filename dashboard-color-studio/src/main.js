import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import './style.css'
import App from './App.vue'
// Importamos las vistas (aun no existen, las crearemos enseguida)
import DashboardView from './views/DashboardView.vue'
import ClientesView from './views/ClientesView.vue'
// Configuramos las rutas
const routes = [
    { path: '/', component: DashboardView },
    { path: '/clientes', component: ClientesView }
]
const router = createRouter({
    history: createWebHistory(),
    routes
})
// Iniciamos la app y le conectamos el router
const app = createApp(App)
app.use(router)
app.mount('#app')