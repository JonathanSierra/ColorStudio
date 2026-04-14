<script setup>
import { ref, watch } from 'vue';

const isDark = ref(localStorage.getItem('theme') === 'true');

watch(isDark, (newValue) => {
    document.documentElement.classList.toggle('dark', isDark.value)

    localStorage.setItem('theme', newValue)
},
    { immediate: true })
</script>
<template>
    <div class="panel-wrap">
        <slot name="menu-lateral"></slot>
        <div class="panel">
            <div class="panel-header">
                <div class="toggle-mode">
                    <input v-model="isDark" type="checkbox" class="checkbox" id="checkbox">
                    <label for="checkbox" class="checkbox-label">
                        <font-awesome-icon icon="fa-solid fa-moon" style="color: rgb(255, 255, 255);" />
                        <font-awesome-icon icon="fa-solid fa-sun" style="color: rgb(255, 255, 255);" />
                    <span class="ball"></span>
                    </label>
                </div>
                <div class="user-box">
                    <h2>Bienvenida Carolina Ramirez</h2>
                    <img class="user-img" src="../assets/images/Carolina_Ramirez.png"></img>
                </div>
            </div>
            <slot></slot>
        </div>
    </div>
</template>
<style scoped>
.panel-wrap {
    background-color: var(--wrapper-color);
    border-radius: 35px;
    padding: 1rem;
    display: flex;
    width: 90%;
    height: 85%;
}

.panel {
    display: flex;
    flex-direction: column;
    z-index: 0;
    width: 95%;
    height: 100%;
    border-radius: 0 35px 35px 0;
    background-color: var(--bg-color);
}

.panel-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    background-color: var(--bg-card-color);
    height: 3.5rem;
    border-radius: 0 35px 0 0;
    color: var(--text-primary-color);
}

.user-box {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0 2rem 0 0;
}

.icon-img {
    width: 1.6rem;
    height: 1.6rem;
}

.user-img {
    border-radius: 100%;
    width: 2rem;
    height: 2rem;
}

h2 {
    margin: 5px 20px;
    font-size: 20px;
}

* {box-sizing: border-box;}

.toggle-mode{
    margin-left: 1rem;
}

body {
  font-family: "Montserrat", sans-serif;
  background-color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  text-align: center;
  min-height: 100vh;
  margin: 0;
  transition: background 0.2s linear;
}

body.dark {background-color: #292c35;} /* #9b59b6 */

body.dark h1, body.dark .support a {color: #fff;}

.checkbox {
  opacity: 0;
  position: absolute;
}

.checkbox-label {
  background-color: var(--accent-color);
  width: 50px;
  height: 26px;
  border-radius: 50px;
  position: relative;
  padding: 5px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.fa-moon {color: #f1c40f;}

.fa-sun {color: #f39c12;}

.checkbox-label .ball {
  background-color: #fff;
  width: 22px;
  height: 22px;
  position: absolute;
  left: 2px;
  top: 2px;
  border-radius: 50%;
  transition: transform 0.2s linear;
}

.checkbox:checked + .checkbox-label .ball {
  transform: translateX(24px);
}

/*  Support me if you like it */
.support {
	position: absolute;
	right: 20px;
	bottom: 20px;
}

.support a {
  color: #292c35;
  font-size: 32px;
  backface-visibility: hidden;
  display: inline-block;
  transition: transform 0.2s ease;
}

.support a:hover{
  transform: scale(1.1);
}
</style>