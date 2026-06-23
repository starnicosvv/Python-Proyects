import json

def cargar_json(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as f:
            contenido = f.read().strip()
            if not contenido:
                return []
            return json.loads(contenido)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
