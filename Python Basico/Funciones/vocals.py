##Cree una función que reciba un string y retorne cuántas vocales contiene el string
def vocal(string,vocals):
    counter=0
    for index in range(len(string)):
        if string[index] in vocals:
            counter += 1
    return counter
string = input("Ingrese un string: ")
vocals = "aeiouAEIOU"
result = vocal(string, vocals)
print("El string contiene", result, "vocales.")