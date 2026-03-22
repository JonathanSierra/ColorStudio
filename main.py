from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI(title="Color Studio API")

# Habilitar CORS para que el Frontend web pueda conectarse sin errores de
# seguridad
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir peticiones desde cualquier página web
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NuevoCliente(BaseModel):
    nombre: str
    fecha_cumpleaños: str
    numero_celular: str

# Función de ayuda para conectar a la Base de Datos
def get_db_connection():
    # Nos conectamos al archivo que creaste
    conn = sqlite3.connect("color_studio.db")
    # Esto hace que SQLite nos devuelva la info como diccionarios (columnas y
    # valores) en lugar de listas
    conn.row_factory = sqlite3.Row
    return conn

# ----- RUTAS DE LA API -----

# Esta es tu ruta principal, solo para probar que el servidor funciona
@app.get("/")
def read_root():
    return {"mensaje": "¡Bienvenido a la API de Color Studio!"}

# Esta ruta va a la Base de Datos y trae a tus clientes
@app.get("/clientes")
def get_clientes():
    # 1. Abrimos conexión a la BD usando el "with" que aprendimos
    with get_db_connection() as conn:
        cursor = conn.cursor()
        # 2. Hacemos la consulta SQL igualita que en la consola
        cursor.execute("SELECT * FROM clientes")
        clientes_db = cursor.fetchall()

    # 3. Convertimos los resultados a un formato web (lista de diccionarios) y
    # los devolvemos
    return [dict(cliente) for cliente in clientes_db]

# Aquí puedes agregar más adelante @app.get('/procesos') o
# @app.get('/productos')
@app.delete("/eliminarCliente/{cliente_id}")
def delete_cliente(cliente_id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
        conn.commit()
        return {"mensaje": "Cliente eliminado"}

@app.put("/editarCliente/{cliente_id}")
def edit_cliente(cliente_id: int, cliente: NuevoCliente):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE clientes SET nombre=?, fecha_cumpleaños=?, numero_celular=? WHERE id=?",
            (cliente.nombre, cliente.fecha_cumpleaños, cliente.numero_celular, cliente_id,),)
        conn.commit()
        return {"mensaje": "Cliente Actualizado"}

@app.patch("/desactivarCliente/{cliente_id}")
def deactivate_cliente(cliente_id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE clientes SET activo = 0 WHERE id = ?", (cliente_id,))
        conn.commit()
        return {"mensaje": "Cliente Desactivado"}

@app.patch("/activarCliente/{cliente_id}")
def activate_cliente(cliente_id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE clientes SET activo = 1 WHERE id = ?", (cliente_id,))
        conn.commit()
        return {"mensaje": "Cliente Activado"}

@app.post("/añadirCliente")
def add_cliente(cliente: NuevoCliente):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO clientes (nombre, fecha_cumpleaños, numero_celular)VALUES (?,?,?)""",
                       (cliente.nombre, cliente.fecha_cumpleaños, cliente.numero_celular),)
        conn.commit()
        return {"mensaje": "Cliente guardado con exito!"}

@app.get("/procesos")
def get_procesos():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM procesos")
        procesos_db = cursor.fetchall()

    return [dict(proceso) for proceso in procesos_db]
