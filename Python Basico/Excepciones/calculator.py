##Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:

def calculadora():
    num_current = 10.0
    while True:
        print(f"Número actual: {num_current}")
        print("Seleccione una operación:")
        print("1. SUMAR")
        print("2. RESTAR")
        print("3. MULTIPLICAR")
        print("4. DIVIDIR")
        print("5. BORRAR RESULTADO Y SALIR")
        option = input("Ingrese el número de la operación que desea realizar: ")
        if option == "5":
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break
        if option not in ["1", "2", "3", "4"]:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
            continue
        try:
            num = float(input("Ingrese el número: "))
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un número.")
            continue
        
        if option == "1":
            num_current += num
        elif option == "2":
            num_current -= num
        elif option == "3":
            num_current *= num
        elif option == "4":
            if num != 0:
                num_current /= num
            else:
                print("Error: No se puede dividir por cero.")
                continue
        
        print(f"Nuevo número actual: {num_current}")

def main():
    calculadora()

if __name__ == "__main__":
    main()






