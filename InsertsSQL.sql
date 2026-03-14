INSERT INTO clientes (nombre, fecha_cumpleaños, numero_celular)
VALUES ("Agatha", "16/02/1996", "3243452532"),
    ("Rebecca", "08/06/1994", "3115362344"),
    ("Victoria", "25/05/2000", "3126874956");
INSERT INTO procesos (nombre, descripcion, precio)
VALUES (
        "Balayage",
        "Decoloración y matiz técnica barrido",
        150000
    ),
    (
        "Corte Clásico",
        "Corte con tijera, lavado y secado",
        35000
    ),
    (
        "Uñas Acrílicas",
        "Set completo de acrílico un tono",
        60000
    );
/* python -c "import sqlite3; con = sqlite3.connect('color_studio.db'); con.executescript(open('InsertsSQL.sql', encoding='utf-8').read()); con.close(); print('¡Datos insertados con éxito!')" */