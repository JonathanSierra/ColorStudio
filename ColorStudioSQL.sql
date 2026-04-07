CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(255) NOT NULL,
    fecha_cumpleaños DATE,
    numero_celular VARCHAR,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS citas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    fecha_hora_cita DATETIME NOT NULL,
    estado TEXT DEFAULT 'Programada',
    proceso_id INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (proceso_id) REFERENCES procesos(id)
);
CREATE TABLE IF NOT EXISTS procesos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(255) NOT NULL,
    descripcion VARCHAR NOT NULL,
    precio INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    stock INTEGER DEFAULT 0,
    precio INTEGER NOT NULL,
    categoria TEXT
);
CREATE TABLE IF NOT EXISTS sesiones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    proceso_id INTEGER NOT NULL,
    fecha_hora_sesion DATETIME NOT NULL,
    valor_sesion INTEGER NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (proceso_id) REFERENCES procesos(id)
);
ALTER TABLE clientes DROP COLUMN activo;
-- INSERT INTO productos (nombre, descripcion, stock, precio, categoria) 
-- VALUES ('Shampoo de Argán', 'Nutrición profunda para cabellos secos - 500ml', 15, 45000, 'Capilar');
-- INSERT INTO productos (nombre, descripcion, stock, precio, categoria) 
-- VALUES ('Tinte Rubio Platino', 'Tinte profesional sin amoniaco', 24, 18000, 'Coloración');
-- INSERT INTO productos (nombre, descripcion, stock, precio, categoria) 
-- VALUES ('Cepillo Térmico', 'Cepillo para blower de alta resistencia', 8, 32000, 'Accesorios');
/* python -c "import sqlite3; con = sqlite3.connect('color_studio.db'); con.executescript(open('ColorStudioSQL.sql', encoding='utf-8').read()); con.close(); print('¡Base de datos creada con éxito!')" */