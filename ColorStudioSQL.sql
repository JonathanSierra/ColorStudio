CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(255) NOT NULL,
    fecha_cumpleaños DATE,
    numero_celular VARCHAR,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE citas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    fecha_hora_cita DATETIME NOT NULL,
    estado TEXT DEFAULT 'Programada',
    proceso_id INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (proceso_id) REFERENCES procesos(id)
);
CREATE TABLE procesos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(255) NOT NULL,
    descripcion VARCHAR NOT NULL,
    precio INTEGER NOT NULL
);
CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(255) NOT NULL,
    marca VARCHAR(255) NOT NULL,
    precio INTEGER NOT NULL
);
CREATE TABLE sesiones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    proceso_id INTEGER NOT NULL,
    fecha_hora_sesion DATETIME NOT NULL,
    valor_sesion INTEGER NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (proceso_id) REFERENCES procesos(id)
);
/* python -c "import sqlite3; con = sqlite3.connect('color_studio.db'); con.executescript(open('ColorStudioSQL.sql', encoding='utf-8').read()); con.close(); print('¡Base de datos creada con éxito!')" */