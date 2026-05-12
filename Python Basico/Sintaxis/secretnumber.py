import random
number_secret= random.randint(1, 10) ##forma para escoger un numero aleatorio del 1 al 10
counter=0                             ##Se inicio en cero, porque puse maximo de intentos 5, y llevar la cuenta


while True:  ## para que siga dando vueltas hasta que encuentre el numero correcto
    number_chosen = int(input("Digite el numero que usted guste y crea que es el correcto"))
    counter += 1
    if number_chosen == number_secret:
        print("¡Felicidades! Adivinaste el número.")
        break
    else:
        print("Lo siento, intenta de nuevo.")
  
        