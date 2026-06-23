import json

ARCHIVO_CONTACTOS = "contactos.json"

def guardar_contactos(contactos):
    with open(ARCHIVO_CONTACTOS, "w") as f:
        json.dump(contactos, f, indent=4)
        
def agregar_contacto(contactos, nombre, telefono, email):
    contactos.append({"nombre": nombre, "telefono": telefono, "email": email})
    guardar_contactos(contactos)

def buscar_contacto(contactos, nombre):
    for contacto in contactos:
        if contacto["nombre"].lower() == nombre.lower():
            return contacto
    return None
