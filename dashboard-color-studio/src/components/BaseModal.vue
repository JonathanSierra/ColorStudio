<script setup>
const emits = defineEmits(['cerrar']);

const props = defineProps({
    overflow: {
        type: String,
        default: 'hidden'
    },
    alto: {
        type: String,
        default: '60%'
    },
    ancho: {
        type: String,
        default: '50%'
    },
    gap: {
        type: String,
        default: '3rem'
    }
});
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
    overflow: v-bind(overflow);
    flex-direction: column;
    border-radius: 20px;
    width: v-bind(ancho);
    height: v-bind(alto);
    background-color: rgb(228, 238, 246);
}

.modal-window header {
    overflow: hidden;
    display: flex;
    border-radius: 20px 20px 0 0;
    align-items: center;
    padding: 1rem;
    background-color: white;
    color: black;
}

.modal-window main {
    display: flex;
    padding: 1rem;
    justify-content: space-between;
    gap: v-bind(gap);
    flex-wrap: wrap;
    flex: 1;
}

.modal-window footer {
    display: flex;
    justify-content: end;
    gap: 1rem;
    border-radius: 0 0 20px 20px;
    background-color: white;
    color: black;
    padding: 1rem;
}
</style>
