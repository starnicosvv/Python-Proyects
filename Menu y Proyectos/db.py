import sqlite3

def inicializar_bd():
    conexion = sqlite3.connect("organizador.db")
    cursor = conexion.cursor()

    # Tabla de movimientos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movimientos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT NOT NULL,
        tipo TEXT CHECK(tipo IN ('ingreso','gasto')),
        categoria TEXT,
        monto REAL NOT NULL,
        descripcion TEXT
    )
    """)

    # Tabla de contactos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contactos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT,
        email TEXT
    )
    """)

    # Tabla de tareas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tareas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        descripcion TEXT,
        fecha_vencimiento TEXT,
        estado TEXT DEFAULT 'pendiente'
    )
    """)

    conexion.commit()
    conexion.close()