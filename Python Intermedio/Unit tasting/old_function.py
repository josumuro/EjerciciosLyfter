def string_letter(helloworld):
    word = ""
    for letter in helloworld: 
        word=letter+word
    return word
print(string_letter("hello world"))