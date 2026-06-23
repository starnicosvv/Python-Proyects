import json

ARCHIVO_TAREAS = "tareas.json"

def guardar_tareas(tareas):
    with open(ARCHIVO_TAREAS, "w") as f:
        json.dump(tareas, f, indent=4)

def agregar_tarea(tareas, titulo, descripcion, fecha_vencimiento):
    tareas.append({"titulo": titulo, "descripcion": descripcion, "fecha_vencimiento": fecha_vencimiento})
    guardar_tareas(tareas)
    
def buscar_tarea(tareas, titulo):
    for tarea in tareas:
        if tarea["titulo"].lower() == titulo.lower():
            return tarea
    return None

def eliminar_tarea(tareas, titulo):
    tarea = buscar_tarea(tareas, titulo)
    if tarea:
        tareas.remove(tarea)
        guardar_tareas(tareas)
        return True
    return False

def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas registradas.")
    else:
        for tarea in tareas:
            print(f"título: {tarea['titulo']}, descripción: {tarea['descripcion']}, Fecha de vencimiento: {tarea['fecha_vencimiento']}")
