<script setup>
const secciones = [
    { titulo: 'Dashboard', descripcion: 'Presiona para ver una vista general del negocio.', img: new URL('../assets/images/home_30dp_000000_FILL0_wght400_GRAD0_opsz24.png', import.meta.url).href, ruta: '/' },
    { titulo: 'Clientes', descripcion: 'Presiona para ver y gestionar a tus clientes.', img: new URL('../assets/images/group_30dp_000000_FILL0_wght400_GRAD0_opsz24.png', import.meta.url).href, ruta: '/clientes' },
    { titulo: 'Inventario', descripcion: 'Presiona para ver y gestionar tu inventario.', img: new URL('../assets/images/inventory_30dp_000000_FILL0_wght400_GRAD0_opsz24.png', import.meta.url).href, ruta: '/inventario' },
    { titulo: 'Configuracion', descripcion: 'Presiona para ver la configuracion de la aplicacion.', img: new URL('../assets/images/settings_30dp_000000_FILL0_wght400_GRAD0_opsz24.png', import.meta.url).href, ruta: '/configuracion' },
    { titulo: 'Ayuda', descripcion: 'Presiona para ver el panel de ayuda del usuario.', img: new URL('../assets/images/help_30dp_000000_FILL0_wght400_GRAD0_opsz24.png', import.meta.url).href, ruta: '/ayuda' }
];
</script>

<template>
    <div class="menuLateral">
        <header>
            <div class="logo"><b>logo</b></div>
        </header>
        <div class="secciones">
            <router-link v-for="seccion in secciones" :to="seccion.ruta">
                <li class="seccion"><img :src="seccion.img" alt="Icon" class="seccion-icon" /> {{ seccion.titulo }}</li>
            </router-link>
        </div>
        <slot> </slot>
    </div>
</template>
<style scoped>
.menuLateral {
    display: flex;
    flex-direction: column;
    z-index: 1;
    width: 20%;
    height: 100%;
    border-radius: 35px 0 0 35px;
    background-color: rgb(163, 206, 241);
}

header {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 15%;
    padding: 15px 0 20px 0;
    border-radius: 35px 0 0 0;
}

.logo {
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 100%;
    width: 5rem;
    height: 5rem;
    border: 2px solid black;
}

.secciones {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin: 0.5rem;
    padding: 0.3rem;
}

.seccion {
    display: flex;
    align-items: center;
    transition: ease-in-out 125ms;
    padding-left: 10px;
    border-radius: 10px;
    gap: 5px;
    color: black;
    font-size: 22px;
}

.seccion:hover {
    background-color: rgb(196, 217, 235);
    cursor: pointer;
}

.seccion-icon {
    width: 20px;
    height: 20px;
}

.router-link-active .seccion {
    background-color: rgb(196, 217, 235);
}
</style>
