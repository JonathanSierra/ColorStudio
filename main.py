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

class NuevaCita(BaseModel):
    proceso_id: int
    fecha_hora_cita: str

class NuevaSesion(BaseModel):
    proceso_id: int
    fecha_hora_sesion: str
    valor_sesion: int

class NuevoProducto(BaseModel):
    nombre: str
    descripcion: str = "Sin Descripcion"
    categoria: str
    precio: int
    stock: int

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

@app.get("/productos")
def get_productos():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        productos_db = cursor.fetchall()

    return [dict(producto) for producto in productos_db]

@app.get("/procesos")
def get_procesos():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM procesos")
        procesos_db = cursor.fetchall()

    return [dict(proceso) for proceso in procesos_db]

@app.get("/historial/{cliente_id}")
def get_sesiones(cliente_id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT s.*, p.nombre as nombre_proceso FROM sesiones s
        JOIN procesos p ON s.proceso_id = p.id WHERE s.cliente_id = ?
        ORDER BY s.fecha_hora_sesion DESC""", (cliente_id,))
        historial = cursor.fetchall()

    return [dict(h) for h in historial]

@app.get("/citas/{cliente_id}")
def get_citas(cliente_id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT c.*, p.nombre as nombre_proceso, p.precio as valor_proceso FROM citas c JOIN procesos p ON c.proceso_id = p.id WHERE c.cliente_id = ?""", (cliente_id,))
        citas = cursor.fetchall()

    return [dict(c) for c in citas]

@app.post("/añadirCliente")
def add_cliente(cliente: NuevoCliente):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO clientes (nombre_producto, fecha_cumpleaños, numero_celular) VALUES (?,?,?)""",
                       (cliente.nombre, cliente.fecha_cumpleaños, cliente.numero_celular),)
        conn.commit()
        return {"mensaje": "Cliente guardado con exito!"}

@app.post("/añadirProducto")
def add_producto(producto: NuevoProducto):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO productos (nombre, descripcion, categoria, precio, stock) VALUES (?,?,?,?,?)""",
                       (producto.nombre, producto.descripcion, producto.categoria, producto.precio, producto.stock),)
        conn.commit()
        return {"mensaje": "Producto guardado con exito!"}

@app.post("/crearCita/{cliente_id}")
def add_cita(cliente_id: int, cita: NuevaCita):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO citas (cliente_id, fecha_hora_cita, proceso_id) VALUES (?,?,?)""", (cliente_id, cita.fecha_hora_cita, cita.proceso_id),)
        conn.commit()
        return {"mensaje": f"Cita asignada al cliente con el id: {cliente_id} con exito!"}

@app.post("/crearSesion/{cliente_id}")
def add_sesion(cliente_id: int, sesion: NuevaSesion):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO sesiones (cliente_id, proceso_id, fecha_hora_sesion, valor_sesion) VALUES (?,?,?,?)""",
                       (cliente_id, sesion.proceso_id, sesion.fecha_hora_sesion, sesion.valor_sesion),)
        conn.commit()
        return {"mensaje": f"Sesion asignada al historial del cliente con el id: {cliente_id} con exito!"}

    # Aquí puedes agregar más adelante @apps.get('/procesos') o
    # @app.get('/productos')
@app.delete("/eliminarCliente/{cliente_id}")
def delete_cliente(cliente_id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
        conn.commit()
        return {"mensaje": "Cliente eliminado con exito!"}

@app.delete("/eliminarProducto/{producto_id}")
def delete_producto(producto_id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
        conn.commit()
        return {"mensaje": "Producto eliminado con exito!"}

@app.delete("/eliminarCita/{cita_id}")
def delete_cita(cita_id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""DELETE FROM citas WHERE id = ?""", (cita_id,))
        conn.commit()
        return {"mensaje": "Cita eliminada con exito!"}

@app.delete("/eliminarSesion/{sesion_id}")
def delete_sesion(sesion_id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""DELETE FROM sesiones WHERE id = ?""", (sesion_id,))
        conn.commit()
        return {"mensaje": "Sesion eliminada con exito!"}

@app.put("/editarCliente/{cliente_id}")
def edit_cliente(cliente_id: int, cliente: NuevoCliente):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE clientes SET nombre=?, fecha_cumpleaños=?, numero_celular=? WHERE id=?",
            (cliente.nombre, cliente.fecha_cumpleaños, cliente.numero_celular, cliente_id,),)
        conn.commit()
        return {"mensaje": "Cliente Actualizado"}

@app.put("/editarProducto/{producto_id}")
def edit_producto(producto_id: int, producto: NuevoProducto):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE productos SET nombre=?, descripcion=?, categoria=?, precio=?, stock=? WHERE id=?",
            (producto.nombre, producto.descripcion, producto.categoria, producto.precio, producto.stock, producto_id,),)
        conn.commit()
        return {"mensaje": "Producto Actualizado"}

@app.put("/editarCita/{cita_id}")
def edit_cita(cita_id: int, cita: NuevaCita):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""UPDATE citas SET proceso_id=?, fecha_hora_cita=? WHERE id=?""", (cita.proceso_id, cita.fecha_hora_cita, cita_id))
        conn.commit()
        return {"mensaje": "Cita Actualizada"}

@app.patch("/activarCliente/{cliente_id}")
def activate_cliente(cliente_id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE clientes SET activo = 1 WHERE id = ?", (cliente_id,))
        conn.commit()
        return {"mensaje": "Cliente Activado"}

@app.patch("/activarProducto/{producto_id}")
def activate_producto(producto_id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE productos SET activo = 1 WHERE id = ?", (producto_id,))
        conn.commit()
        return {"mensaje": "Producto Activado"}

@app.patch("/desactivarCliente/{cliente_id}")
def deactivate_cliente(cliente_id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE clientes SET activo = 0 WHERE id = ?", (cliente_id,))
        conn.commit()
        return {"mensaje": "Cliente Desactivado"}

@app.patch("/desactivarProducto/{producto_id}")
def deactivate_producto(producto_id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE productos SET activo = 0 WHERE id = ?", (producto_id,))
        conn.commit()
        return {"mensaje": "Producto Desactivado"}
