<template>
    <div class="panel-wrap">
        <slot name="menu-lateral"></slot>
        <div class="panel">
            <div class="panel-header">
                <div class="user-box">

                    <h2>Bievenida...</h2>
                    <img class="icon-img"
                        src="../assets/images/notifications_24dp_000000_FILL0_wght400_GRAD0_opsz24.png"
                        alt="Notificaciones">
                    <img class="user-img"></img>
                </div>
            </div>
            <slot></slot>
        </div>
    </div>
</template>
<style scoped>
.panel-wrap {
    background-color: rgba(255, 255, 255, 0.418);
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
    background-color: rgb(228, 238, 246);
}

.panel-header {
    display: flex;
    justify-content: end;
    align-items: center;
    width: 100%;
    background-color: rgb(255, 255, 255);
    height: 3.5rem;
    border-radius: 0 35px 0 0;
    color: black;
}

.user-box {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0 1rem 0 0;
}

.icon-img {
    width: 1.6rem;
    height: 1.6rem;
}

.user-img {
    border-radius: 100%;
    border: 2px solid red;
    width: 2.6rem;
    height: 2.6rem;
}

h2 {
    margin: 5px 20px;
    font-size: 20px;
}
</style>