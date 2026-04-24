##Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.

def order_by(string):
    words=string.split("-")
    words.sort()
    return "-".join(words)
result=order_by("papaya-apple-orange")
print(result)