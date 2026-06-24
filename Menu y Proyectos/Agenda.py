import funciones_contactos

def menu():
    

    while True:
        print("\n--- Agenda de Contactos ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Mostrar todos")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            funciones_contactos.agregar_contacto(nombre, telefono, email)

        elif opcion == "2":
            nombre = input("Nombre a buscar: ")
            contacto = funciones_contactos.buscar_contacto(nombre)
            if contacto:
                print("✅ Encontrado:", contacto)
            else:
                print("ℹ️ No existe ese contacto.")

        elif opcion == "3":
            funciones_contactos.mostrar_contactos()

        elif opcion == "4":
            nombre = input("Nombre del contacto a eliminar: ")
            funciones_contactos.eliminar_contacto(nombre)

        elif opcion == "5":
            print("👋 ¡Hasta luego!")
            break

        else:
            print("❌ Opción inválida. Por favor, ingrese un número válido.")
