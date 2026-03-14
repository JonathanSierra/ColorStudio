<script setup>
import Background from './components/Background.vue';
import Panel from './components/Panel.vue';
import MenuLateral from './components/MenuLateral.vue';
</script>
<template>
  <div class="app-container">
    <!-- Aquí irá tu hermoso menú lateral luego -->
    <Background>
      <Panel>
        <template v-slot:menu-lateral>
          <MenuLateral></MenuLateral>
        </template>
        <main class="main-content">
          <router-view></router-view>
        </main>
      </Panel>
    </Background>
    <!-- Router-view es la "ventana" donde Vue Router va a inyectar las páginas -->
  </div>
</template>
<style>
/* Un reseteo básico para que el fondo se vea bien */
.app-container {
  min-width: 100%;
  background-color: #f3f4f6;
  /* Un gris muy suave y moderno */
  font-family: 'Inter', sans-serif;
}

.main {
  display: flex;
  flex-direction: column;
  align-items: center;
  color: black;
  height: 100vh;
}
</style>