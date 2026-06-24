import sqlite3
from rich.table import Table
from rich.console import Console

DB_NAME = "organizador.db"

def agregar_contacto(nombre, telefono, email):
    if not nombre or not telefono or not email:
        print("❌ Error: Ningún campo puede quedar vacío.")
        return

    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO contactos (nombre, telefono, email) VALUES (?,?,?)",
                   (nombre, telefono, email))
    conexion.commit()
    conexion.close()
    print("✅ Contacto agregado exitosamente.")


def buscar_contacto(nombre):
    if not nombre:
        print("❌ Error: Debes ingresar un nombre para buscar.")
        return None

    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM contactos WHERE nombre=?", (nombre,))
    contacto = cursor.fetchone()
    conexion.close()

    if contacto:
        return contacto
    else:
        print("ℹ️ No se encontró el contacto.")
        return None


def eliminar_contacto(nombre):
    if not nombre:
        print("❌ Error: Debes ingresar un nombre para eliminar.")
        return False

    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM contactos WHERE nombre=?", (nombre,))
    conexion.commit()
    conexion.close()
    print("✅ Contacto eliminado (si existía).")
    return True


def mostrar_contactos():
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, telefono, email FROM contactos")
    filas = cursor.fetchall()
    conexion.close()

    if not filas:
        print("ℹ️ No hay contactos registrados.")
    else:
        table = Table(title="📒 Agenda de Contactos")
        table.add_column("ID", justify="center")
        table.add_column("Nombre", justify="center")
        table.add_column("Teléfono", justify="center")
        table.add_column("Email", justify="center")

        for cid, nombre, telefono, email in filas:
            # Evita errores si algún campo es None
            table.add_row(str(cid),
                          nombre if nombre else "",
                          telefono if telefono else "",
                          email if email else "")

        console = Console()
        console.print(table)

