<script setup>
const secciones = [
    { titulo: "Dashboard", descripcion: "Presiona para ver una vista general del negocio.", img: new URL("../assets/images/home_30dp_000000_FILL0_wght400_GRAD0_opsz24.png", import.meta.url).href },
    { titulo: "Clientes", descripcion: "Presiona para ver y gestionar a tus clientes.", img: new URL("../assets/images/group_30dp_000000_FILL0_wght400_GRAD0_opsz24.png", import.meta.url).href },
    { titulo: "Inventario", descripcion: "Presiona para ver y gestionar tu inventario.", img: new URL("../assets/images/inventory_30dp_000000_FILL0_wght400_GRAD0_opsz24.png", import.meta.url).href },
    { titulo: "Configuracion", descripcion: "Presiona para ver la configuracion de la aplicacion.", img: new URL("../assets/images/settings_30dp_000000_FILL0_wght400_GRAD0_opsz24.png", import.meta.url).href },
    { titulo: "Ayuda", descripcion: "Presiona para ver el panel de ayuda del usuario.", img: new URL("../assets/images/help_30dp_000000_FILL0_wght400_GRAD0_opsz24.png", import.meta.url).href }
]

</script>

<template>
    <div class="menuLateral">
        <header>
            <div class="logo"></div>
        </header>
        <div class="secciones">
            <li v-for="seccion in secciones" class="seccion">
                <img :src="seccion.img" alt="Icon"> {{ seccion.titulo }}
            </li>
        </div>
        <slot>

        </slot>
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
    border: 2px solid red;
    border-radius: 35px 0 0 0;
}

.logo {
    border-radius: 100%;
    width: 5rem;
    height: 5rem;
    border: 2px solid red;
}

.secciones {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin: 0.5rem;
    padding: 0.3rem;
    border: 2px solid red;
}

.seccion {
    display: flex;
    align-items: center;
    transition: ease-in-out 125ms;
    gap: 5px;
    color: black;
    font-size: 22px;
    border: 2px solid red;
}

.seccion:hover {
    background-color: rgb(196, 217, 235);
    cursor: pointer;
}
</style>