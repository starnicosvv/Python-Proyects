import funciones_tareas
from db import inicializar_bd

def menu():
    print("-----Agenda de Tareas-----") 
    inicializar_bd()  # crea las tablas si no existen

    while True:
        print("\nSeleccione la operación que desea realizar:")
        print("1. Agregar tarea")
        print("2. Buscar tarea")
        print("3. Eliminar tarea")
        print("4. Mostrar todas las tareas")
        print("5. Editar tarea")
        print("6. Marcar tarea como completada")
        print("7. Salir")
    
        try:
            opcion = int(input("Ingrese el número de la operación: "))
        except ValueError:
            print("❌ Error: Debes ingresar un número válido.")
            continue

        if opcion == 1:
            titulo = input("Ingrese el título de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            fecha_vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")
            funciones_tareas.agregar_tarea(titulo, descripcion, fecha_vencimiento)

        elif opcion == 2:
            titulo = input("Ingrese el título de la tarea a buscar: ")
            tarea = funciones_tareas.buscar_tarea(titulo)
            if tarea:
                print("✅ Tarea encontrada:", tarea)

        elif opcion == 3:
            titulo = input("Ingrese el título de la tarea a eliminar: ")
            funciones_tareas.eliminar_tarea(titulo)

        elif opcion == 4:
            funciones_tareas.mostrar_tareas()

        elif opcion == 5:
            try:
                id_tarea = int(input("Ingrese el ID de la tarea a editar: "))
                nuevo_titulo = input("Nuevo título (dejar vacío si no cambia): ")
                nueva_descripcion = input("Nueva descripción (dejar vacío si no cambia): ")
                nueva_fecha = input("Nueva fecha de vencimiento (YYYY-MM-DD, dejar vacío si no cambia): ")
                funciones_tareas.editar_tarea(id_tarea,
                                              nuevo_titulo if nuevo_titulo.strip() else None,
                                              nueva_descripcion if nueva_descripcion.strip() else None,
                                              nueva_fecha if nueva_fecha.strip() else None)
            except ValueError:
                print("❌ Error: El ID debe ser un número válido.")

        elif opcion == 6:
            try:
                id_tarea = int(input("Ingrese el ID de la tarea a marcar como completada: "))
                funciones_tareas.marcar_tarea_completada(id_tarea)
            except ValueError:
                print("❌ Error: El ID debe ser un número válido.")

        elif opcion == 7:
            print("👋 Saliendo del programa...")
            break

        else:
            print("❌ Opción no válida. Por favor, ingrese un número válido.")
