from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI(title="Color Studio API")

# Habilitar CORS para que el Frontend web pueda conectarse sin errores de seguridad
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permitir peticiones desde cualquier página web
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Función de ayuda para conectar a la Base de Datos
def get_db_connection():
    # Nos conectamos al archivo que creaste
    conn = sqlite3.connect('color_studio.db')
    # Esto hace que SQLite nos devuelva la info como diccionarios (columnas y valores) en lugar de listas
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
        
    # 3. Convertimos los resultados a un formato web (lista de diccionarios) y los devolvemos
    return [dict(cliente) for cliente in clientes_db]

# Aquí puedes agregar más adelante @app.get('/procesos') o @app.get('/productos')

@app.get("/procesos")
def get_procesos():
    with get_db_connection() as conn: 
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM procesos")
        procesos_db = cursor.fetchall()

    return [dict(proceso) for proceso in procesos_db]