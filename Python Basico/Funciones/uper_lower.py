def find_letter(word):
    upper=0
    lower=0
    for letter in word:
        if letter.isupper():#probe el metodo igualando y no me funciono, luego probe con el metodo isupper() y si me funciono, lo mismo con el metodo islower()
            upper+=1
        elif letter.islower():
            lower+=1
    return upper, lower
def main():
    word=input("Enter a word:")
    upper, lower=find_letter(word)
    print(f"the number of upper case letters is {upper} and {lower} lower case letter , in this word")
main()
