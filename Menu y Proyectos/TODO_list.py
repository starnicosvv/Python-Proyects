import funciones_tareas
import Utils

def menu():
    print ("-----Agenda de Tareas-----") 
    tareas = Utils.cargar_json("tareas.json")
    while True:
        
        print("\nSeleccione la operación que desea realizar:")
        print("1. Agregar tarea")
        print("2. Buscar tarea")
        print("3. Eliminar tarea")
        print("4. Mostrar todas las tareas")
        print("5. Salir")
    
        opcion = int(input("Ingrese el número de la operación: "))
        if opcion == 1:
            titulo = input("Ingrese el título de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            fecha_vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")
            funciones_tareas.agregar_tarea(tareas, titulo, descripcion, fecha_vencimiento)
            print("Tarea agregada exitosamente.")
        elif opcion == 2:
            titulo = input("Ingrese el título de la tarea a buscar: ")
            funciones_tareas.buscar_tarea(tareas, titulo)
        elif opcion == 3:
            titulo = input("Ingrese el título de la tarea a eliminar: ")
            funciones_tareas.eliminar_tarea(tareas, titulo)
            print("Tarea eliminada exitosamente.")
        elif opcion == 4:
            funciones_tareas.mostrar_tareas(tareas)
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

    

