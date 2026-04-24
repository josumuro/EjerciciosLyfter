##Pida al usuario su nombre
##Si el nombre es numérico (isdigit()), haga raise ValueError("El nombre no puede ser un número")

def is_digit(name, age):
    if name.isdigit():
        raise ValueError("El nombre no puede ser un número")
    elif not age.isdigit():  
        raise ValueError("La edad debe ser un número")
    else:
        return f"Hola {name}!, tienes {age} años."

def main():
    name = str(input("Ingrese su nombre: "))
    age = input("Ingrese su edad: ")  # Como string primero
    try: 
        result = is_digit(name, age)
        print(result)
    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()