from datetime import datetime
import json
from rich.table import Table
from rich.console import Console

ARCHIVO_MOVIMIENTOS = "movimientos.json"

def guardar_movimientos(movimientos):
    with open(ARCHIVO_MOVIMIENTOS, "w") as f:
        json.dump(movimientos, f, indent=4)

def agregar_movimiento(movimientos, tipo, descripcion, categoria, monto, fecha):
    try:
        monto = float(monto)
        fecha = datetime.strptime(fecha, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        print("Error: El monto debe ser un número válido.")
        print("Error: La fecha debe estar en formato YYYY-MM-DD.")
        return

    movimientos.append({
        "tipo": tipo,
        "descripcion": descripcion,
        "categoria": categoria,
        "monto": monto,
        "fecha": fecha
    })
    guardar_movimientos(movimientos)

def buscar_movimiento(movimientos, descripcion, tipo=None):
    for m in movimientos:
        if m["descripcion"].lower() == descripcion.lower():
            if tipo is None or m["tipo"] == tipo:
                return m
    return None

def eliminar_movimiento(movimientos, descripcion, tipo=None):
    movimiento = buscar_movimiento(movimientos, descripcion, tipo)
    if movimiento:
        movimientos.remove(movimiento)
        guardar_movimientos(movimientos)
        return True
    return False

def mostrar_movimientos(movimientos):
    if not movimientos:
        print("No hay movimientos registrados.")
    else:
        table = Table(title="Movimientos")
        table.add_column("Tipo", justify="center")
        table.add_column("Descripción", justify="center")
        table.add_column("Categoría", justify="center")
        table.add_column("Monto", justify="center")
        table.add_column("Fecha", justify="center")

        for m in movimientos:
            table.add_row(m["tipo"], m["descripcion"], m["categoria"], str(m["monto"]), m["fecha"])

        console = Console()
        console.print(table)

def calcular_total(movimientos, tipo):
    return sum(m["monto"] for m in movimientos if m["tipo"] == tipo)

def balance_mensual(movimientos):
    ingresos = calcular_total(movimientos, "ingreso")
    gastos = calcular_total(movimientos, "gasto")
    return ingresos, gastos, ingresos - gastos

def mostrar_balance_mensual(movimientos):
    ingresos, gastos, balance = balance_mensual(movimientos)
    print(f"Ingresos: {ingresos}")
    print(f"Gastos: {gastos}")
    print(f"Balance mensual: {balance}")

def exportar_movimientos_a_csv(movimientos, nombre_archivo):
    import csv
    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(["Tipo", "Descripción", "Categoría", "Monto", "Fecha"])
        for m in movimientos:
            escritor_csv.writerow([m["tipo"], m["descripcion"], m["categoria"], m["monto"], m["fecha"]])
            
def importar_movimientos_desde_csv(nombre_archivo):
    import csv
    movimientos = []
    with open(nombre_archivo, mode='r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            movimientos.append({
                "tipo": fila["Tipo"],
                "descripcion": fila["Descripción"],
                "categoria": fila["Categoría"],
                "monto": float(fila["Monto"]),
                "fecha": fila["Fecha"]
            })
    return movimientos

def log_movimiento(movimiento):
    with open("log_movimientos.txt", "a") as f:
        f.write(f"{movimiento['fecha']} - {movimiento['tipo']} - {movimiento['descripcion']} - {movimiento['categoria']} - {movimiento['monto']}\n")
