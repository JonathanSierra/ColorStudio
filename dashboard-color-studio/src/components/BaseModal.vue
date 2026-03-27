<script setup>
const emits = defineEmits(['cerrar']);
</script>

<template>
    <Teleport to="body">
        <div class="backdrop" @click.self="$emit('cerrar')">
            <div class="modal-window">
                <header>
                    <slot name="BaseModalHeader"></slot>
                </header>
                <main>
                    <slot name="BaseModalMain"></slot>
                </main>
                <footer>
                    <slot name="BaseModalFooter"></slot>
                </footer>
            </div>
        </div>
    </Teleport>
</template>

<style scoped>
.backdrop {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 2;
    background-color: rgba(0, 0, 0, 0.412);
    width: 100dvw;
    height: 100dvh;
}

.modal-window {
    display: flex;
    overflow: hidden;
    flex-direction: column;
    border-radius: 20px;
    width: 50%;
    height: 60%;
    background-color: rgb(228, 238, 246);
}

.modal-window header {
    overflow: hidden;
    display: flex;
    align-items: center;
    padding: 1rem;
    background-color: white;
    color: black;
}

.modal-window main {
    display: flex;
    padding: 1rem;
    justify-content: space-between;
    gap: 3rem;
    flex-wrap: wrap;
    flex: 1;
}

.modal-window footer {
    display: flex;
    justify-content: end;
    gap: 1rem;
    background-color: white;
    color: black;
    padding: 1rem;
}
</style>
