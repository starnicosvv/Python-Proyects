import funciones_calc  

def menu():
    while True:
        print("\n--- Calculadora ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", funciones_calc.sumar(a, b))
        elif opcion == "2":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", funciones_calc.restar(a, b))
        elif opcion == "3":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", funciones_calc.multiplicar(a, b))
        elif opcion == "4":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", funciones_calc.dividir(a, b))
        elif opcion == "5":
            print("Saliendo de la calculadora...")
            break   # <-- aquí sí está dentro del while
        else:
            print("Opción inválida.")
