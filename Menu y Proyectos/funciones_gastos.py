import sqlite3
from rich.table import Table
from rich.console import Console
from datetime import datetime
import csv

DB_NAME = "organizador.db"

# -------------------------------
# Funciones de Movimientos
# -------------------------------

def agregar_movimiento(tipo, descripcion, categoria, monto, fecha):
    # Validar campos vacíos
    if not tipo or not descripcion or not categoria or not monto or not fecha:
        print("❌ Error: Ningún campo puede quedar vacío.")
        return

    # Validar tipo
    if tipo.lower() not in ["ingreso", "gasto"]:
        print("❌ Error: El tipo debe ser 'ingreso' o 'gasto'.")
        return

    # Validar monto
    try:
        monto = float(monto)
        if monto <= 0:
            print("❌ Error: El monto debe ser mayor a 0.")
            return
    except ValueError:
        print("❌ Error: El monto debe ser un número válido.")
        return

    # Validar fecha
    try:
        fecha = datetime.strptime(fecha, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        print("❌ Error: La fecha debe estar en formato YYYY-MM-DD.")
        return

    # Insertar en la base
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO movimientos (fecha,tipo,categoria,monto,descripcion) VALUES (?,?,?,?,?)",
        (fecha, tipo, categoria, monto, descripcion)
    )
    conexion.commit()
    conexion.close()

    log_movimiento({"fecha": fecha, "tipo": tipo, "categoria": categoria, "monto": monto, "descripcion": descripcion})
    print("✅ Movimiento agregado exitosamente.")


def buscar_movimiento(descripcion, tipo=None):
    if not descripcion:
        print("❌ Error: Debes ingresar una descripción para buscar.")
        return None

    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    if tipo:
        cursor.execute("SELECT * FROM movimientos WHERE descripcion=? AND tipo=?", (descripcion, tipo))
    else:
        cursor.execute("SELECT * FROM movimientos WHERE descripcion=?", (descripcion,))
    resultado = cursor.fetchone()
    conexion.close()

    if resultado:
        return resultado
    else:
        print("ℹ️ No se encontró el movimiento.")
        return None


def eliminar_movimiento(descripcion, tipo=None):
    if not descripcion:
        print("❌ Error: Debes ingresar una descripción para eliminar.")
        return False

    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    if tipo:
        cursor.execute("DELETE FROM movimientos WHERE descripcion=? AND tipo=?", (descripcion, tipo))
    else:
        cursor.execute("DELETE FROM movimientos WHERE descripcion=?", (descripcion,))
    conexion.commit()
    conexion.close()
    print("✅ Movimiento eliminado (si existía).")
    return True


def mostrar_movimientos():
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("SELECT id, tipo, descripcion, categoria, monto, fecha FROM movimientos")
    filas = cursor.fetchall()
    conexion.close()

    if not filas:
        print("ℹ️ No hay movimientos registrados.")
    else:
        table = Table(title="📊 Movimientos")
        table.add_column("ID", justify="center")
        table.add_column("Tipo", justify="center")
        table.add_column("Descripción", justify="center")
        table.add_column("Categoría", justify="center")
        table.add_column("Monto", justify="center")
        table.add_column("Fecha", justify="center")

        for mid, tipo, descripcion, categoria, monto, fecha in filas:
            table.add_row(str(mid), tipo, descripcion, categoria, str(monto), fecha)

        console = Console()
        console.print(table)


# -------------------------------
# Funciones de Balance
# -------------------------------

def calcular_total(tipo):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("SELECT SUM(monto) FROM movimientos WHERE tipo=?", (tipo,))
    total = cursor.fetchone()[0] or 0
    conexion.close()
    return total

def mostrar_balance_mensual():
    ingresos = calcular_total("ingreso")
    gastos = calcular_total("gasto")
    balance = ingresos - gastos
    print("📈 Balance mensual:")
    print(f"   Ingresos: {ingresos}")
    print(f"   Gastos:   {gastos}")
    print(f"   Balance:  {balance}")


# -------------------------------
# Funciones de Importación/Exportación
# -------------------------------

def exportar_movimientos_a_csv(nombre_archivo):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("SELECT tipo, descripcion, categoria, monto, fecha FROM movimientos")
    filas = cursor.fetchall()
    conexion.close()

    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(["Tipo", "Descripción", "Categoría", "Monto", "Fecha"])
        for fila in filas:
            escritor_csv.writerow(fila)

    print(f"✅ Movimientos exportados a {nombre_archivo}.")


def importar_movimientos_desde_csv(nombre_archivo):
    try:
        with open(nombre_archivo, mode='r') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            for fila in lector_csv:
                agregar_movimiento(
                    fila["Tipo"],
                    fila["Descripción"],
                    fila["Categoría"],
                    fila["Monto"],
                    fila["Fecha"]
                )
        print(f"✅ Movimientos importados desde {nombre_archivo}.")
    except FileNotFoundError:
        print("❌ Error: El archivo no existe.")


# -------------------------------
# Función de Log
# -------------------------------

def log_movimiento(movimiento):
    with open("log_movimientos.txt", "a") as f:
        f.write(f"{movimiento['fecha']} - {movimiento['tipo']} - {movimiento['descripcion']} - {movimiento['categoria']} - {movimiento['monto']}\n")
