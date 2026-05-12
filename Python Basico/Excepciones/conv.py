##Cree una función convertir_a_entero(lista) que:
##Reciba una lista de strings
##Intente convertir cada elemento a entero usando int()
##Use try-except para atrapar los errores ValueError
##Si algún elemento no puede convertirse, mostrar "No se pudo convertir el elemento: <valor>" y continuar con los demás

def convertir_a_entero(lista):
    enteros = []
    counter=0
    for element in lista:
        try:
            enteros.append(int(element))
        except ValueError:
            print(f"No se pudo convertir el elemento:,{element}")
    return enteros


def main():
    elementos=input("Ingrese una lista de elementos separados por comas: ")
    elementos=elementos.split(",")
    resultado=convertir_a_entero(elementos)
    print(f"Elementos convertidos a enteros: {resultado}")


if __name__=="__main__":
    main()