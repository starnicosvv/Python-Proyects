import funciones_gastos
import Utils

def menu():
    print ("-----Gestor de Gastos Personales-----") 
    movimientos = Utils.cargar_json("movimientos.json")
    while True:
        print("\nSeleccione la operación que desea realizar:")
        print("1. Agregar movimiento")
        print("2. Buscar movimiento")
        print("3. Eliminar movimiento")
        print("4. Mostrar todos los movimientos")
        print("5. importar movimientos desde archivo")
        print("6. exportar movimientos a archivo")
        print("7. mostrar log de movimientos")
        print("8. Salir")
    
        opcion = int(input("Ingrese el número de la operación: "))
        if opcion == 1:
            tipo = input("Ingrese el tipo de movimiento (ingreso/gasto): ")
            descripcion = input("Ingrese la descripción del movimiento: ")
            categoria = input("Ingrese la categoría del movimiento: ")
            monto = float(input("Ingrese el monto del movimiento: "))
            fecha = input("Ingrese la fecha del movimiento (YYYY-MM-DD): ")
            funciones_gastos.agregar_movimiento(movimientos, tipo, descripcion, categoria, monto, fecha)
            funciones_gastos.log_movimiento({
                "tipo": tipo,
                "descripcion": descripcion,
                "categoria": categoria,
                "monto": monto,
                "fecha": fecha
            })
            print("Movimiento agregado exitosamente.")
        elif opcion == 2:
            descripcion = input("Ingrese la descripción del movimiento a buscar: ")
            tipo = input("Ingrese el tipo de movimiento a buscar (opcional): ")
            if tipo.strip() == "":
                tipo = None
            movimiento = funciones_gastos.buscar_movimiento(movimientos, descripcion, tipo)
            if movimiento:
                print("Movimiento encontrado:", movimiento)
            else:
                print("No se encontró el movimiento.")
        elif opcion == 3:
            descripcion = input("Ingrese la descripción del movimiento a eliminar: ")
            tipo = input("Ingrese el tipo de movimiento a eliminar (opcional): ")
            if tipo.strip() == "":
                tipo = None
            if funciones_gastos.eliminar_movimiento(movimientos, descripcion, tipo):
                print("Movimiento eliminado exitosamente.")
            else:
                print("No se encontró el movimiento.")
        elif opcion == 4:
            print("Movimientos:")
            for m in movimientos:
                print(m)
        elif opcion == 5:
            archivo_importar = input("Ingrese el nombre del archivo desde donde importar los movimientos: ")
            movimientos_importados = funciones_gastos.cargar_json(archivo_importar)
            movimientos.extend(movimientos_importados)
            funciones_gastos.guardar_movimientos(movimientos)
            print(f"Movimientos importados desde {archivo_importar}.")
        elif opcion == 6:
            archivo_exportar = input("Ingrese el nombre del archivo donde exportar los movimientos: ")
            funciones_gastos.guardar_json(archivo_exportar, movimientos)
            print(f"Movimientos exportados a {archivo_exportar}.")
        elif opcion == 7:
            with open("log_movimientos.txt", "r") as f:
                log = f.read()
            print("Log de movimientos:")
            print(log)
        elif opcion == 8:
            print("Saliendo del programa...")
            break

