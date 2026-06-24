import sqlite3
from datetime import datetime
from rich.table import Table
from rich.console import Console

DB_NAME = "organizador.db"


# -------------------------------
# Funciones CRUD
# -------------------------------
def agregar_tarea(titulo, descripcion, fecha_vencimiento):
    # Validar campos vacíos
    if not titulo or not descripcion or not fecha_vencimiento:
        print("❌ Error: Ningún campo puede quedar vacío.")
        return

    # Validar fecha
    try:
        fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        print("❌ Error: La fecha debe estar en formato YYYY-MM-DD.")
        return

    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO tareas (titulo, descripcion, fecha_vencimiento) VALUES (?,?,?)",  
                   (titulo, descripcion, fecha_vencimiento))
    conexion.commit()
    conexion.close()
    print("✅ Tarea agregada exitosamente.")


def buscar_tarea(titulo):
    if not titulo:
        print("❌ Error: Debes ingresar un título para buscar.")
        return None

    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tareas WHERE titulo=?", (titulo,))
    tarea = cursor.fetchone()
    conexion.close()

    if tarea:
        return tarea
    else:
        print("ℹ️ No se encontró la tarea.")
        return None


def eliminar_tarea(titulo):
    if not titulo:
        print("❌ Error: Debes ingresar un título para eliminar.")
        return False

    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM tareas WHERE titulo=?", (titulo,))
    conexion.commit()
    conexion.close()
    print("✅ Tarea eliminada (si existía).")
    return True


def mostrar_tareas():
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("SELECT id, titulo, descripcion, fecha_vencimiento, estado FROM tareas")
    filas = cursor.fetchall()
    conexion.close()

    if not filas:
        print("ℹ️ No hay tareas registradas.")
    else:
        table = Table(title="📋 Lista de Tareas")
        table.add_column("ID", justify="center")
        table.add_column("Título", justify="center")
        table.add_column("Descripción", justify="center")
        table.add_column("Fecha Vencimiento", justify="center")
        table.add_column("Estado", justify="center")

        for tid, titulo, descripcion, fecha, estado in filas:
            table.add_row(str(tid), titulo, descripcion, fecha, estado)

        console = Console()
        console.print(table)

# -------------------------------
# Funciones extra
# -------------------------------
def editar_tarea(id_tarea, nuevo_titulo=None, nueva_descripcion=None, nueva_fecha=None):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()

    if nuevo_titulo:
        cursor.execute("UPDATE tareas SET titulo=? WHERE id=?", (nuevo_titulo, id_tarea))
    if nueva_descripcion:
        cursor.execute("UPDATE tareas SET descripcion=? WHERE id=?", (nueva_descripcion, id_tarea))
    if nueva_fecha:
        try:
            nueva_fecha = datetime.strptime(nueva_fecha, "%Y-%m-%d").strftime("%Y-%m-%d")
            cursor.execute("UPDATE tareas SET fecha_vencimiento=? WHERE id=?", (nueva_fecha, id_tarea))
        except ValueError:
            print("❌ Error: La fecha debe estar en formato YYYY-MM-DD.")
            conexion.close()
            return

    conexion.commit()
    conexion.close()
    print("✅ Tarea actualizada exitosamente.")


def marcar_tarea_completada(id_tarea):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("UPDATE tareas SET estado='completada' WHERE id=?", (id_tarea,))
    conexion.commit()
    conexion.close()
    print("✅ Tarea marcada como completada.")
