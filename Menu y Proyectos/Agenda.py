import funciones_contactos
import Utils
def menu():
    contactos = Utils.cargar_json("contactos.json")
    while True:
        print("\n--- Agenda de Contactos ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Mostrar todos")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            funciones_contactos.agregar_contacto(contactos, nombre, telefono, email)
            print("Contacto agregado.")
        elif opcion == "2":
            nombre = input("Nombre a buscar: ")
            contacto = funciones_contactos.buscar_contacto(contactos, nombre)
            if contacto:
                print("Encontrado:", contacto)
            else:
                print("No existe ese contacto.")
        elif opcion == "3":
            print("Contactos:")
            for c in contactos:
                print(c)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")


