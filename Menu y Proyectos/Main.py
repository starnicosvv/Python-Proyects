import Calculadora
import Agenda
import TODO_list
import GestorDeGastosPersonales
from db import inicializar_bd

# Al iniciar el programa
inicializar_bd()


def menu_principal():
    while True:
        print("\n--- Menú de Proyectos ---")
        print("1. Calculadora")
        print("2. Agenda de contactos")
        print("3. TO-DO list")
        print("4. Gestor de gastos personales")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("Iniciando calculadora...")
            Calculadora.menu()   # submenú de calculadora
        elif opcion == "2":
            print("Iniciando agenda de contactos...")
            Agenda.menu()   # submenú de contactos
        elif opcion == "3":
            print("Iniciando TO-DO list...")
            TODO_list.menu()   # submenú de tareas
        elif opcion == "4":
            print("Iniciando gestor de gastos personales...")
            GestorDeGastosPersonales.menu()   # submenú de gastos
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_principal()
