import funciones_gastos  # aquí tienes las funciones conectadas a SQLite
from db import inicializar_bd  # inicializa la base de datos

def menu():
    print("-----Gestor de Gastos Personales-----") 
    inicializar_bd()  # crea las tablas si no existen

    while True:
        print("\nSeleccione la operación que desea realizar:")
        print("1. Agregar movimiento")
        print("2. Buscar movimiento")
        print("3. Eliminar movimiento")
        print("4. Mostrar todos los movimientos")
        print("5. Mostrar balance mensual")
        print("6. Exportar movimientos a CSV")
        print("7. Importar movimientos desde CSV")
        print("8. Salir")
    
        opcion = int(input("Ingrese el número de la operación: "))
        if opcion == 1:
            tipo = input("Ingrese el tipo de movimiento (ingreso/gasto): ")
            descripcion = input("Ingrese la descripción del movimiento: ")
            categoria = input("Ingrese la categoría del movimiento: ")
            monto = input("Ingrese el monto del movimiento: ")
            fecha = input("Ingrese la fecha del movimiento (YYYY-MM-DD): ")
            funciones_gastos.agregar_movimiento(tipo, descripcion, categoria, monto, fecha)
            print("Movimiento agregado exitosamente.")

        elif opcion == 2:
            descripcion = input("Ingrese la descripción del movimiento a buscar: ")
            tipo = input("Ingrese el tipo de movimiento a buscar (opcional): ")
            if tipo.strip() == "":
                tipo = None
            movimiento = funciones_gastos.buscar_movimiento(descripcion, tipo)
            if movimiento:
                print("Movimiento encontrado:", movimiento)
            else:
                print("No se encontró el movimiento.")

        elif opcion == 3:
            descripcion = input("Ingrese la descripción del movimiento a eliminar: ")
            tipo = input("Ingrese el tipo de movimiento a eliminar (opcional): ")
            if tipo.strip() == "":
                tipo = None
            funciones_gastos.eliminar_movimiento(descripcion, tipo)
            print("Movimiento eliminado (si existía).")

        elif opcion == 4:
            funciones_gastos.mostrar_movimientos()

        elif opcion == 5:
            funciones_gastos.mostrar_balance_mensual()

        elif opcion == 6:
            archivo_exportar = input("Ingrese el nombre del archivo CSV donde exportar: ")
            funciones_gastos.exportar_movimientos_a_csv(archivo_exportar)
            print(f"Movimientos exportados a {archivo_exportar}.")

        elif opcion == 7:
            archivo_importar = input("Ingrese el nombre del archivo CSV desde donde importar: ")
            funciones_gastos.importar_movimientos_desde_csv(archivo_importar)
            print(f"Movimientos importados desde {archivo_importar}.")

        elif opcion == 8:
            print("Saliendo del programa...")
            break
