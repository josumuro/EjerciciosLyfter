##Cree una función que retorne la suma de todos los números de una lista.
## función va a tener un parámetro (la lista) y retornar un número (la suma de todos sus elementos).
def my_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

result = my_list([4, 5])
print("La suma de la lista es:", result)