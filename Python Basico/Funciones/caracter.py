##Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto
def cracter(texto, cataracter ):
    counter=0
    for index in range(len(texto)):
        if texto[index] == cataracter:
            counter += 1
    return counter
    print("El caracter no se encuentra en el texto")
    return counter    
texto = input("Ingrese un texto: ")
cataracter = input("Ingrese un caracter: ")
result = cracter(texto, cataracter)
print("El caracter", cataracter, "aparece", result, "veces en el texto.")

    
   